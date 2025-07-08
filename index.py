from flask import Flask, request, jsonify

app = Flask(__name__)

def convert(text, base, offset):
    return ''.join(chr(ord(char) + offset) if base <= ord(char) <= base + 25 else char for char in text.lower())

@app.route("/")
def generate_fonts():
    text = request.args.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    result = {
        "bold": ''.join(chr(0x1D400 + ord(c) - 65) if c.isalpha() and c.isupper() else
                        chr(0x1D41A + ord(c) - 97) if c.isalpha() else c for c in text),
        "italic": ''.join(chr(0x1D434 + ord(c) - 65) if c.isalpha() and c.isupper() else
                          chr(0x1D44E + ord(c) - 97) if c.isalpha() else c for c in text),
        "monospace": ''.join(chr(0x1D670 + ord(c) - 65) if c.isalpha() and c.isupper() else
                             chr(0x1D68A + ord(c) - 97) if c.isalpha() else c for c in text),
        "wide": ''.join(chr(0xFF21 + ord(c) - 65) if c.isalpha() and c.isupper() else
                        chr(0xFF41 + ord(c) - 97) if c.isalpha() else c for c in text),
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run()
