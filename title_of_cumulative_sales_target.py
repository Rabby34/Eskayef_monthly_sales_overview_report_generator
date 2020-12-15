from PIL import Image, ImageDraw, ImageFont

img = Image.open("extra_space_mid.png")
above_title5 = ImageDraw.Draw(img)

font7 = ImageFont.truetype("bitstream-vera-sans.bold.ttf", 25, encoding="unic")

above_title5.text((400, 15), "Cumulative MTD Target VS Sales", (7,21,21), font=font7)
#above_title5.text((170, 16), "Cumulative MTD Target VS Sales", (7,24,24), font=font7)
#above_title5.text((245, 16), "Day Wise Target VS Sales", (7,24,24), font=font7)

img.save('changed_extra_space_mid.png')

print('9. text of day sale vs target plotted on extra mid space')