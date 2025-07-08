from flask import Flask, request, jsonify
import fancytext

app = Flask(__name__)

@app.route('/')
def font_generator():
    text = request.args.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400

    fonts = fancytext.get_fancy(text)
    return jsonify(fonts)

if __name__ == '__main__':
    app.run()
