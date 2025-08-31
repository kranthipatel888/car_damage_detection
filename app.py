import streamlit as st
from model_helper import predict

st.title("Vechile Damage Detection")

uploaded_file = st.file_uploader("upload the Image",type=['jpg','png'])

if uploaded_file:
    img_path='Image.jpg'
    with open(img_path,'wb') as f:
        f.write(uploaded_file.getbuffer())
        st.image(uploaded_file, caption='uploaded Image',use_container_width=True)
        prediction=predict(img_path)
        st.info(f"{prediction}")