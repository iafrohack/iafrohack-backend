from interface import implements
from providers.connections.ConnectionsProviderInterface import ConnectionsProviderInterface
import json
from google.cloud import firestore

# Connection provider for Google Firestore
# @see https://cloud.google.com/firestore/docs/quickstart-servers
class FireStoreProvider(implements(ConnectionsProviderInterface)):

    #def __init__(self):


    @property
    def get_connection(self):
                # @see https://cloud.google.com/firestore/docs/quickstart-servers
        # Project ID is determined by the GCLOUD_PROJECT environment variable
        self.client = firestore.Client()
        return self.client
