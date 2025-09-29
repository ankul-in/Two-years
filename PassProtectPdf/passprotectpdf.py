import pikepdf

old_pdf=pikepdf.Pdf.open(r"PassProtectPdf\Cisco.pdf")

no_extr=pikepdf.Permissions(extract=False)

old_pdf.save("D:\PY\PassProtectPdf\pro_new.pdf",encryption=pikepdf.Encryption(user="123abc",owner="arseces",allow=no_extr))