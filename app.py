import streamlit as st
from models import Model
from utils import load_yaml_as_dict, save_file


VARIABLES = load_yaml_as_dict('variables/variables.yaml')
MODELS = VARIABLES['MODELS']
PATHS = VARIABLES['PATHS']

model_variant = st.selectbox('Select a variant of YOLO v8', options=MODELS)
model = Model(model_variant)
select_mode = st.radio('Select mode (Webcam or video file)', ['Webcam', 'Video File'], index=1)
mode = 0 if select_mode == 'Webcam' else 1

if mode == 1:
    upload = st.file_uploader(
              'Upload a video or an image!',
              type=['mov', 'avi', 'mp4', 'mpg', 'mpeg', 'm4v', 'wmv', 'mkv'],
              disabled=(mode == 0)
          )
    if upload is not None:
        save_file(upload, PATHS['SOURCES']+upload.name)
    if st.button('Start detecting'):
        model.predict_video(
            source=PATHS['SOURCES']+upload.name,
            target=PATHS['OUTPUTS']+'detected - '+upload.name
        )

else:
    if st.button('Start detecting'):
        model.predict_web_cam()

