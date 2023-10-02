# pip install pyqrcode

import pyqrcode
# import png

def qrcode() :
    
    q = pyqrcode.create(input("Enter the text of which youy want to generate qr:"))
    q.png('qrcode.jpg', scale = 6)
    print("QR successfully generated")
    
if __name__ == '__main__' :
    qrcode()
    