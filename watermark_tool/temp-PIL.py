import os
from PIL import Image

watermark  = "logo.png"
mark = Image.open(watermark)

def paster_and_saver(filename) :
	im   = Image.open(filename)
	im_width, im_height = im.size
	
	X_OFFSET_1 =    im_width//20
	X_OFFSET_2 =  2*im_width//5
	X_OFFSET_3 = 13*im_width//19
	Y_OFFSET_1 = 11*im_height//50
	Y_OFFSET_2 =  7*im_height//10

	required_size = (im_width//4,im_height//15)
	mark = Image.open(watermark)
	mark = mark.resize(required_size)

	im.paste(mark, (X_OFFSET_1,Y_OFFSET_1), mask = mark)
	im.paste(mark, (X_OFFSET_2,Y_OFFSET_1), mask = mark)
	im.paste(mark, (X_OFFSET_3,Y_OFFSET_1), mask = mark)
	im.paste(mark, (X_OFFSET_1,Y_OFFSET_2), mask = mark)
	im.paste(mark, (X_OFFSET_2,Y_OFFSET_2), mask = mark)
	im.paste(mark, (X_OFFSET_3,Y_OFFSET_2), mask = mark)

	im.save("./watermarked_images/img"+str(1)+".jpg")

for file in os.listdir("."):
   	filename = os.fsdecode(file)
   	if filename.endswith(".jpg"): 
   		paster_and_saver(filename)
   	else:
   		continue


