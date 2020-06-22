from trimmer.sublog.sublog import wrap_context, log_error, ContextError, log, context_logger, root_context_logger


def test_sublog_wrapping():
    with log_error():
        with wrap_context('initializing', request_id=42):
            with wrap_context('liftoff', speed='zero'):
                raise RuntimeError('dupa')

    with log_error():
        raise ContextError('dupa2', a=5, z='fifteen')

    with log_error():
        raise ContextError('dupa3')

    log.info('success', param='with_param')
    log.warn('attention')
    log.debug('trace')


def test_sublog_traceback():
    with log_error():
        with wrap_context('initializing', request_id=42):
            with wrap_context('liftoff', speed='zero'):
                disaster()


def disaster():
    reason()


def reason():
    raise RuntimeError('disaster')


def test_context_logger():
    with context_logger(request_id=0xdeaddead) as logger:
        logger.debug('got request')
        with context_logger(logger, user='igrek') as logger2:
            logger2.info('logged in', page='home')
            log.warn('im a root')

        logger.debug('logged out')
    log.debug('exited')


def test_root_context_logger():
    log.debug('outside context', a=4)

    with root_context_logger(request_id=0xdeaddead):
        log.debug('got request')

        with root_context_logger(user='igrek'):
            log.info('logged in', page='home')
            with log_error():
                log.warn('im a root')
                raise RuntimeError("I'm a pickle")

        log.debug('logged out')

    log.debug('exited')
