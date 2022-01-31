import pyttsx3
import PyPDF2
pdf = open('english_poems.pdf', 'rb')
PdfReader = PyPDF2.PdfFileReader(pdf)
pages = PdfReader.numPages

speaker = pyttsx3.init()
for no in range(80, pages):
    page = PdfReader.getPage(no)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()