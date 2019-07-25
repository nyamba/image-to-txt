from flask import Flask, request
import pytesseract
try:
    from PIL import Image
except ImportError:
    import Image


app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def parse_image():
	img = Image.open(request.files['data'].stream)
	pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
	return pytesseract.image_to_string(img, lang='mon', config='--psm 6')