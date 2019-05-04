# noinspection PyInterpreter
from eve import Eve
app = Eve()

@app.route('/man')
def hello_world():
    return 'Yes we can my Friend!!'

if __name__ == '__main__':
    app.run(host="0.0.0.0")
