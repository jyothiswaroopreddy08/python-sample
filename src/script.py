from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return 'Hello World'

@app.route('/demo')
def demo():
    return 'Welcome to python demo!'

if __name__ == '__main__':
    app.run(port=5000)
