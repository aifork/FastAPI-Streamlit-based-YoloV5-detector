import os
import shutil
import glob

def delete_video_files():
    file=glob.glob('C:/Users/BHASKAR BOSE/frame_split/*')
    for f in file:
        os.remove(f)
        
    shutil.rmtree('C:/Users/BHASKAR BOSE/runs/detect/exp')
    file=glob.glob('C:/Users/BHASKAR BOSE/runs/detect/*')
    for f in file:
        os.remove(f)
    
def delete_image_files():
    
    shutil.rmtree('C:/Users/BHASKAR BOSE/runs/detect/exp')
    #file=glob.glob('C:/Users/BHASKAR BOSE/runs/detect/*')
    #for f in file:
        #os.remove(f)
    
#delete_video_files()
