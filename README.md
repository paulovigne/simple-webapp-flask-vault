# Simple Web Application + Vault Python SDK HVAC

This is a simple web application using [Python Flask](http://flask.pocoo.org/). 
This is used in the demonstration of developments.
  
  Below are the steps required to get this working on a base linux system.
  
  - Install all required dependencies
  - Install and Configure Web Server
  - Start Web Server

## 1. Start Vault as Dev and create a kv secret engine

    export VAULT_ADDR=http://0.0.0.0:8200
    export VAULT_TOKEN="root"
    vault server -dev -dev-no-store-token
    vault secrets enable -path=app-secrets kv
    vault kv enable-versioning app-secrets
    vault kv put app-secrets/simple-webapp-flask app_color=blue

## 2. Enable a approle login

    vault auth enable approle
    
## 3. Create a policy and role

    cat <<EOF > /tmp/simple-webapp-flask.policy
    path "app-secrets/data/simple-webapp-flask" {
      capabilities = ["read"]
    }
    EOF
    vault policy write simple-webapp-flask /tmp/simple-webapp-flask.policy
    vault write auth/approle/role/simple-webapp-flask-role token_policies="simple-webapp-flask"

## 4. Record Role-ID and Secred-ID to a file

    vault read -field=role_id auth/approle/role/simple-webapp-flask-role/role-id > /tmp/roleid
    vault write -field=secret_id -f auth/approle/role/simple-webapp-flask-role/secret-id > /tmp/secretid

## 5. Install all required dependencies
  
  Python and its dependencies

    Debian/Ubuntu: apt-get install -y python python-setuptools python-dev build-essential python-pip
    Enterprise Linux: yum -y install python3 python3-pip git

   
## 6. Install and Configure Web Server

Install Python dependencies

    pip3 install -r requirements.txt

- Copy app.py or download it from source repository

## 7. Start Web Server

Start web server

    FLASK_APP=app.py flask run --host=0.0.0.0 --port=8080
    
## 8. Test

Open a browser and go to URL

    http://<IP>:8080                        => Hello World!
    http://<IP>:8080/api                    => {status: ok}
