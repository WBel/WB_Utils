import logging
LOG = logging.getLogger(__name__)

def run_test():
    """Returns true to user to test that this toolkit has installed correctly

        Usage:
            import mechRig_toolkit
            rigging_toolkit.run_test()
    """
    LOG.info('Rigging Toolkit installed successfully')
    return True
