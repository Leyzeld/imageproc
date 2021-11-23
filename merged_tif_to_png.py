import glob
import numpy as np
import rasterio
from rasterio.merge import merge
import os
import matplotlib.image as mplimg
import skimage.io


def merge_tif(path,ftype,outfile, resfolder):
    alltif=glob.glob(os.path.join(path,'*.%s'%ftype))
    bigtif=[]
    for tif in alltif:
        src=rasterio.open(tif)
        bigtif.append(src)
        print(tif)
    mosaic, out_trans = merge(bigtif)
    outmeta=src.meta.copy()
    outmeta.update({'driver':'GTiff','height':mosaic.shape[1],'width':mosaic.shape[2],'transform':out_trans})
    os.makedirs(path+'\\merged')
    outpath=path+'\\merged\%s.tif'%outfile
    with rasterio.open(outpath,'w',**outmeta) as dest:
        dest.write(mosaic)


def to_png(foldername,colourmap, resfolder):
    files = []
    for file in sorted(os.listdir(foldername)):
        files.append(file)

    if not os.path.exists(resfolder +'RES'):
        os.makedirs(resfolder +'RES')

    _min=1E8
    _max=-1E6
    filemax=''
    filemin=''
    for filenow in files:
        img = skimage.io.imread(foldername+filenow, plugin='tifffile')
        img_arr = np.array(img)
        if np.max(img_arr)>_max:
            _max=np.max(img_arr)
            filemax=filenow
        if np.min(img_arr)<_min:
            _min=np.min(img_arr)
            filemin=filenow
    for filenow in files:
        print('PROCESSING '+filenow+' right now')
        img = skimage.io.imread(foldername+filenow, plugin='tifffile')
        img_arr = np.array(img)
        mplimg.imsave(resfolder+'RES/'+filenow+'.png',img_arr,cmap=colourmap,vmin=_min,vmax=_max)


path=r'./tiffiles/'
resfolder = r'./'
outfile='res_tif'
ftype='tif'
colourmap = 'coolwarm' # https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
merge_tif(path,ftype,outfile)
to_png(path, colourmap,resfolder)
