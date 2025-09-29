#https://youtu.be/dTZgwIOYjEI

# import pikepdf

# old_pdf = pikepdf.Pdf.open(r"D:\PY\RotatePdf\Cisco.pdf")

# for i in old_pdf.pages:
#     i.rotate = 180
#     old_pdf.save(r"D:\PY\RotatePdf\new_pdf.pdf")

# import pikepdf

# old_pdf = pikepdf.Pdf.open(r"D:\PY\RotatePdf\Cisco.pdf")

# for i in old_pdf.pages:
#     i.rotate = 180
#     old_pdf.save(r"D:\PY\RotatePdf\new_pdf.pdf")

import pikepdf

with pikepdf.open(r"D:\PY\RotatePdf\Cisco.pdf") as pdf:
    for page in pdf.pages:
        current_rotation = page.get('/Rotate', 0)
        page['/Rotate'] = (current_rotation + 90) % 360  
    pdf.save(r"D:\PY\RotatePdf\rotated_output.pdf")