# Import PIL (Note: the package name is Pillow, yet we import from PIL).
# Yes, the import here is confusing. More context here: https://pypi.org/project/Pillow/
from PIL import Image

# Import pytesseract (a Python wrapper for Tesseract)
# Note: You will need to have Tesseract installed on your machine for pytesseract to work.
import pytesseract

# Extract text from the image
extracted_text = pytesseract.image_to_string('receipt.jpeg')

# Write the extracted text to a file
with open('extracted_text.txt', 'w') as f:
    f.write(extracted_text)
