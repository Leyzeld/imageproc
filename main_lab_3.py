import cv2 as cv
import numpy as np
import glob
from matplotlib import pyplot as plt 

def Spectrum(shift):
    f_sh = np.abs(shift)
    min_val = np.amin(f_sh)
    f_sh[f_sh == 0] = min_val
    spectrum = 40*np.log10(f_sh)
    return spectrum, min_val

def DFFTnp(pic, f_name):
    f = np.fft.fft2(pic)
    f_shift = np.fft.fftshift(f)
    magnitude_spectrum, _min = Spectrum(f_shift)

    pic_min = pic.min();

    for a in f_shift[0:337]: a[508:520] = _min
    for a in f_shift[345:]: a[508:520] = _min
    for a in f_shift[335:345]: a[0:508] = _min
    for a in f_shift[335:345]: a[515:] = _min

    res, empty = Spectrum(f_shift)

    plt.subplot(141),plt.imshow(magnitude_spectrum, cmap = 'gray', vmin = 0, vmax = 255)
    plt.title('magnitude_spectrum '), plt.xticks([]), plt.yticks([])
    plt.subplot(142),plt.imshow(res, cmap = 'gray', vmin=0, vmax=255)

    res = np.real(np.fft.ifft2(np.fft.ifftshift(f_shift)))
    plt.subplot(143),plt.imshow(pic, cmap = 'gray', vmin = 0, vmax = 255)
    plt.title('In pic '+ f_name), plt.xticks([]), plt.yticks([])

    plt.subplot(144),plt.imshow(res, cmap = 'gray', vmin=0, vmax=255)
    plt.title(' Res '), plt.xticks([]), plt.yticks([])

    plt.show()

folder_path = r'./'
images = glob.glob(folder_path + '*.png')

def main():
    for f_name in images:
        pic = np.float32(cv.imread(f_name,0))
        DFFTnp(pic, f_name)

if __name__ == '__main__':
    main()
