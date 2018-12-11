from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hey Its Python Flask application!!!'

@app.route('/awesome')
def awesome():
  return 'Hey its Python Flask application Test!'

if __name__ == '__main__':
  app.run()
