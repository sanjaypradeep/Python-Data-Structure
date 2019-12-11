import pyqrcode

img = pyqrcode.create("Hello World")

img.png("HelloWorldQR.png", scale=6)

