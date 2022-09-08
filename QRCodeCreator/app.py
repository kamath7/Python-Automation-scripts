import qrcode 

img = qrcode.make("https://google.com/")

img.save('lalle.png')