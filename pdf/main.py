from PyPDF2 import PdfFileReader, PdfFileWriter

template = PdfFileReader(open('resume.pdf', 'rb'))
watermark = PdfFileReader(open('draft.pdf', 'rb'))
output = PdfFileWriter()

for n in range(template.numPages):
    page = template.getPage(n)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    with open('example.pdf', 'wb') as filehandle_output:
        output.write(filehandle_output)
