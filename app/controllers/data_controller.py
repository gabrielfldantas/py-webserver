from flask import Blueprint, request, jsonify
from app.models.data_model import save_request_data
from app.auth import auth


data_bp = Blueprint('data', __name__)

@auth.login_required
def store_request_data():
    data = {
        'method': request.method,
        'endpoint': request.path,
        'headers': dict(request.headers),
        'body': request.get_json()
    }
    success, message = save_request_data(**data)
    return jsonify({'message': message}), 201 if success else 500

data_bp.add_url_rule('/booking', view_func=store_request_data, methods=['POST'])
data_bp.add_url_rule('/gps', view_func=store_request_data, methods=['POST'])
data_bp.add_url_rule('/ride_operational_info', view_func=store_request_data, methods=['POST'])
data_bp.add_url_rule('/relation', view_func=store_request_data, methods=['POST'])