import qrcode
from PIL import Image
import os
print(os.getcwd())

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data("how are you doing mate??")
qr.make(fit=True)
img=qr.make_image(fill_color="yellow",back_color="black")
img.save(r"D:\PY\QRcode\Talks.png")