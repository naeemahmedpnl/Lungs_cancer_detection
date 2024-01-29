# # main.py
# import streamlit as st
# from streamlit_option_menu import option_menu
# from PIL import Image
# import tensorflow as tf
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.applications.inception_v3 import preprocess_input
# import numpy as np


# # Set the page config
# st.set_page_config(
#     page_title="Lung Cancer Detection",  # Set the page title
#     page_icon="lung.png"  # Set the page icon
# )


# # Import your modules
# import Home
# import Account
# import Test
# from AdditionalInfo import app as AdditionalInfoApp
# import Contact
# import AboutUs


# class MultiApp:
#     def __init__(self, is_logged_in=False):
#         self.apps = []
#         self.is_logged_in = is_logged_in

#     def add_app(self, title, func):
#         self.apps.append({
#             "title": title,
#             "function": func
#         })

#     def run(self):
#         if not self.is_logged_in:
#             Account.app()
#             if st.session_state.get("is_login_successful", False):
#                 self.is_logged_in = True
#             else:
#                 return

#             with st.sidebar:
#                 custom_logo_path = 'lung.png'

#                 # Display the custom logo
#                 st.image(custom_logo_path, use_column_width=True, width=20)
#                 # Create a selection box in the sidebar for choosing different pages
#                 selected_page = option_menu(
#                     menu_title='LungsVision',
#                     options=[
#                         'Account',  # Change the order of pages
#                         'Home',
#                         'Test',
#                         'Additional Info',
#                         'Contact',
#                         'About Us',
#                     ],
#                     icons=[
#                         'clock',  # Use appropriate icon for history
#                         'house-fill',
#                         'eye',
#                         'info',
#                         'phone',
#                         'info-circle-fill',
#                         # Use 'phone' icon for contact
#                     ],
#                     default_index=0,
#                     styles={
#                         "container": {"padding": "5px!important", "background-color": 'black'},
#                         "icon": {"color": "white", "font-size": "23px"},
#                         "nav-link": {"color": "white", "font-size": "16px", "text-align": "left", "margin": "0px",
#                                     "--hover-color": "blue"},
#                         "nav-link-selected": {"background-color": "#02ab21"},
#                     },
#                 )

#             if selected_page == 'Home':
#                 Home.app()
#             elif selected_page == 'Test':
#                 Test.app()
#             elif selected_page == 'Additional Info':
#                 AdditionalInfoApp(model, classes)
#             elif selected_page == 'Contact':
#                 Contact.app()
#             elif selected_page == 'About Us':
#                 AboutUs.app()

# # Load the model outside of the run method
# model = tf.keras.models.load_model("my_model2.hdf5", compile=False)
# # Mapping class indices to labels
# classes = [
#     "Large cell carcinoma Lung Cancer",
#     "Adenocarcinoma Chest Lung Cancer",
#     "Squamous cell carcinoma Lung Cancer"
#     "NO Lung Cancer/ NORMAL",
# ]

# # Create an instance of MultiApp and run it
# if __name__ == "__main__":
#     # Check if the user is logged in (you need to implement this check based on your authentication mechanism)
#     is_logged_in = False  # Change this to the actual check for login status

#     multi_app = MultiApp(is_logged_in)
# multi_app.run()








































# # # main.py
# # import streamlit as st
# # from streamlit_option_menu import option_menu
# # from PIL import Image
# # import tensorflow as tf
# # from tensorflow.keras.preprocessing import image
# # from tensorflow.keras.applications.inception_v3 import preprocess_input
# # import numpy as np

# # # Set the page config
# # st.set_page_config(
# #     page_title="Lung Cancer Detection", # Set the page title
# #     page_icon="lung.png" # Set the page icon
# # )

# # # Import your modules
# # import Home
# # import Account
# # import Test
# # from AdditionalInfo import app as AdditionalInfoApp
# # import Contact
# # import AboutUs


# # class MultiApp:
# #     def __init__(self, is_logged_in=False):
# #         self.apps = []
# #         self.is_logged_in = is_logged_in

# #     def add_app(self, title, func):
# #         self.apps.append({
# #             "title": title,
# #             "function": func
# #         })

