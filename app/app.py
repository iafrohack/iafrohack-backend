# noinspection PyInterpreter
from eve import Eve
from routes import *
from flask import g
from containers.ConnectionsContainer import ConnectionsContainer
from settings import APP_SECRET_KEY
from flask_cors import CORS

app = Eve()
CORS(app)
app.register_blueprint(routes)
app.secret_key = APP_SECRET_KEY

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

connections_container = ConnectionsContainer().db()
Session = connections_container.get_connection()

@app.teardown_appcontext
def cleanup(resp_or_exc):
    Session.remove()
