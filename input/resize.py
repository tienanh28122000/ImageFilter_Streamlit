from PIL import Image

filename="lake.png"
im = Image.open(filename)
im.thumbnail((500, 500))
im.save(filename)