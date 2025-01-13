from flask import jsonify, Flask
from app.models.health_model import check_health
from app.auth import auth


@auth.login_required
def health_check():
   status, message = check_health()
   return jsonify({
       'database': {
           'status': 'healthy' if status else 'unhealthy',
           'message': message
       }
   }), 200 if status else 500

def register_health_routes(app: Flask):
   app.add_url_rule('/health', view_func=health_check, methods=['GET'])