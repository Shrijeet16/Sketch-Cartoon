import cv2
import numpy as np

print(cv2.__version__)

width, heigth = 3, 4
capture = cv2.VideoCapture(0)
capture.set(width, 360)
capture.set(heigth, 480)


def cameracalib():
    for i in range(4):
        ret1, frame1 = capture.read()

cameracalib()

def wait():
    pass


def bilateralfilter(image):
    # gaussianblur = cv2.GaussianBlur(image,(5,5) ,1 , 1)
    #image = cv2.medianBlur(image , (5))
    bilateralblur = cv2.bilateralFilter(image, 15, 75, 75)
    # cv2.imshow('gaussina' , gaussianblur)
    # cv2.imshow('bila' , bilateralblur)
    return bilateralblur


def edgedetection(img):
    laplacian = cv2.Laplacian(img, cv2.CV_8U)
    # sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    # sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
    # sobel = cv2.add(sobelx , sobely)
    # canny = cv2.Canny(img,75 , 200)
    # cv2.imshow('lap'  ,laplacian)
    # cv2.imshow('sobel' , sobel)
    # cv2.imshow('canny', canny)
    return laplacian

def thresholding(img):
    ret ,img = cv2.threshold(img ,16,255 ,cv2.THRESH_BINARY_INV)
    return img

frame = cv2.imread('C:\Users\Sinal\Documents\opencv_proj\lena.tif')

#frame = np.uint8(frame)
frame = cv2.cvtColor(frame ,cv2.COLOR_BGR2GRAY)
#frame = cv2.medianBlur(frame , 1)
frame = edgedetection(frame)
frame = np.uint8(frame)
frame = thresholding(frame)

#frame = bilateralfilter(frame)

cv2.imshow('sketch', frame)

#frame = blur(frame)
frame = cv2.cvtColor(frame ,cv2.COLOR_GRAY2BGR)
cv2.waitKey(0)
capture.release()
cv2.destroyAllWindows()


'''while (1):
    ret, frame = capture.read()
    # the error which is coming can be removed with the help of condition in which we have to check the return variable
    

    #wait()
'''