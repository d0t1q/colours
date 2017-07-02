#! /usr/bin/python
from PIL import Image
import random
import imageio as io
import os

#how to random
random.seed()

def static_gen(file_name):

    colour_def=[(255, 0, 0,),(255, 128, 0),(255, 255, 0),(128, 255, 0),(0, 255, 0),(0, 255, 128),(0, 255, 255),(0, 128,255),(0, 0, 255),(127, 0, 255)]
    #create new image
    file_number=0

    for i in range (0,450):
        file_path = "./static/"+str(file_number)+file_name
        print file_path
        img = Image.new('RGB',(512,512), "black")
        pixels = img.load()
        random.seed()
        #colour all pixels a random colour
        for i in range(img.size[0]):
            for j in range(img.size[0]):
                colour = colour_def[random.randint(0,9)]
                pixels[i,j] = colour
        img.save(file_path)
        file_number+=1
    file_names = sorted((fn for fn in os.listdir('./static/') if fn.endswith(file_name)))
    with io.get_writer('static.gif', mode='I', duration=0.1) as writer:
        for filename in file_names:
            filname="./static/"+filename
            image = io.imread(filename)
            writer.append_data(image)
    writer.close()

def main():
    file_name = raw_input("Name the file(needs .png): ")
    if "png" in file_name:
        static_gen(file_name)
    else:
        print "include png in filename"
        main()

if __name__=='__main__':
        main()
        sys.exit()
