

from database import get_connection
from read_pdf import extract_text

def upload_document():
    pdf_path = input("Enter PDF Path : ").strip().replace('"', '')

    text = extract_text(pdf_path)

    paragraphs = text.split("\n")

    conn = get_connection()

    cursor = conn.cursor()

    for para in paragraphs:

        para = para.strip()

        if para:

            cursor.execute(
                "INSERT INTO documents(paragraph, file_name) VALUES(%s, %s)",
                (para, pdf_path)
            )

    conn.commit()

    cursor.close()
    conn.close()

    print("PDF Data Stored Successfully")