class ApiClient(object):
    """ Base class for invoking business logic functionality """

    def __init__(self, host, port):
        self._host = host
        self._port = port
        
    def connect(self):
        self.server = conn = http.client.HTTPConnection(self._host, self._port)

class EfsApiClient(ApiClient):
    """ Concrete class to communicate with RAS API, invokes CsmApi directly """

    def __init__(self):
        super().__init__(host="127.0.0.1", port="8081")

    def call(self, command):
        """ Call remote API method synchronously. Response is received over the  callback channel """

        #self._command_name = command.name()
        self._action = command.action()
        self._args = command.args()

        
        return self._response

        # Form and send REST request and receive response in  self._response
        
