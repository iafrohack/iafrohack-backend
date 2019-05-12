from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from interface import implements
from providers.connections.ConnectionsProviderInterface import ConnectionsProviderInterface


class Postgres(implements(ConnectionsProviderInterface)):

    @property
    def get_connection(self):

        db_uri = "" # db connection string

        engine = create_engine(db_uri)

        Session = scoped_session(sessionmaker(bind=engine))
        return Session
