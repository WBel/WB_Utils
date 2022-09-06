import logging
LOG = logging.getLogger(__name__)

def run_test():
    """Returns true to user to test that this toolkit has installed correctly

        Usage:
            import WB_Utils
            WB_Utils.run_test()
    """
    LOG.info('WB Utils installed successfully')
    return True
