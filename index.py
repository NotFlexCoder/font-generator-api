from flask import Flask, request, jsonify
import fancyfonts.fancy as fancy

app = Flask(__name__)

@app.route("/")
def generate_all_fonts():
    text = request.args.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    fonts = {}
    for style in dir(fancy):
        if callable(getattr(fancy, style)) and not style.startswith("_"):
            try:
                fonts[style] = getattr(fancy, style)(text)
            except:
                continue

    return jsonify(fonts)
