import qrcode

# URL de la carpeta en el servidor local
url = "https://hcimarron.000webhostapp.com/"

# Crear el objeto QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Agregar datos (la URL)
qr.add_data(url)
qr.make(fit=True)

# Crear una imagen del código QR
img = qr.make_image(fill_color="black", back_color="white")

# Guardar la imagen
img.save("codigo_qr.png")
