import soundcard as sc
import soundfile as sf
import whisper


model = whisper.load_model("medium.en")
result = model.transcribe("out2.mp3")

print("edited this file")

with open("transcription.txt", "w",encoding="utf-8") as f:
    print("transcribing........")
    f.write(result["text"])
    print("Done transcribing....")






