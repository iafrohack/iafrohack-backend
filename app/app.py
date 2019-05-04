# noinspection PyInterpreter
from eve import Eve
app = Eve()

@app.route('/hello')
def hello_world():
    return 'how does the world does JP my friends!'

if __name__ == '__main__':
    app.run(host="0.0.0.0")
