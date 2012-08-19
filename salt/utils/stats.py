'''
Setup Statistics
'''
import sys


def _error_reporting():
    import traceback

    def hook_exceptions(type_, value_, traceback_):
        lines = traceback.format_exception(type_, value_, traceback_)
        print '''
####################################
#### Unhandled Exception Caught ####
####################################

{0}
####################################
'''.format(''.join(lines))

    sys.excepthook = hook_exceptions


class stats():

    def __init__(self):
        pass

_error_reporting()
