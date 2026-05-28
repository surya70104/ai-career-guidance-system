from PyPDF2 import PdfReader

def extract_resume_text(file):

    text = ""

    pdf = PdfReader(file)

    for page in pdf.pages:
        text += page.extract_text()

    return text.lower()