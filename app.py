import os
import hvac
from flask import Flask
app = Flask(__name__)

client = hvac.Client()

client.auth.approle.login(
    role_id='<some_role_id>',
    secret_id='<some_secret_id>',
)

read_response = client.secrets.kv.read_secret_version(path='app-secrets/simple-webapp-flask')
app_color = read_response['data']['data']['app_color']

@app.route("/")
def main():
    return '<h1><p style="color:' + app_color + '">Hello World</p></h1>'

@app.route('/api')
def hello():
    return '{status: ok}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
