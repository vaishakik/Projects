#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 05:01:03 2018

@author: shocked
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
import glob
import matplotlib as p
from PIL import Image


def rot_matrix(theta):
    ct, st = np.cos(theta), np.sin(theta)
    return np.array([[ct, -st],[st, ct]])

data_path='/home/mahima/Desktop/text detect/MSRA-TD500/'
test=False

data_path = data_path
if test:
    gt_path = os.path.join(data_path, 'test')
else:
    gt_path = os.path.join(data_path, 'train')

image_path = image_path = gt_path
classes = ['Background', 'Text']

image_names = []
data = []
text = []
for image_file_name in sorted(glob.glob(image_path+'/*.JPG')):
    image_name = os.path.split(image_file_name)[1]
    #fig,ax = plt.subplots(1)
    im1 = Image.open(image_file_name)
    
    w1, h1 = im1.size
    fig, ax = plt.subplots(figsize=(w1/100,h1/100))
    
    print(w1,h1)
    im2=Image.new('RGB',(w1,h1),(0,0,0))
    gt_file_name = os.path.splitext(image_name)[0] + '.gt'
    with open(os.path.join(gt_path, gt_file_name), 'r') as f:
        for line in f:
            line_split = line.strip().split(' ')
            # line_split = [index, difficult, x, y, w, h, theta]
            
            # skip difficult boxes
            if int(line_split[1]) == 1:
                #continue
                pass
            
            cx, cy, w, h, theta = [float(v) for v in line_split[2:]]
            print(cx, cy, w, h, theta)
        # Display the image
            f=ax.imshow(im2)
            #f=plt.imshow(im2)
            rect = patches.Rectangle((cx, cy), w, h, (theta),linewidth=1,edgecolor='w',facecolor='white')
            t = p.transforms.Affine2D().rotate_around(cx,cy,
                theta)

            rect.set_transform(t + plt.gca().transData)

            plt.gca().add_patch(rect)
            #ax.add_patch(rect)
            #w2,h2=f.size;
            #print(w2,h2)
            ax.axes.get_xaxis().set_visible(False)
            ax.axes.get_yaxis().set_visible(False)
            ax.set_frame_on(False)
            plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
        hspace = 0, wspace = 0)
    #fig.savefig('/home/mahima/Desktop/text detect/trainm/'+ os.path.splitext(image_name)[0] + '.png')
    
    ax.set_axis_off()
    plt.axis('off')
    plt.savefig('/home/mahima/Desktop/text detect/trainm/'+ os.path.splitext(image_name)[0] + '.png',bbox_inches='tight',pad_inches=-0.2)
    #plt.show()
    #im = Image.fromarray(np.uint8(f))
    #im.save('/home/mahima/Desktop//text detect/trainm/'+ os.path.splitext(image_name)[0] + '.png', "PNG")
