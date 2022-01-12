import os
import sys
from PIL import Image
from tqdm import tqdm

#StarObit just need keep the brighter point of the 2 pic
def merge_pic(data1,data2,size_tuple):
    for x in range(size_tuple[0]):
        for y in range(size_tuple[1]):
            if sum(data1[x,y])<sum(data2[x,y]):
                data1[x,y]=data2[x,y] 


def main():
    if not os.path.exists('pic'):
        print('No pic/ folder. Pls place photos under pic/ folder.')
        return

    pic_list=[i for i in os.listdir('pic') if os.path.isfile(os.path.join('pic',i)) and i[0]!='.']
    #pic_list.sort() 

    if pic_list:
        print(pic_list)

        im=Image.open(os.path.join('pic',pic_list[0]))
        print(im.format,im.size,im.mode)

        merged=im.load()
        for pic in tqdm(pic_list[1:]):
            im2=Image.open(os.path.join('pic',pic))
            data2=im2.load()
            merge_pic(merged,data2,im.size)
        im.save('merged.png')
        print('finished.')
        im.show()
    else:
        print('no pic under pic folder.')

if __name__ == '__main__':
    main()
