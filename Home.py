import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input
import numpy as np

# def app():
#     st.title('Detect Lung Cancer from CT Scan Images in Minutes 🩺')
#     st.markdown('Discover the easy, fast, and accurate way to diagnose lung cancer using our AI-powered app. 🚀')
#     st.markdown('Lung cancer is one of the most common and deadly types of cancer in the world. Early detection and diagnosis can improve the survival rate and quality of life of patients. 🙏')

#     # st.markdown('Join our community and let's create a world without limits. 💫')
#     st.button('Start Your Free Trial Now 👇')
#     st.markdown('Or upload an image and click on "Generate Prediction" to see the results. 🔥')
#     # Lung Cancer Prediction section
#     uploaded_file = st.file_uploader("Upload a CT scan image", type=["jpg", "jpeg", "png"])

#     if uploaded_file is not None:
        
#         # Load the model outside of the run method
#         model = tf.keras.models.load_model("my_model2.hdf5", compile=False)
#         # Mapping class indices to labels
#         classes = [
#         "Adenocarcinoma Chest Lung Cancer",
#         "Large cell carcinoma Lung Cancer",
#         "NO Lung Cancer/ NORMAL",
#         "Squamous cell carcinoma Lung Cancer"
#         ]      # Define the classes variable here

#         img = Image.open(uploaded_file)
#         st.image(img, caption='Uploaded Image', use_column_width=True)

#         # Preprocess the uploaded image
#         img = img.resize((224, 224)).convert('RGB')
#         img_array = np.array(img)
#         img_array = np.expand_dims(img_array, axis=0)
#         img_array = preprocess_input(img_array)

#         # Generate prediction
#         if st.button("Generate Prediction"):
#             prediction = model.predict(img_array)
#             predicted_class = np.argmax(prediction)
#             st.write(f"Prediction: {classes[predicted_class]}")

















def app():
    # Create the first set of columns with spacing
    col1, col2 = st.columns([1, 5])
    st.write("")  # Add vertical space between logo/title and other content

    # Display the logo image in the first column
    logo_path = 'lung.png'  # Replace with your logo path
    col1.image(logo_path, use_column_width=True, width=100)

    # Set the title and text in the second column
    with col2:
        st.title("Detect Lung Cancer from CT Scan Images in Minutes 🩺")
    col3, col4 = st.columns([1, 1])
    with col3:
        st.markdown("- Discover the easy, fast, and accurate way to diagnose lung cancer using our AI-powered app. 🚀")
        st.markdown("- Many people with lung cancer live long and fulfilling lives.")
        st.markdown("- Breath by breath, step by step, we stand united against lung cancer. ")
        st.markdown("- join our community and let's create a world without limits.💫")
        st.button('Generate Prediction 🚀') 
                 
   
    st.write("")  # Add vertical space below the text

    # Display the image in the third column
    image_path = 'pic.png'  # Replace with your image path
    col4.image(image_path, use_column_width=False, width=200)

   
   

