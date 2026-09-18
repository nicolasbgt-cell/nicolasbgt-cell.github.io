import qrcode

data = "https://nicolasbgt-cell.github.io/"
img = qrcode.make(data)
img.save("qrcode_site_perso.png")
