from flask import Flask
import config
import interact

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/switch/<action>')
def switch(action):
#  todo = string.split(action, sep="-")
  output = interact.gembird(action)
  return output 

@app.route('/ml/<action>')
def ml(action):
  output = "foo"
if __name__ == '__main__':
    app.debug=True
    app.run(host=config.listen_ip , port=config.listen_port)


