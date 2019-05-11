from pyzbar import pyzbar
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to input image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])

barcodes=pyzbar.decode(image)

if(barcodes < 1)
   print("Its a normal image")

else
   print("Its a Barcode Image") 
