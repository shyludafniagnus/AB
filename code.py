import qrcode

url = "https://shyludafniagnus.github.io/A08/"

img = qrcode.make(url)
img.save("birthday_qr.png")

print("QR code generated!")
