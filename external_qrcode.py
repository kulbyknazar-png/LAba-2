import qrcode


def create_qr(text):
    qr = qrcode.make(text)
    qr.save("qr_code.png")
    return "QR-код створено"