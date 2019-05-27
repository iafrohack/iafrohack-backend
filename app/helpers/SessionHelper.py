from flask import session
import uuid

class SessionHelper(object):

    SESSION_ID_KEY = 'session_id'

    def get_session_id(self, session: session) -> str:
        """
        Get a unique identifier of a session
        :param session:
        :return:
        """

        if not self.SESSION_ID_KEY in session:
            session[self.SESSION_ID_KEY] = uuid.uuid4()

        return session[self.SESSION_ID_KEY]


