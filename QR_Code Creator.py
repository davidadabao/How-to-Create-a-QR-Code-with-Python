import pyqrcode
import png

link = "http://www.google.com"
qr_code = pyqrcode.create (link)
qr_code.png("google.png", scale = 100)

