from vosk import Model, KaldiRecognizer
import wave
import json
from flask import Flask, request

app = Flask(__name__)

# Загружаем модель Vosk
# model = Model("vosk-model-small-en-us-0.15")

@app.route("/transcribe", methods=["GET"])
def test():
    print('it is work!')
    return json.loads("it is work!")
    
# def transcribe():
    # if "audio" not in request.files:
    #     return {"error": "No audio file provided"}, 400
    
    # audio_file = request.files["audio"]
    # with wave.open(audio_file, "rb") as wf:
    #     rec = KaldiRecognizer(model, wf.getframerate())
    #     rec.SetWords(True)

    #     while True:
    #         data = wf.readframes(4000)
    #         if len(data) == 0:
    #             break
    #         rec.AcceptWaveform(data)

    # return json.loads(rec.Result())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2700)