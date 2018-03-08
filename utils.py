import re
import base64

def convert_image(img_data):
    imgstr = re.search(b'base64,(.*)',img_data).group(1)
    with open('output.png','wb') as output:
        output.write(base64.b64decode(imgstr))
