import qrcode

#get text or url from user
data=input("Enter the text or url : ").strip()

#get file name
filename=input('enter file name: ').strip()

#setting and generating qr code
qr=qrcode.QRCode(box_size=10,border=4)
qr.add_data(data)
image=qr.make_image(fill_color="black",back_color="white")

#saving the qr code in the user named file
image.save(filename)
print(f"QR Code saved in {filename}")