import fitz
from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter

input_file = 'new.pdf'
output_file = 'draft.pdf'
draft_image = 'draft.png'

position = fitz.Rect(70, 0, 550, 900)

file_handle = fitz.open(input_file)

for page in file_handle.pages():
    page.insertImage(position, draft_image)
    file_handle.save(output_file)
