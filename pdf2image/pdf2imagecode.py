#https://youtu.be/sGmjb6UJdpU

from pdf2image import convert_from_path

old_pdf=convert_from_path(r"pdf2image\Cisco.pdf",poppler_path=r"D:\PY\pdf2image\poppler-22.04.0")
for i in range(len(old_pdf)):
    old_pdf[i].save("new"+str(i)+".jpg","JPEG")