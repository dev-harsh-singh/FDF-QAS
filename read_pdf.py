from PyPDF2 import PdfReader

def extract_text(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:                # This loop will visit each page from pdf
        text += page.extract_text()        # this will increase page no one by one

    return text

