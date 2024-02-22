

# import tabula
#
# from pdfminer.high_level import extract_pages, extract_text
# from pdfminer.layout import LTTextContainer, LTChar, LTRect, LTFigure

pdf_file = "SAEJ1939-71.pdf"
# with open("SAEJ1939-71.pdf", "rb") as f:
#     text = extract_text(pdf_file)
# print(text)

# file = open("text.txt", "w", encoding='utf-8')
# file.write(text)
# file.close()


from PyPDF2 import PdfReader

reader = PdfReader(pdf_file)
number_of_pages = len(reader.pages)
file = open("text.txt", "a+", encoding='utf-8')
for i in range(number_of_pages):
    page = reader.pages[i]
    text = page.extract_text()
    r = ('Page '+str(i+1)+' of '+str(number_of_pages)+' J1939 –71 Database Report April 15, 2001 ')
    text = text.replace(r, '\n')
    file.write(text)
file.close()

