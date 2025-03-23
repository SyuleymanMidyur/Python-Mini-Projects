import pyqrcode

link = input("Enter the link: ")
url = pyqrcode.create(link)
url.png('youtube.png', scale=8)
