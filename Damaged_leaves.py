import numpy as np
import cv2 as cv
import sys

def CalcOfDamageAndNonDamage (image) :

    image_blur = cv.GaussianBlur(image, (7,7), cv.BORDER_DEFAULT)

    hsv_img = cv.cvtColor( image_blur, cv.COLOR_BGR2HSV)

    markers = np.zeros((image.shape[0], image.shape[1]) , dtype = "int32" )
    markers [ 100 : 140 , 100 : 140 ] = 255 # center
    markers [ 236 : 255 , 0 : 20 ] = 1 #upper right
    markers [ 0 : 20 , 0 : 20 ] = 1 #upper left
    markers [ 0 : 20 , 236 : 255 ] = 1 #low left
    markers [ 236 : 255 , 236 : 255 ] = 1 #low right
    leafs_area_BGR = cv.watershed(image_blur, markers)
    healthy_part = cv.inRange(hsv_img, (36,25,25), (86,255,255))
    ill_part = leafs_area_BGR - healthy_part
    mask = np.zeros_like(image, np.uint8)
    mask [leafs_area_BGR > 1] = ( 0, 255, 100)
    mask [ill_part > 1 ] = (128, 0, 255)
    cv.imshow("hsv_img", hsv_img) 

    cv.imshow("Blured", image_blur) 
    

    return mask
    
def main():
    img = cv.imread('5.jpg') 
    if img is None:
        sys.exit("Could not read the image.")
    
    cv.imshow("Orig", img) 

    resimg = CalcOfDamageAndNonDamage(img)
    cv.imshow("Res", resimg) 
    k = cv.waitKey(0) 

if __name__ == '__main__':
    main()