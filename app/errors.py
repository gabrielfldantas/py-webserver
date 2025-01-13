from flask import jsonify


def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify(
            {"message": "Bad Request - invalid json."}), 400

    @app.errorhandler(401)
    def unauthorized(e):
        return jsonify({"message": "Unauthorized"}), 401

    @app.errorhandler(403)
    def forbidden(e):
        return jsonify({"message": "Forbidden"}), 403

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"message": "404 Not Found"}), 404

    @app.errorhandler(405)
    def method_not_allowed(e):
        return jsonify({"message": "Method Not Allowed"}), 405

    @app.errorhandler(415)
    def unsupported_media_type(e):
        return jsonify({"message": "Unsupported media type"}), 415

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({"message": "Internal Server Error"}), 500
