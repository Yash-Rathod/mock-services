from flask import Flask, jsonify, request
import logging, os, uuid

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


def create_app():
    app = Flask(__name__)

    @app.route("/health")
    def health():
        return jsonify(status="ok")

    @app.route("/process", methods=["POST"])
    def process():
        payload = request.get_json(silent=True) or {}
        camera_id = payload.get("camera_id", "unknown")
        frames = payload.get("frames", 0)
        app.logger.info("processing %d frames from %s", frames, camera_id)
        gif_key = f"{camera_id}/{uuid.uuid4().hex}.gif"
        return jsonify(
            gif_url=f"s3://mock-baktrack-clips/{gif_key}",
            duration_ms=frames * 15,
        )

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

