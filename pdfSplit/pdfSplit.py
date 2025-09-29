#https://youtu.be/kSlz2PP8Ibo


import pikepdf

old_pdf = pikepdf.Pdf.open(r"D:\PY\pdfSplit\Cisco.pdf")

for n,page_cont in enumerate(old_pdf.pages):
    new_pdf=pikepdf.Pdf.new()
    new_pdf.pages.append(page_cont)
    name="test"+str(n)+".pdf"
    new_pdf.save(name)