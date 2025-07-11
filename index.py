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
                            chr(0x1D4EA + ord(c) - 97) if c.islower() else c for c in text),
        "squared": ''.join(chr(0x1F130 + ord(c) - 65) if c.isupper() and 65 <= ord(c) <= 90 else c for c in text),
        "fullwidth_upper": ''.join(chr(0xFF21 + ord(c) - 65) if c.isupper() else c for c in text),
        "reverse": text[::-1],
        "tiny": ''.join({
            'a': 'ᵃ', 'b': 'ᵇ', 'c': 'ᶜ', 'd': 'ᵈ', 'e': 'ᵉ', 'f': 'ᶠ', 'g': 'ᵍ',
            'h': 'ʰ', 'i': 'ᶦ', 'j': 'ʲ', 'k': 'ᵏ', 'l': 'ˡ', 'm': 'ᵐ', 'n': 'ⁿ',
            'o': 'ᵒ', 'p': 'ᵖ', 'q': 'ᑫ', 'r': 'ʳ', 's': 'ˢ', 't': 'ᵗ', 'u': 'ᵘ',
            'v': 'ᵛ', 'w': 'ʷ', 'x': 'ˣ', 'y': 'ʸ', 'z': 'ᶻ'
        }.get(c, c) for c in text.lower()),
        "underline": ''.join(c + '\u0332' for c in text),
        "strikethrough": ''.join(c + '\u0336' for c in text),
        "parenthesized": ''.join(chr(0x1F110 + ord(c) - 65) if c.isupper() and 65 <= ord(c) <= 90 else c for c in text),
        "superscript": ''.join({
            '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
            '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
            'a': 'ᵃ', 'b': 'ᵇ', 'c': 'ᶜ', 'd': 'ᵈ', 'e': 'ᵉ',
            'f': 'ᶠ', 'g': 'ᵍ', 'h': 'ʰ', 'i': 'ⁱ', 'j': 'ʲ',
            'k': 'ᵏ', 'l': 'ˡ', 'm': 'ᵐ', 'n': 'ⁿ', 'o': 'ᵒ',
            'p': 'ᵖ', 'q': 'ᑫ', 'r': 'ʳ', 's': 'ˢ', 't': 'ᵗ',
            'u': 'ᵘ', 'v': 'ᵛ', 'w': 'ʷ', 'x': 'ˣ', 'y': 'ʸ', 'z': 'ᶻ'
        }.get(c.lower(), c) for c in text),
        "subscript": ''.join({
            '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄',
            '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉',
            'a': 'ₐ', 'e': 'ₑ', 'h': 'ₕ', 'i': 'ᵢ', 'j': 'ⱼ',
            'k': 'ₖ', 'l': 'ₗ', 'm': 'ₘ', 'n': 'ₙ', 'o': 'ₒ',
            'p': 'ₚ', 'r': 'ᵣ', 's': 'ₛ', 't': 'ₜ', 'u': 'ᵤ',
            'v': 'ᵥ', 'x': 'ₓ'
        }.get(c.lower(), c) for c in text),
        "mirror": text[::-1].translate(str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
            "zʎxʍʌnʇsɹbdouɯʃʞᴉɥƃɟǝpɔqɐZ⅄XＭΛ∩⊥SᴚὉՈWИOИM⅃ʞIH⅁ℲƎᗡƆ𐐒∀➊➋➌➍➎➏➐➑➒"
        ))
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run()
