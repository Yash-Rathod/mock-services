from flask import Flask, jsonify, request
import logging, os

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

def create_app():
    app = Flask(__name__)

    @app.route("/health")
    def health():
        return jsonify(status="ok")

    @app.route("/notify", methods=["POST"])
    def notify():
        payload = request.get_json(silent=True) or {}
        app.logger.info("notification received: %s", payload)
        return jsonify(accepted=True, payload=payload), 202

    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))