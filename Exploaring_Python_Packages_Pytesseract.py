# import all the required packages
import pytesseract as pt
import pdf2image
from PyPDF2 import PdfFileMerger
import os,glob,natsort

# convert all pages to image with 200 dpi
pages = pdf2image.convert_from_path(pdf_path='Trialpdf.pdf', dpi=200)


# required everytime for using tesseract-ocr
# not required if tesseract is in environment variable
# I have not kept in environment variable hence I had to explicitly define it
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# the start page number
pageNumber = 1

# creation of a temporary folder
os.mkdir('tempProj')

# initialising the object for merging of pages afterwards
merger = PdfFileMerger()

# looping through each page/image in pdf and converting it to readable pdf
for page in pages:
    content = pt.image_to_pdf_or_hocr(page, nice=0, extension='pdf',lang = 'eng+jpn')

    # Creating individual pdf page and saving it in the temp folder 
    f = open('tempProj/temp'+str(pageNumber)+'.pdf', 'a+b')
    f.write(bytearray(content))
    f.close()
    print('Page Done: ' + str(pageNumber))
    pageNumber+=1
    
# sorting the pdf files in page number order
listofPdfFiles = natsort.natsorted(glob.glob('tempProj/*.pdf'))  

# merging the files into one pdf
for pdfList in  listofPdfFiles:
    merger.append(pdfList)

merger.write("result.pdf")
merger.close()