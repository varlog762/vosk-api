from vosk import Model, KaldiRecognizer
import wave
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Загружаем модель Vosk
ru_model = Model("models/vosk-model-ru-0.42")

@app.route("/test", methods=["GET"])
def test():
    return jsonify(message="Hello Dude!")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files["audio"]

    with wave.open(audio_file.stream, "rb") as wf:
        rec = KaldiRecognizer(ru_model, wf.getframerate())
        rec.SetWords(True)

        result = ""
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result += rec.Result()

        final_result = rec.FinalResult()
        final_result_json = json.loads(final_result) if final_result else {}

    return jsonify(final_result_json)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2700, debug=True)