'''
Setup Statistics
'''
import sys
import httplib2
import json


class _web_connection:
    def __init__(self, connect_args):
        self.connect_args = connect_args
        self.conn = httplib2.Http(timeout=1,
                                  disable_ssl_certificate_validation=True)

    def send(self, data):
        try:
            jdata = json.dumps(data)
            self.conn.request(body=jdata, **self.connect_args)
        except:
            pass


def _error_reporting():
    import traceback

    def hook_exceptions(type_, value_, traceback_):
        etype = traceback.format_exception_only(type_, value_)
        etb = traceback.format_tb(traceback_)
        e_server.send('''{{'type':'{0}', 'trace':'{1}'}}'''.format(etype, etb))
        eout = ''.join(traceback.format_exception(type_, value_, traceback_))
        print eout

    sys.excepthook = hook_exceptions


class stats():

    def __init__(self):
        pass

e_server = _web_connection({
    'method': 'POST',
    'uri': 'http://localhost/error',
    'headers': {'Content-Type': 'application/json'}})
_error_reporting()
raise Exception('TESTING 123')
