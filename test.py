from PIL import Image

img1= Image.open("images/empty.png").convert("RGBA")
img2= Image.open("images/claws.png").convert("RGBA")

finImage = Image.alpha_composite(img1, img2)

finImage.show()