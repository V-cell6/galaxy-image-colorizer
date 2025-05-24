import streamlit as st
import requests
from PIL import Image
import io
import os
from main import RGB_DIR, GALAXY_DIR, L_CHANNEL_DIR

# API endpoints
GENERATE_API = "http://localhost:8000/generate/"  # Endpoint for generating galaxy images
COLORIZE_API = "http://localhost:8000/colorize/"  # Endpoint for colorizing images

# Set up the Streamlit page layout
st.set_page_config(page_title="Galaxy Image Colorizer", layout="wide", page_icon="🌌")

# Sidebar setup
st.sidebar.image("logo.png", use_column_width=True)  # Display logo image in the sidebar
st.sidebar.write("Welcome to the Galaxy Image Colorizer!")  # Welcome message

# Sidebar navigation
st.sidebar.markdown("## Navigate")

# Initialize page variable in session state
if 'page' not in st.session_state:
    st.session_state.page = "Generate a New Galaxy Image"  # Default page when first loaded

# Initialize the upload counter in session state
if 'upload_counter' not in st.session_state:
    st.session_state.upload_counter = 0  # Counter to track uploads

# Navigation buttons in the sidebar
if st.sidebar.button("🌌 Generate a New Galaxy Image"):
    st.session_state.page = "Generate a New Galaxy Image"  # Change page to generate image
if st.sidebar.button("🎨 Colorize an Image of Galaxy (Galaxy Zoo Format)"):
    # Reset counter when navigating to colorization page
    st.session_state.page = "Colorize an Image of Galaxy (Galaxy Zoo Format)"
    st.session_state.upload_counter = 0  # Reset the upload counter

# Page 1: Generate and Color the Random Galaxy Images
if st.session_state.page == "Generate a New Galaxy Image":
    st.title("Refresh to Generate a New Galaxy Image")  # Title for the page

    # Function to load the latest galaxy image from the directory
    def load_latest_galaxy_image():
        latest_image_path = sorted(os.listdir(GALAXY_DIR))[-1]  # Get the most recent file
        return Image.open(os.path.join(GALAXY_DIR, latest_image_path))  # Open the image file

    # Create columns for layout
    col1, col2 = st.columns(2)  # Create two columns for displaying images

    # Trigger image generation on first load
    if 'galaxy_image' not in st.session_state:
        with st.spinner("Generating your galaxy image..."):  # Show spinner while generating
            response = requests.post(GENERATE_API)  # POST request to generate galaxy image
            if response.status_code == 200:  # Check if the request was successful
                st.session_state.galaxy_image = load_latest_galaxy_image()  # Load the generated image
                st.session_state.image_displayed = True  # Track if an image has been displayed

    # Display the generated image if it exists
    if st.session_state.get('image_displayed', False):
        with col1:
            st.image(st.session_state.galaxy_image, caption="AI Generated Galaxy Image", use_column_width=True)  # Display generated image

            # Button to colorize the currently displayed image
            if st.button("Colorize it"):
                img_byte_arr = io.BytesIO()  # Create a byte stream for the image
                st.session_state.galaxy_image.save(img_byte_arr, format='PNG')  # Save the image to the byte stream
                img_byte_arr.seek(0)  # Seek to the beginning of the stream
                files = {'file': img_byte_arr.getvalue()}  # Prepare file for POST request
                
                with col2:
                    with st.spinner("Colorizing the image..."):  # Show spinner while colorizing
                        colorize_response = requests.post(COLORIZE_API, files=files)  # POST request to colorize the image

                        if colorize_response.status_code == 200:  # Check if colorization was successful
                            # Load and display the latest RGB image
                            rgb_image_path = sorted(os.listdir(RGB_DIR))[-1]  # Get the most recent colorized image
                            colorized_image = Image.open(os.path.join(RGB_DIR, rgb_image_path))  # Open the image file
                            
                            # Display colorized image in the second column
                            st.image(colorized_image, caption="AI Colorized Image", use_column_width=True)
    else:
        st.info("Generating your galaxy image...")  # Inform user that the galaxy image is being generated

# Page 2: Colorize an Image of Galaxy (Galaxy Zoo Format)
if st.session_state.page == "Colorize an Image of Galaxy (Galaxy Zoo Format)":
    st.title("Colorize an Image of Galaxy (Galaxy Zoo Format)")  # Title for the colorization page

    # Reset the upload counter when the file uploader is activated
    uploaded_file = st.file_uploader(
        "Upload an image", type=["png", "jpg", "jpeg"],
        on_change=lambda: setattr(st.session_state, 'upload_counter', 0)  # Reset counter on upload
    )

    if uploaded_file is not None:  # Check if a file has been uploaded
        # Prepare to colorize the uploaded image
        img_byte_arr = io.BytesIO()  # Create a byte stream
        uploaded_image = Image.open(uploaded_file)  # Open the uploaded image file
        uploaded_image.save(img_byte_arr, format='PNG')  # Save it to the byte stream
        img_byte_arr.seek(0)  # Seek to the beginning of the stream
        files = {'file': img_byte_arr.getvalue()}  # Prepare file for POST request

        # Increment upload counter
        st.session_state.upload_counter += 1
        
        # Check the upload counter to determine spinner message
        if st.session_state.upload_counter == 1:
            with st.spinner("Uploading the Black and White Image of the Galaxy..."):  # Show spinner while uploading
                colorize_response = requests.post(COLORIZE_API, files=files)  # POST request to colorize the image
        else:
            with st.spinner("Colorizing the image..."):  # Show spinner for subsequent uploads
                colorize_response = requests.post(COLORIZE_API, files=files)

        if colorize_response.status_code == 200:  # Check if colorization was successful
            # Get the most recent L channel image
            l_channel_image_path = sorted(os.listdir(L_CHANNEL_DIR))[-1]  # Get the most recent L channel image
            l_channel_image = Image.open(os.path.join(L_CHANNEL_DIR, l_channel_image_path))  # Open the image file
            
            # Get the most recent RGB image (to display later)
            rgb_image_path = sorted(os.listdir(RGB_DIR))[-1]  # Get the most recent colorized image
            rgb_image = Image.open(os.path.join(RGB_DIR, rgb_image_path))  # Open the image file

            # Create two columns for the L channel image and RGB image
            col1, col2 = st.columns(2)

            # Display the L channel image in the first column
            with col1:
                st.image(l_channel_image, caption="Black and White Image", use_column_width=True)  # Display L channel image

            # Prepare a placeholder for the colorized image
            with col2:
                placeholder = st.empty()  # Create an empty placeholder for the colorized image

            # Button to colorize the L channel image
            if st.button("Colorize"):
                # Update the placeholder with the colorized image
                with col2:
                    placeholder.image(rgb_image, caption="AI Generated Colorized Image", use_column_width=True)  # Display colorized image
