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
```
powershell -Command "(gc myapp.py) -replace 'C:/Users/BHASKAR BOSE', 'root/' | Out-File -encoding ASCII myapp.py"

```
Do the same for stream.py and delete_files.py
# Step 3-

Great! now you have to install all the required libraries, so write-
```
pip install -r requirements.txt
```
# Step 4-

There is one more step we need to do before running our application. Open Jupyter notebook (or any IDE) and write-
```
import delete_files
delete_files.delete_video_files()
```
This will remove all the unnecessary files before starting.
# Step 5-

Now that all the libraries are installed we can now begin to run the application. First we run the following command-

```
uvicorn myapp:app --reload
```
following which we run-
```
streamlit run "root/stream.py"
```

We see that a drop down is provided where we can select either image or video. Select one and upload the image video.

You will soon see the annotated image/video on the screen. Additionally the image/video will also be saved in your root/ directory.

