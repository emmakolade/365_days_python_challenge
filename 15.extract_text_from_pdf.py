
from PyPDF2 import PdfReader

reader = PdfReader("Kolade_Olanipekun_Resume.pdf")
page = reader.pages[0]
print(page.extract_text())