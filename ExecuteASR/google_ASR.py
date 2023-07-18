import speech_recognition as sr
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence

# give the location of the .wav audio file
directory = r"C:\Users\keera\Desktop\VsCodeWorkspace\TechMahindra\test\audio"
for filename in os.listdir(directory):
    f = os.path.join(directory,filename)
    
# initialize the recognizer
r = sr.Recognizer()
def transcribe_audio(path):
    # use the audio file as the audio source
    with sr.AudioFile(path) as source:
        audio_listened = r.record(source)
        # converting it to text
        text = r.recognize_google(audio_listened, language = 'hi-In')
    return text

# looping through the audiofiles in the directory, getting transcription for each and writing it to file in format that matches ground truth
textTranscription = ""
for k,filename in enumerate(os.listdir(directory)[3356:], start = 3357):
    f = os.path.join(directory, filename)
    splitFilename = f.split("\\")
    fileNumberwav = splitFilename[len(splitFilename)-1]
    fileNumber = fileNumberwav[:-4]
    try:
        transcribedText = transcribe_audio(f)
    except sr.UnknownValueError as e:
        textTranscription += fileNumber + " " + "unknown" + "\n"
    else:
        transcribedTexttext = f"{transcribedText.capitalize()}. "
        textTranscription += fileNumber + " " + transcribedText + "\n"
    #textTranscription += fileNumber + " " + transcribedText + "\n"
    print(k, "files done")
    if k//100:
        text_file = open("PredictionsGooglePart3.txt", "w", encoding = "utf-8")
        text_file.write(textTranscription)
