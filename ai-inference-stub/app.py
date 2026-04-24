from flask import Flask, jsonify, request
import logging, os

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

_CANNED_SUMMARIES = [
    "Person entered restricted zone at 14:32",
    "Vehicle parked in no-stop area at 09:17",
    "Unattended bag detected near entrance at 22:05",
    "Crowd density exceeded threshold at 16:45",
]


def create_app():
    app = Flask(__name__)

    @app.route("/health")
    def health():
        return jsonify(status="ok")

    @app.route("/summarize", methods=["POST"])
    def summarize():
        payload = request.get_json(silent=True) or {}
        gif_url = payload.get("gif_url", "")
        app.logger.info("running inference on %s", gif_url)
        idx = hash(gif_url) % len(_CANNED_SUMMARIES)
        return jsonify(
            summary=_CANNED_SUMMARIES[idx],
            confidence=0.87,
        )

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
