import soundcard as sc
import soundfile as sf
import whisper


model = whisper.load_model("medium.en")
result = model.transcribe("out2.mp3")

# output_file_name = "out2.mp3"  # file name
# samplerate = 48000  # (Hz) sampling rate
# record_sec = 30  # (sec) duration of recording audio
#
#
# with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=samplerate) as mic:
#     # record audio with loopback from default speaker
#     print("Recording....")
#     data = mic.record(numframes=samplerate * record_sec)
#
#     # change "data=data[:,0]" to "data=data", if you would like to write audio as multiple channels
#     sf.write(file=output_file_name, data=data[:, 0], samplerate=samplerate)
#     print("Done recording....")

# print(result["text"])

with open("transcription.txt", "w",encoding="utf-8") as f:
    print("transcribing........")
    f.write(result["text"])
    print("Done transcribing....")






