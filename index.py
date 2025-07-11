from flask import Flask, request, jsonify

app = Flask(__name__)

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
        "bold_italic": ''.join(chr(0x1D468 + ord(c) - 65) if c.isalpha() and c.isupper() else
                               chr(0x1D482 + ord(c) - 97) if c.isalpha() else c for c in text),
        "monospace": ''.join(chr(0x1D670 + ord(c) - 65) if c.isalpha() and c.isupper() else
                             chr(0x1D68A + ord(c) - 97) if c.isalpha() else c for c in text),
        "script": ''.join(chr(0x1D49C + ord(c) - 65) if c.isalpha() and c.isupper() else
                          chr(0x1D4B6 + ord(c) - 97) if c.isalpha() else c for c in text),
        "bold_script": ''.join(chr(0x1D4D0 + ord(c) - 65) if c.isalpha() and c.isupper() else
                               chr(0x1D4EA + ord(c) - 97) if c.isalpha() else c for c in text),
        "fraktur": ''.join(chr(0x1D504 + ord(c) - 65) if c.isalpha() and c.isupper() else
                           chr(0x1D51E + ord(c) - 97) if c.isalpha() else c for c in text),
        "bold_fraktur": ''.join(chr(0x1D56C + ord(c) - 65) if c.isalpha() and c.isupper() else
                                chr(0x1D586 + ord(c) - 97) if c.isalpha() else c for c in text),
        "double_struck": ''.join(chr(0x1D538 + ord(c) - 65) if c.isalpha() and c.isupper() else
                                 chr(0x1D552 + ord(c) - 97) if c.isalpha() else c for c in text),
        "circled": ''.join(chr(0x24B6 + ord(c) - 65) if c.isalpha() and c.isupper() else
                           chr(0x24D0 + ord(c) - 97) if c.isalpha() else c for c in text),
        "wide": ''.join(chr(0xFF21 + ord(c) - 65) if c.isalpha() and c.isupper() else
                        chr(0xFF41 + ord(c) - 97) if c.isalpha() else c for c in text),
        "sans_serif": ''.join(chr(0x1D5A0 + ord(c) - 65) if c.isalpha() and c.isupper() else
                              chr(0x1D5BA + ord(c) - 97) if c.isalpha() else c for c in text),
        "sans_serif_bold": ''.join(chr(0x1D5D4 + ord(c) - 65) if c.isalpha() and c.isupper() else
                                   chr(0x1D5EE + ord(c) - 97) if c.isalpha() else c for c in text),
        "sans_serif_italic": ''.join(chr(0x1D608 + ord(c) - 65) if c.isalpha() and c.isupper() else
                                     chr(0x1D622 + ord(c) - 97) if c.isalpha() else c for c in text),
        "sans_serif_bold_italic": ''.join(chr(0x1D63C + ord(c) - 65) if c.isalpha() and c.isupper() else
                                          chr(0x1D656 + ord(c) - 97) if c.isalpha() else c for c in text),
        "small_caps": ''.join(chr(0x1D00 + ord(c) - 97) if c.isalpha() and c.islower() and 0x1D00 + ord(c) - 97 <= 0x1D25 else c for c in text.lower()),
        "upside_down": text[::-1].translate(str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.!?()[]{}",
            "ɐqɔpǝɟƃɥᴉɾʞʅɯuodbɹsʇnʌʍxʎz∀𐐒ƆᗡƎℲפHIſʞ⅃WNOԀQᴚS┴∩ΛMXʎZ'˙¡¿)(][}{"
        )),
        "squiggle": ''.join(chr(0x1D4D0 + ord(c) - 65) if c.isupper() else
                            chr(0x1D4EA + ord(c) - 97) if c.islower() else c for c in text)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run()
