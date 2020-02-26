class ApiClient(object):
    """ Base class for invoking business logic functionality """

    def __init__(self, server):
        self._server = server

class EfsApiClient(ApiClient):
    """ Concrete class to communicate with RAS API, invokes CsmApi directly """

    def __init__(self):
        super(CsmApiClient, self).__init__(None)
        CsmApi.init()

    def call(self, command):
        """ Call remote API method synchronously. Response is received over the  callback channel """

        self._command_name = command.name()
        self._action = command.action()
        self._args = command.args()

        // Form and send REST request and receive response in  self._response
       return self._response

