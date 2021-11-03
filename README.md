# FastAPI-Streamlit-based-YoloV5-detector
Playing around with FastAPI and streamlit to create a YoloV5 object detector

It turns out that a User Interface improves the user satisfaction when they utilize deep learning models for experiments. This project of mine aims to do just that.
Even though a FastAPI, Streamlit based web app isn't a unique idea, I have however put my own twist by adding a section that accepts videos for bounding box annotation as well as images.

The Streamlit based UI will consist of two sections- A video section and an image section. After uploading, the user will get back the bounding annotation of the video/image and additionally the video/image will also be saved in the root/ folder from where the .py files are run.

The below steps are required to run the application-

# Step 1-

First Clone the repo and make note of the root/ directory where the repo is saved. This directory will also store the resulting image/video that is saved by the YoloV5 model.

# Step 2-

We need to change the root directory to what you are currently using. In the repository the directory in which the repo is saved is "C:/Users/BHASKAR BOSE", we need to change this.
If you are using windows then open a terminal and write-
'''
powershell -Command "(gc myFile.txt) -replace 'foo', 'bar' | Out-File -encoding ASCII myFile.txt"

'''

