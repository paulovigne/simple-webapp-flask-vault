import os
import hvac
from flask import Flask
app = Flask(__name__)

roleid_file=open("/authentication/account.txt","r")
lines=roleid_file.readlines()
roleid_file_value=lines[0]
roleid_file.close()

secretid_file=open("/authentication/account.txt","r")
lines=secretid_file.readlines()
secretid_file_value=lines[0]
secretid_file.close()

client = hvac.Client()

client.auth.approle.login(
    role_id=roleid_file_value,
    secret_id=secretid_file_value,
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
