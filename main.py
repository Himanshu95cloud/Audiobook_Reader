import pyttsx3
import PyPDF2
from pyttsx3 import engine

book = open('SBS.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
engine.setProperty("rate", 50)
for num in range(10, pages):
    page = pdfReader.getPage(1)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()