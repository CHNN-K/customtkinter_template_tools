import cv2
import numpy as np
import json
import os

from lib.utils import Path, FindCentroidSetting, ApplicationConfiguration

class FindCentroid:
    @staticmethod
    def findCentroid(image, roi = None, debug : bool = False):
        img = image
        showImage = img.copy()
        detectedList = []

        try:
            if roi == None:
                h, w = image.shape[0], image.shape[1]
                roi = (0, 0, w, h)
            
            elif roi == -1:
                cv2.namedWindow("ROI", cv2.WINDOW_NORMAL)
                cv2.resizeWindow("ROI", 1200,900)
                roi = cv2.selectROI("ROI", img)
                img = img[int(roi[1]):int(roi[1] + roi[3]), 
                        int(roi[0]):int(roi[0] + roi[2])] 
                cv2.destroyAllWindows()
        except:
            print("No input image")
            return None, None

        threshold = FindCentroid().json_read_setting()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if debug:
            cv2.namedWindow('Shape Detection', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Shape Detection', 1200, 900)
            cv2.imshow("Shape Detection", thresh)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        # Loop over each contour and detect the shape
        for contour in contours:
            shape = FindCentroid().detect_shape(contour)
            
            # Get contour center for labeling
            M = cv2.moments(contour)
            if M["m00"] > 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                detectedList.append([shape, (cX + roi[0], cY + roi[1])])
                cv2.circle(showImage, (cX + roi[0], cY + roi[1]), 3, (0,0,255), -1)
                cv2.putText(showImage, f"{cX + roi[0], cY + roi[1]}", (cX + roi[0], cY + roi[1] - 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2 , (255,0,0), 2)

        detectedList = sorted(detectedList, key = lambda x: x[1][0])

        if debug:
            for i in detectedList:
                print(i)
                
            cv2.namedWindow('Shape Detection', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Shape Detection', 1200, 900)
            cv2.imshow("Shape Detection", showImage)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        return showImage, detectedList
    
    @staticmethod
    def detect_shape(contour):
        # Approximate the contour to reduce the number of points
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.04 * peri, True)
        
        # Determine the shape based on the number of points in the approximated contour
        if len(approx) == 3:
            return "Triangle"
        elif len(approx) == 4:
            return "Rectangle"
            # Further check if it's a square or rectangle
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = w / float(h)
            if 0.95 <= aspect_ratio <= 1.05:
                return "Square"
            else:
                return "Rectangle"
        elif len(approx) > 4:
            return "Circle"
        return "Unknown"
    
    @staticmethod
    def json_read_setting():
        if not os.path.isfile(Path().json_setting_find_centriod):
            ApplicationConfiguration().createFindCentroidSetting()
        
        with open(Path().json_setting_find_centriod, 'r') as file:
            json_data = json.load(file)
        threshold = json_data[FindCentroidSetting.threshold.name]
        return threshold