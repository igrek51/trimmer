import datetime
import sys
import traceback
from contextlib import contextmanager
from typing import Dict, Any

C_RESET = '\033[0m'
C_GREEN = '\033[0;32m'
C_BLUE = '\033[0;34m'
C_CYAN = '\033[0;36m'
C_RED_BOLD = '\033[1;31m'
C_GREEN_BOLD = '\033[1;32m'
C_YELLOW_BOLD = '\033[1;33m'


class ContextError(RuntimeError):
    def __init__(self, message: str, **ctx):
        super().__init__(message)
        self.ctx = ctx


@contextmanager
def wrap_context(context_name: str, **ctx):
    try:
        yield
    except ContextError as e:
        merged_context = {**ctx, **e.ctx}
        raise ContextError(f'{context_name}: {e}', **merged_context) from e
    except Exception as e:
        raise ContextError(f'{context_name}: {e}', **ctx) from e


@contextmanager
def log_error(print_traceback: bool = True):
    try:
        yield
    except ContextError as e:
        if print_traceback:
            ex_type, ex, tb = sys.exc_info()
            # traceback.format_exception(ex_type, ex, tb)
            t1 = traceback.TracebackException(type(ex_type), ex, tb, limit=None)
            while t1.__cause__ is not None:
                t1 = t1.__cause__

            frames = traceback.extract_tb(t1.exc_traceback)

            lines = [f'{frame.filename}:{frame.lineno}' for frame in frames
                     if not frame.filename.endswith('/sublog.py')]
            tb = ','.join(lines)
            e.ctx['traceback'] = tb

        error(str(e), **e.ctx)
    except KeyboardInterrupt:
        print()
        debug('KeyboardInterrupt')
        exit(1)
    except Exception as e:
        error(str(e))


def _display_context(ctx: Dict[str, Any]) -> str:
    if len(ctx) == 0:
        return ''
    keys = ctx.keys()
    parts = [_display_context_var(key, ctx[key]) for key in keys]
    return " ".join(parts)


def _display_context_var(var: str, val: str) -> str:
    val = str(val)
    if ' ' in val:
        return f'{C_GREEN}{var}="{C_GREEN_BOLD}{val}{C_GREEN}"{C_RESET}'
    else:
        return f'{C_GREEN}{var}={C_GREEN_BOLD}{val}{C_RESET}'


def error(message: str, **ctx):
    print_log(message, f'{C_RED_BOLD}ERROR{C_RESET}', ctx)


def warn(message: str, **ctx):
    print_log(message, f'{C_YELLOW_BOLD}WARN {C_RESET}', ctx)


def info(message: str, **ctx):
    print_log(message, f'{C_BLUE}INFO {C_RESET}', ctx)


def debug(message: str, **ctx):
    print_log(message, f'{C_GREEN}DEBUG{C_RESET}', ctx)


def print_log(message: str, level: str, ctx: Dict[str, Any]):
    display_context = _display_context(ctx)
    timestamp_part = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if display_context:
        print(f'[{C_CYAN}{timestamp_part}{C_RESET}] [{level}] {message} {display_context}')
    else:
        print(f'[{C_CYAN}{timestamp_part}{C_RESET}] [{level}] {message}')
