# noinspection PyInterpreter
from eve import Eve
from routes import *
from flask_sqlalchemy import SQLAlchemy
from flask import g
from containers.ConnectionsContainer import ConnectionsContainer

app = Eve()

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

connections_container = ConnectionsContainer().db()
Session = connections_container.get_connection()

@app.teardown_appcontext
def cleanup(resp_or_exc):
    Session.remove()
