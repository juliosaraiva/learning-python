from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.png')

filtered_img = img.convert('L')
box = (150, 100, 1500, 950)
region = filtered_img.crop(box)
print(img.quantize)
region.save("./pokedex/grey.png", "png")
