from PIL import Image

img1= Image.open("images/worlds/origins/Chest01.png").convert("RGBA").resize((300,300))
img2= Image.open("images/claws.png").convert("RGBA").resize((300,300))

finImage = Image.alpha_composite(img1, img2)

finImage.show()