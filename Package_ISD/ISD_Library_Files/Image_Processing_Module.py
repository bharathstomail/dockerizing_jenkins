
#@author: Bharath HS

from PIL import Image
from io import BytesIO
import os
import datetime
import sys
import time
from PIL import Image, ImageChops
from scipy.misc import imread
from scipy.linalg import norm
from scipy import sum, average
import traceback
import sys

class Image_Processing():
    
    #def __init__(self):
    
    # Below function would take a screenshot for the element(image viewer) identified

    def Convert_Image_to_String(self,image_path):
        import base64
        
        #image_path = 'C:/Git_Repository/Project_ISD/Package_ISD/Element_Screenshots/Test.png'
        with open(image_path, "rb") as imageFile:
            image_str = base64.b64encode(imageFile.read())
        
        time.sleep(1)
        Image_Slice = str(str(image_str).split("b'")[1])
        Image_encrypt = str(Image_Slice).replace("'","")
        
        return Image_encrypt
    
    def Get_Screenshot_Ele(self,driver_arg,element_arg,Package_path):
        try: 
            #find part of the page you want image of
            location = element_arg.location
            size = element_arg.size
            png = driver_arg.get_screenshot_as_png() # saves screenshot of entire page
            
            im = Image.open(BytesIO(png)) # uses PIL library to open image in memory
            
            left = location['x']
            top = location['y']
            right = location['x'] + size['width']
            bottom = location['y'] + size['height']
            
            im = im.crop((left, top, right, bottom)) # defines crop points
            
            #Pckg_Path = os.path.abspath(os.pardir) # Path of the Package folder
            now = datetime.datetime.now()
            time_stamp = str(now.strftime('%Y-%m-%dT%H:%M:%S') + ('-%02d' % (now.microsecond / 10000)))
            print(time_stamp.replace(":","_").replace("-","_").replace(" ","_"))
            
            time_stamp_new = time_stamp.replace(":","_").replace("-","_").replace(" ","_")  #timestamp with delimenters replaced with '_'
             
            file_name = 'screenshot_'+time_stamp_new
            image_path = Package_path+'/Element_Screenshots/'+file_name+'.png'
            im.save(image_path) # saves new cropped image
            return image_path
        except Exception:
            print("Screenshot was not captured")
            print(str(traceback.format_exc() + "--- "+ str(sys.exc_info()[0])))
            
#--------------Below functions would compare the images w.r.t pixels -------------------------------    
    def normalize(self,arr):
        try:
            rng = arr.max()-arr.min()
            amin = arr.min()
            return (arr-amin)*255/rng
        except Exception:
            print(ValueError)

    def to_grayscale(self,arr):
        "If arr is a color image (3D array), convert it to grayscale (2D array)."
        if len(arr.shape) == 3:
            return average(arr, -1)  # average over the last axis (color channels)
        else:
            return arr

    def compare_images(self,img1, img2):
        # normalize to compensate for exposure difference, this may be unnecessary
        # consider disabling it
        try:
            img1 = self.normalize(img1)
            img2 = self.normalize(img2)
            # calculate the difference and its norms
            diff = img1 - img2  # elementwise for scipy arrays
            m_norm = sum(abs(diff))  # m norm
            z_norm = norm(diff.ravel(), 0)  # Zero norm
            return (m_norm, z_norm)
        except:
            return None


    def Final_Image_Comparison(self,img1_arg,img2_arg): 
        try:
            
            #file1, file2 = sys.argv[1:1+2]
                # read images as 2D arrays (convert to grayscale for simplicity)
            img1 = self.to_grayscale(imread(img1_arg).astype(float))
            img2 = self.to_grayscale(imread(img2_arg).astype(float))
            # compare
            n_m, n_0 = self.compare_images(img1, img2)
            if n_m is not None:
                print(n_m)
                print("M_norm:", n_m, "/ per pixel:", n_m/img1.size)
                print("Z_norm:", n_0, "/ per pixel:", n_0*1.0/img1.size)
                print("M_norm:", n_m, "/ per pixel:", n_m/img2.size)
                print("Z_norm:", n_0, "/ per pixel:", n_0*1.0/img2.size)  
                return n_m      
            else:
                return None
        except:
            print(Exception)
            return None
            #self.Report_Instance.Report_Log("Image Validation","Should be able to validate the images","Encountered with an exception - "+str(traceback.format_exc() + "--- "+ str(sys.exc_info()[0])),"FAILED")
       

# -------------Below functions would greyout the background of the images and highlight the differences of 2 images -------------------

    # need to rework on the arguments and how to save the images without using timestamps. 
    def black_or_b(self,a, b):
        diff = ImageChops.difference(a,b)
        diff = diff.convert('L')
        # diff = diff.point(point_table)
        #h,w=diff.size
        new = diff.convert('RGB')
        new.paste(b, mask=diff)
        return new
    
    # Below code will highlight the mismatch (Mismatch could be the annotations/lesions)
    def Image_Comparison_Stage_1(self,img1_arg,img2_arg,Package_path):
        #Pckg_Path = os.path.abspath(os.pardir) # Path of the Package folder
        now = datetime.datetime.now()
        time_stamp = str(now.strftime('%Y-%m-%dT%H:%M:%S') + ('-%02d' % (now.microsecond / 10000)))
        print(time_stamp.replace(":","_").replace("-","_").replace(" ","_"))
        
        time_stamp_new = time_stamp.replace(":","_").replace("-","_").replace(" ","_")  #timestamp with delimenters replaced with '_'
         
        file_name = 'diff_'+time_stamp_new
        image_path = Package_path+'/Element_Screenshots/'+file_name+'.png'
        print("Image_Comparison_Stage_1 ",image_path)
        a = Image.open(img1_arg)
        b = Image.open(img2_arg)
        c = self.black_or_b(a, b)
        c.save(image_path)
        return image_path