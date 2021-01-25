import cv2 as cv
import numpy as np
import time
import serial
import math

from win32 import win32gui
import win32ui
import win32con

serialcomm = serial.Serial('COM3', 9600)
serialcomm.timeout = 1

print('Virgin powers activate...')
time.sleep(5)
global tHealth;
tHealth = 10;
#-------------------------------------------find contours function
def getContours(img, imgContour):
    #find contours
    #creates a list of found contours
    contours, hierarchy = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #draw contours
    #(src,contour list,index of contours, clr, thinkness)
    cv.drawContours(imgContour, contours, -1, (0,0,255), 1)
    health = len(contours)/2.9
    global tHealth;
    z = 0;
    #print(health)
    if health < tHealth:
        print('ZAP') #used for debugging
        tHealth = tHealth - (tHealth - health)
        z = 1;
    elif health > tHealth:
        print('Healing') #used for debugging
        tHealth = tHealth + (health - tHealth)
        z = 0;
#-------------------------send over health data
    d = str(z) #health
    serialcomm.write(d.encode())
    
#----------------------------function to capture screenshots
def window_cap():
    #width and height of screen
    w = 200 #set to monitor width and height to capture entire screen
    h = 50  #dont reccomend this as red flowers will be capture and cause pain

    #below captures a screenshot directly from windows
    hwnd = None
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0), (w, h) , dcObj, (480,630), win32con.SRCCOPY)

    #good to test but we dont actually want to save the screenshot
    #dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')

    #performce enhancing string
    #np library can process strings faster than tuples so its converted here
    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (h, w, 4)
    
    #Free Resources. POWER
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    return img

#--------------------------------------------------loop screenshot function
#essentially creating a video
while(True):
    #win32 grabs a screenshot
    screenshot = window_cap()

    #hsv offers stronger contrast
    hsv = cv.cvtColor(screenshot, cv.COLOR_RGB2HSV)
    
    #best vaules for red hearts
    tLow = np.array([119,180,0])
    tUp = np.array([123,255,255])
    mask = cv.inRange(hsv,tLow,tUp)
    output = cv.bitwise_and(screenshot,screenshot,mask=mask)

    #canny and threshold
    thresh = cv.Canny(mask, 0, 255)

    imgContour = screenshot.copy()

    getContours(thresh, imgContour)

    #cv.imshow('contour', imgContour)
    
    #show the raw video
    cv.imshow('mined it', screenshot)
    #hsv
    #cv.imshow('hsv', hsv)
    #mask
    #cv.imshow('mask', mask)
    #output
    #cv.imshow('output', output)
    #threshhold
    #cv.imshow('thresh', thresh)

    if cv.waitKey(1) == ord('q'):
        #serialcomm.close()
        cv.destroyAllWindows()
        break

print('Powering down...');

    
