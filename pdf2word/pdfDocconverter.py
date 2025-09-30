#https://youtu.be/fJ-dzdlejyc
from pdf2docx import Converter

old_pdf = r"D:\PY\pdf2word\Cisco.pdf"
new_doc = r"new.docx"


obj=Converter(old_pdf)
obj.convert(new_doc)
obj.close()