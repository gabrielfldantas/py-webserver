from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os

load_dotenv()

auth_method = os.getenv('AUTH_METHOD')

if auth_method == 'basic':
    basic_user = os.getenv('USER_AUTH')
    basic_pass = os.getenv('PASS_AUTH')
    auth = HTTPBasicAuth()
    users = {
    basic_user: generate_password_hash(basic_pass)}

    @auth.verify_password
    def verify_password(username, password):
        if username in users and check_password_hash(users.get(username), password):
            return username
else:
    api_token = os.getenv('TOKEN_AUTH')
    auth = HTTPTokenAuth(header='X-API-Key')
    @auth.verify_token
    def verify_token(token):
        return token == api_token
    
@auth.error_handler
def auth_error(status):
    return jsonify({"message": "Unauthorized"}), status