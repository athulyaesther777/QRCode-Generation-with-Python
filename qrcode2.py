import qrcode


# Create a QR Code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add data to the QR Code
qr.add_data("https://www.linkedin.com/in/athulya-esther-b65740220")
qr.make(fit=True)

# Create an image from the QR Code instance
# Use 'fill_color' and 'back_color' instead of 'fill_colour' and 'black_colur'
img = qr.make_image(fill_color="red", back_color="yellow")

# Save the image
img.save("Athulya_LinkedIn.png")
