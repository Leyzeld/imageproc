import cv2 as cv
import numpy as np
import glob
from matplotlib import pyplot as plt 

def DFFTnp(pic, f_name):
    f = np.fft.fft2(pic)
    f_shift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(f_shift))
    pic_min = pic.min();
    if pic_min >= 0:
        plt.subplot(121),plt.imshow(pic, cmap = 'gray', vmin = 0, vmax = 255)
    else:
        plt.subplot(121),plt.imshow(pic, cmap = 'gray')
    plt.title('In pic '+ f_name), plt.xticks([]), plt.yticks([])
    s_min = magnitude_spectrum.min()
    s_max = magnitude_spectrum.max()
    if s_min == s_max:
        plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray', vmin = 0, vmax = 255)
    else:
        plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()

folder_path = r'./'
images = glob.glob(folder_path + '*.png')
for f_name in images:
    pic = np.float32(cv.imread(f_name,0))
    DFFTnp(pic, f_name)
