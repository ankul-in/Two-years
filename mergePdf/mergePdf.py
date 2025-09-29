#https://youtu.be/VeW6Y8EOQHw

from glob import glob
from pikepdf import Pdf

new_pdf=Pdf.new()
for file in glob("*.pdf"):
    old_pdf=Pdf.open(file)

    new_pdf.pages.extend(old_pdf.pages)
new_pdf.save("demo.pdf")

