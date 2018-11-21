# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 23:47:38 2018

@author: rostik vasylyk
"""
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

f=misc.imread('new2.jpg')
 
plt.imshow(f)
plt.show()

#create row of images
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(15,5))

#zip take several lists and combine it
for c, ax in zip(range(3), axs):
    tmp_im = np.zeros(f.shape, dtype="uint8")
    tmp_im[:,:,c] = f[:,:,c]
    ax.imshow(tmp_im)
    ax.set_axis_off()
plt.show()    
    
f = np.average(f,weights = [0.2989, 0.5870, 0.1140],axis =2)

'''def to_grayscale(im, weights = np.c_[0.2989, 0.5870, 0.1140]):
    tile = np.tile(weights, (im.shape[0],im.shape[1],1))
    #np.tile(a, (2, 2))
    #array([[0, 1, 2, 0, 1, 2],
    #      [0, 1, 2, 0, 1, 2]])
    return np.sum(tile * im, axis=2)'''

#f = to_grayscale(f)
    
plt.imshow(f, cmap=plt.cm.gray,vmin=10, vmax=100)
plt.show()