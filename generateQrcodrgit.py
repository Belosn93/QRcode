import qrcode
link_to_convert = ''
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10, #размер каждого квадратика в QR-коде в px
    border=4,
)
qr.add_data(link_to_convert)
qr.make(fit=True) # автоматически определяет размер QR-кода
img = qr.make_image(fill_color="black", back_color="white")
img.save("meme.png")
img.show()

