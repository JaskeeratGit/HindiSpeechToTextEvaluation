import torch
import os
from transformers import pipeline

directory = r"C:\Users\keera\Desktop\VsCodeWorkspace\TechMahindra\test\audio"

device = "cpu"
transcribe = pipeline(task="automatic-speech-recognition", model="vasista22/whisper-hindi-large-v2", chunk_length_s=30, device=device)
transcribe.model.config.forced_decoder_ids = transcribe.tokenizer.get_decoder_prompt_ids(language="hi", task="transcribe")

textTranscription = ""

for k,filename in enumerate(os.listdir(directory), start = 1):
    
    f = os.path.join(directory, filename)

    splitFilename = f.split("\\")
    fileNumberwav = splitFilename[len(splitFilename)-1]
    fileNumber = fileNumberwav[:-4]
    
    transcribedText = transcribe(f)["text"]

    textTranscription += fileNumber + " " + transcribedText + "\n"

    print(k, "files done")
    if k//20:
        text_file = open("PredictionsWhisperV2Large.txt", "w", encoding = "utf-8")
        text_file.write(textTranscription)