from flask import Flask
import time

import config
import interact
import auth

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/switch/<action>')
@auth.requires_auth
def switch(action):
  message = interact.gembird(action)
  otime =  time.asctime(time.localtime(time.time()))
  return "%s <br> %s" % (otime, message)

@app.route('/ml/<action>')
def ml(action):
  output = "foo"

@app.route('/favicon.ico')
def favicon():
  return app.send_static_file("favicon.ico") 


if __name__ == '__main__':
#    app.debug=True
    app.run(host=config.listen_ip , port=config.listen_port)
