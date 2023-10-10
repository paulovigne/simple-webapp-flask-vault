import os
import hvac
from flask import Flask
app = Flask(__name__)

def getValueFromFile(filename):
    import imp
    f = open(filename)
    global data
    data = f.readline()
    f.close()
    print(data)

client = hvac.Client(
    url='http://127.0.0.1:8200',
    verify=False
)

client.auth.approle.login(
    role_id=getValueFromFile(/tmp/roleid),
    secret_id=getValueFromFile(/tmp/secretid)
)

read_response = client.secrets.kv.read_secret_version(mount_point='app-secrets', path='simple-webapp-flask')
app_color = read_response['data']['data']['app_color']

@app.route("/")
def main():
    return '<h1><p style="color:' + app_color + '">Hello World</p></h1>'

@app.route('/api')
def hello():
    return '{status: ok}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