# #     def run(self):
# #         if not self.is_logged_in:
# #             Account.app()
# #             if st.session_state.get("is_login_successful", False):
# #                 self.is_logged_in = True
# #             else:
# #                 return
# #             with st.sidebar:
# #                 custom_logo_path = 'lung.png'

# #                 # Display the custom logo
# #                 st.image(custom_logo_path, use_column_width=True, width=20)
# #                 # Create a selection box in the sidebar for choosing different pages
# #                 selected_page = option_menu(
# #                     menu_title='LungsVision',
# #                         options=[
# #                             'Account',  # Change the order of pages
# #                             'Home',
# #                             'Test',
# #                             'Additional Info',
# #                             'Contact',
# #                             'About Us',
# #                         ],
# #                         icons=[
# #                             'clock',  # Use appropriate icon for history
# #                             'house-fill',
# #                             'house-fill',
# #                             'eye',
# #                             'phone',
# #                             'info-circle-fill',
# #                             # Use 'phone' icon for contact
# #                         ],
# #                         #menu_icon='chat-text-fill',
# #                         default_index=0,
# #                         styles={
# #                             "container": {"padding": "5px!important", "background-color": 'black'},
# #                             "icon": {"color": "white", "font-size": "23px"},
# #                             "nav-link": {"color": "white", "font-size": "16px", "text-align": "left", "margin": "0px",
# #                                         "--hover-color": "blue"},
# #                             "nav-link-selected": {"background-color": "#02ab21"},
                            
# #                         },
# #                     )

# #             if selected_page == 'Home':
# #                     Home.app()
# #             elif selected_page == 'Test':
# #                     Test.app()
# #             elif selected_page == 'Additional Info':
# #                     AdditionalInfoApp(model, classes)
# #             elif selected_page == 'Contact':
# #                     Contact.app()
# #             elif selected_page == 'About Us':
# #                     AboutUs.app()     
            
                    
                    
# # # Load the model outside of the run method
# # model = tf.keras.models.load_model("my_model2.hdf5", compile=False)
# # # Mapping class indices to labels
# # classes = [
# #     "Large cell carcinoma Lung Cancer",
# #     "Adenocarcinoma Chest Lung Cancer",
# #     "Squamous cell carcinoma Lung Cancer"
# #     "NO Lung Cancer/ NORMAL",
    
# # ]                   


# # # Create an instance of MultiApp and run it
# # if __name__ == "__main__":
# #     # Check if the user is logged in (you need to implement this check based on your authentication mechanism)
# #     is_logged_in = False  # Change this to the actual check for login status

# #     multi_app = MultiApp(is_logged_in)
# #     multi_app.run()

# # main.py
# import streamlit as st
# from streamlit_option_menu import option_menu
# from PIL import Image
# import tensorflow as tf
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.applications.inception_v3 import preprocess_input
# import numpy as np

# # Set the page config
# st.set_page_config(
#     page_title="Lung Cancer Detection",  # Set the page title
#     page_icon="lung.png"  # Set the page icon
# )

# # Import your modules
# import Home
# import Account
# import Test
# from AdditionalInfo import app as AdditionalInfoApp
# import Contact
# import AboutUs

# class MultiApp:
#     def __init__(self, is_logged_in=False):
#         self.apps = []
#         self.is_logged_in = is_logged_in

#     def add_app(self, title, func):
#         self.apps.append({
#             "title": title,
#             "function": func
#         })

#     def run(self):
#         if not self.is_logged_in:
#             if not self.is_logged_in:
#                 Account.app()
#             if st.session_state.get("is_login_successful", False):
#                 self.is_logged_in = True
#             else:
#                 return
#             with st.sidebar:
#                 custom_logo_path = 'lung.png'

