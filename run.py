from waitress import serve
from app import create_app
from dotenv import load_dotenv
import os

load_dotenv()

w_host = os.getenv('WAITRESS_HOST')
w_port = int(os.getenv('WAITRESS_PORT'))

app = create_app()

if __name__ == '__main__':
    serve(app, host=w_host, port=w_port)