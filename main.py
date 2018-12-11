from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hey its Python Flask application!'

@app.route('/test')
def hello_world():
  return 'Hey its Python Flask application Test!'

if __name__ == '__main__':
  app.run()
