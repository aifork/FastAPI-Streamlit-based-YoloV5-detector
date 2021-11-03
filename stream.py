import streamlit as st
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from PIL import Image
import io
import time

def process(name, image, server_url: str):

    m = MultipartEncoder(fields={"file": (name, image, "image/jpg")})

    r = requests.post(
        server_url, data=m, headers={"Content-Type": m.content_type}, timeout=8000
    )

    return r
def main():
    page=st.sidebar.selectbox("choose a particular page",["image","video"])
    if page=="image":
        
        st.title("YoloV5 Person Detection in Images")
        
        st.write(
         """Here we get the Person Detections of the Image that you provide.
         This streamlit example uses a FastAPI service as backend.
         Visit this URL at `:8000/docs` for FastAPI documentation.
         """
        )  # description and instructions
        
        st.write("""Additionally go to root/ to find the final image containing annotations of all humans.""")
        
        input_image = st.file_uploader("insert image") 
        
        
        backend='http://127.0.0.1:8000/img/'
        #segments = process("example.jpg", input_image, backend)
        #st.write(segments.content)
        
        col1, col2 = st.columns(2)
        
        if input_image:
            segments = process("example.jpg", input_image, backend)         
            #segments = process(input_image, backend)
            original_image = Image.open(input_image).convert("RGB")
            segmented_image = Image.open(io.BytesIO(segments.content)).convert("RGB")
            col1.header("Original")
            col1.image(original_image, use_column_width=True)
            col2.header("detect")
            col2.image(segmented_image, use_column_width=True)
            
    elif page=="video":
        
        st.title("YoloV5 Person Detection in Video")
        
        st.write(
         """Here we get Person Detections of the Video that you provide. Additonally the number of persons in each frame is also mentioned.
         This streamlit example uses a FastAPI service as backend.
         Visit this URL at `:8000/docs` for FastAPI documentation.
         """
        )  # description and instructions
        
        st.write("""Additionally go to Root/ to find the final project.avi file that is the annotated video.""")
        
        input_video = st.file_uploader("insert video") 
        
        if input_video:
        
            #video1=open("10 sec cli.mp4","rb")
            #st.video(video1)
            #st.video(open(input_video,"rb"))
        
            backend='http://127.0.0.1:8000/video/'
            segments = process("10 sec cli.mp4", input_video, backend)
            
            video1=open("10 sec cli.mp4","rb")
            st.video(video1)
            
            time.sleep(5)
            video2=open("project.avi","rb")
            st.video(video2)
       
    
if __name__ =="__main__":
    main()