from interface import Interface

class ConnectionsProviderInterface(Interface):

    @property
    def get_connection(self):
        pass
