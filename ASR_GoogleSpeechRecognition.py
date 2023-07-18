import speech_recognition as sr
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence

# give the location of the .wav audio file
directory = r"C:\Users\keera\Desktop\VsCodeWorkspace\TechMahindra\test\audio"
for filename in os.listdir(directory):
    f = os.path.join(directory,filename)
    
#filename = r"C:\Users\keera\Desktop\VsCodeWorkspace\test\audio\0116_003.wav"

# initialize the recognizer
r = sr.Recognizer()
def transcribe_audio(path):
    # use the audio file as the audio source
    with sr.AudioFile(path) as source:
        audio_listened = r.record(source)
        # try converting it to text
        text = r.recognize_google(audio_listened, language = 'hi-In')
    return text

# a function that splits the audio file into chunks on silence
# and applies speech recognition
'''def get_large_audio_transcription_on_silence(path):
    """Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks"""
    # open the audio file using pydub
    sound = AudioSegment.from_file(path)  
    # split audio sound where silence is 500 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        try:
            text = transcribe_audio(chunk_filename)
        except sr.UnknownValueError as e:
            whole_text += "unknown"
        else:
            text = f"{text.capitalize()}. "
            print(chunk_filename, ":", text)
            whole_text += text
    
    # return the text for all chunks detected
    return whole_text'''

# creating the name of the txt file
#splitfilename=filename.split('\\')
#name = splitfilename[len(splitfilename)-1]
#txtfilename = "TextFor_" + name +".txt"
#print(splitfilename, txtfilename)

# opening and writing to the txt file
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


#text_file = open(txtfilename, "w",encoding="utf-8")
#text_file.write(transcribedText)


