from rembg import remove
from PIL import Image
input = 'Ella.jpg'
output = 'Ella.png'
inp = Image.open(input)
out = remove(inp)
out.save(output)
Image.open('Ella.png')