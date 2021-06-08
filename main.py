# python3 -m venv venv
# . venv/bin/activate
# pip install streamlit
# pip install torch torchvision
# streamlit run main.py
import streamlit as st
from PIL import Image
from filter import HongAnh
from transform import Transform
from brightness import Brightness
from saturated import Saturated

import style

st.title('Image Filtering')

img = st.sidebar.selectbox(
    'Select Image',
    ('city.png', 'lake.png', 'LongBien.png', 'river.jpg')
)

# style_name = st.sidebar.selectbox(
#     'Select Style',
#     ('candy', 'mosaic', 'rain_princess', 'udnie')
# )

filter_name = st.sidebar.selectbox(
    'Select Filter',
    ('sepia', 'greyscale', 'invert', 'electric', 'high_contrast', 'darkened', 'censored', 'vintage', 'brightness', 'saturated')
)

# model= "saved_models/" + style_name + ".pth"
input_image = "input/" + img
output_image = "output/output.png"

st.write('### Source image:')
image = Image.open(input_image)
if image.mode != 'RGB':
    image = image.convert('RGB')
    image.save(input_image)
st.image(image, width=400) # image: numpy array

clicked_filter = st.button('Stylize')

if clicked_filter:
    if filter_name == 'sepia':
        # model = style.load_model(model)
        # style.stylize(model, input_image, output_image)
        HongAnh(f=img, filter='Sepia')
        st.write('### Output image:')
        image = Image.open(output_image)
        st.image(image, width=400)
    elif filter_name ==  'greyscale':
        # model = style.load_model(model)
        # style.stylize(model, input_image, output_image)
        HongAnh(f=img, filter='GreyScale')
        st.write('### Output image:')
        image = Image.open(output_image)
        st.image(image, width=400)
    elif filter_name ==  'invert':
        # model = style.load_model(model)
        # style.stylize(model, input_image, output_image)
        HongAnh(f=img, filter='Invert')
        st.write('### Output image:')
        image = Image.open(output_image)
        st.image(image, width=400)
    elif filter_name ==  'electric':
        # model = style.load_model(model)
        # style.stylize(model, input_image, output_image)
        if input_image.lower().endswith(('.jpg')):
            im=Image.open(input_image)
            im.save('input/input.png')
            img='input.png'
        Transform(f=img, filter='Electric')
        st.write('### Output image:')
        image = Image.open(output_image)
        st.image(image, width=400)
    elif filter_name ==  'high_contrast':
        # model = style.load_model(model)
        # style.stylize(model, input_image, output_image)
        if input_image.lower().endswith(('.jpg')):
            im=Image.open(input_image)
            im.save('input/input.png')
            img='input.png'
        Transform(f=img, filter='HighContrast')
        st.write('### Output image:')
        image = Image.open(output_image)
        st.image(image, width=400)
    elif filter_name == 'darkened':
        # model = style.load_model(model)
        # style.stylize(model, input_image, output_image)
        if input_image.lower().endswith(('.jpg')):
            im=Image.open(input_image)
            im.save('input/input.png')
            img='input.png'
        Transform(f=img, filter='Darkened')
        st.write('### Output image:')
        image = Image.open(output_image)
        st.image(image, width=400)
    elif filter_name ==  'censored':
        # model = style.load_model(model)
        # style.stylize(model, input_image, output_image)
        if input_image.lower().endswith(('.jpg')):
            im=Image.open(input_image)
            im.save('input/input.png')
            img='input.png'
        Transform(f=img, filter='Censored')
        st.write('### Output image:')
        image = Image.open(output_image)
        st.image(image, width=400)
    elif filter_name ==  'vintage':
        # model = style.load_model(model)
        # style.stylize(model, input_image, output_image)
        if input_image.lower().endswith(('.jpg')):
            im=Image.open(input_image)
            im.save('input/input.png')
            img='input.png'
        Transform(f=img, filter='Vintage')
        st.write('### Output image:')
        image = Image.open(output_image)
        st.image(image, width=400)
    elif filter_name ==  'brightness':
        # model = style.load_model(model)
        # style.stylize(model, input_image, output_image)
        Brightness(f=img)
        st.write('### Output image:')
        image = Image.open(output_image)
        st.image(image, width=400)
    elif filter_name ==  'saturated':
        # model = style.load_model(model)
        # style.stylize(model, input_image, output_image)
        Saturated(f=img)
        st.write('### Output image:')
        image = Image.open(output_image)
        st.image(image, width=400)