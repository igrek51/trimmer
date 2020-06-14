from trimmer.sublog.sublog import wrap_context, log_error, ContextError, info, warn, debug


def test_sublog_wrapping():
    with log_error():
        with wrap_context('initializing', request_id=42):
            with wrap_context('liftoff', speed='zero'):
                raise RuntimeError('dupa')

    with log_error():
        raise ContextError('dupa2', a=5, z='fifteen')

    with log_error():
        raise ContextError('dupa3')

    info('success', param='with_param')
    warn('attention')
    debug('trace')


def test_sublog_traceback():
    with log_error():
        with wrap_context('initializing', request_id=42):
            with wrap_context('liftoff', speed='zero'):
                disaster()


def disaster():
    reason()


def reason():
    raise RuntimeError('disaster')