#                 # Display the custom logo
#                 st.image(custom_logo_path, use_column_width=True, width=20)
#                 # Create a selection box in the sidebar for choosing different pages
#                 selected_page = option_menu(
#                     menu_title='LungsVision',
#                     options=[
#                         'Account',  # Change the order of pages
#                         'Home',
#                         'Test',
#                         'Additional Info',
#                         'Contact',
#                         'About Us',
#                     ],
#                     icons=[
#                         'clock',  # Use appropriate icon for history
#                         'house-fill',
#                         'eye',
#                         'info',
#                         'phone',
#                         'info-circle-fill',
#                         # Use 'phone' icon for contact
#                     ],
#                     default_index=0,
#                     styles={
#                         "container": {"padding": "5px!important", "background-color": 'black'},
#                         "icon": {"color": "white", "font-size": "23px"},
#                         "nav-link": {"color": "white", "font-size": "16px", "text-align": "left", "margin": "0px",
#                                     "--hover-color": "blue"},
#                         "nav-link-selected": {"background-color": "#02ab21"},
#                     },
#                 )

#                 if selected_page == 'Home':
#                     Home.app()
#                 elif selected_page == 'Test':
#                     Test.app()
#                 elif selected_page == 'Additional Info':
#                     # Load the model outside of the run method
#                     model = tf.keras.models.load_model("my_model2.hdf5", compile=False)
#                     # Mapping class indices to labels
#                     classes = [
#                         "Large cell carcinoma Lung Cancer",
#                         "Adenocarcinoma Chest Lung Cancer",
#                         "Squamous cell carcinoma Lung Cancer",
#                         "NO Lung Cancer/ NORMAL",
#                     ]
#                     AdditionalInfoApp(model, classes)
#                 elif selected_page == 'Contact':
#                     Contact.app()
#                 elif selected_page == 'About Us':
#                     AboutUs.app()

# # Create an instance of MultiApp and run it
# if __name__ == "__main__":
#     # Check if the user is logged in (you need to implement this check based on your authentication mechanism)
#     is_logged_in = False  # Change this to the actual check for login status

# multi_app = MultiApp(is_logged_in)
# multi_app.run()
# main.py
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input
import numpy as np

# Set the page config
st.set_page_config(
    page_title="Lung Cancer Detection",  # Set the page title
    page_icon="lung.png"  # Set the page icon
)

# Import your modules
import Home
import Account
import Test
from AdditionalInfo import app as AdditionalInfoApp
import Contact
import AboutUs

class MultiApp:
    def __init__(self, is_logged_in=False):
        self.is_logged_in = is_logged_in
        self.selected_page = None

    def run(self):
        if not self.is_logged_in:
            Account.app()
            if st.session_state.get("is_login_successful", False):
                self.is_logged_in = True
            else:
                return

        with st.sidebar:
            custom_logo_path = 'lung.png'

            # Display the custom logo
            st.image(custom_logo_path, use_column_width=True, width=20)
            # Create a selection box in the sidebar for choosing different pages
            selected_page = option_menu(
                menu_title='LungsVision',
                options=[
                    'Account',  # Change the order of pages
                    'Home',
                    'Test',
                    'Additional Info',
                    'Contact',
                    'About Us',
                ],
                icons=[
                    'clock',  # Use appropriate icon for history
                    'house-fill',
                    'eye',
                    'info',
                    'phone',
                    'info-circle-fill',
                    # Use 'phone' icon for contact
                ],
                default_index=0,
                styles={
                    "container": {"padding": "5px!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "16px", "text-align": "left", "margin": "0px",
                                "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                },
            )

        self.selected_page = selected_page
        self.show_selected_page()

    def show_selected_page(self):
        if self.selected_page == 'Home':
            Home.app()
        elif self.selected_page == 'Test':
            Test.app()
        elif self.selected_page == 'Additional Info':
            # Load the model outside of the run method
            model = tf.keras.models.load_model("my_model2.hdf5", compile=False)
            # Mapping class indices to labels
            classes = [
                "Large cell carcinoma Lung Cancer",
                "Adenocarcinoma Chest Lung Cancer",
                "Squamous cell carcinoma Lung Cancer",
                "NO Lung Cancer/ NORMAL",
            ]
            AdditionalInfoApp(model, classes)
        elif self.selected_page == 'Contact':
            Contact.app()
        elif self.selected_page == 'About Us':
            AboutUs.app()

# Create an instance of MultiApp and run it
if __name__ == "__main__":
    # Check if the user is logged in (you need to implement this check based on your authentication mechanism)
    is_logged_in = False  # Change this to the actual check for login status

    multi_app = MultiApp(is_logged_in)
multi_app.run()
