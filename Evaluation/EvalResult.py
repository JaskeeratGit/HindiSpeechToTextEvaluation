import jiwer
predictionsFile = open(r"C:\Users\keera\Desktop\VsCodeWorkspace\PredictionsGoogle.txt", "r", encoding= "utf-8")
groundTruthFile = open(r"C:\Users\keera\Desktop\VsCodeWorkspace\TechMahindra\testDataPrep\Formatted\text", "r", encoding= "utf-8")

predictions = predictionsFile.read()
groundTruth = groundTruthFile.read()

wer = jiwer.wer(groundTruth, predictions)
cer = jiwer.cer(groundTruth, predictions)
print("wer: ",wer, "cer: ",cer)


