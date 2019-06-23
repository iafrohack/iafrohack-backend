from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from interface import implements
from providers.connections.ConnectionsProviderInterface import ConnectionsProviderInterface
import json

class Postgres(implements(ConnectionsProviderInterface)):

    @property
    def get_connection(self):

        with open('/var/lib/iafrohack/.config/gcloud/postgres_uri.json', 'r') as json_config:
            config_data = json_config.read()

        config = json.loads(config_data) # db connection config

        engine = create_engine(config['uri'])

        Session = scoped_session(sessionmaker(bind=engine))
        return Session
