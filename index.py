from flask import Flask, request, jsonify
from fancy_text import generate_fancy_text

app = Flask(__name__)

@app.route('/')
def font_generator():
    text = request.args.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    try:
        fonts = generate_fancy_text(text)
        return jsonify(fonts)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
