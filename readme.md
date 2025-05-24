# 🌌 Galaxy Image Colorizer

Welcome to the **Galaxy Image Colorizer**, a deep learning-powered application that can:

1. **Generate** realistic images of galaxies
2. **Colorize** grayscale galaxy images using a pretrained Pix2Pix model

This project combines a FastAPI backend with a Streamlit frontend to offer an interactive AI experience.

---

## 🚀 Getting Started

Follow these steps to set up the project locally:

1. **Create a virtual environment**

   ```bash
   python -m venv <venv_name>
   ```

2. **Activate the environment**

   * On Windows:

     ```bash
     .\<venv_name>\Scripts\activate
     ```
   * On macOS/Linux:

     ```bash
     source <venv_name>/bin/activate
     ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Start the FastAPI backend**

   ```bash
   uvicorn main:app --reload
   ```

5. **Launch the Streamlit frontend**

   ```bash
   streamlit run frontend.py
   ```

You’re all set to explore the universe with AI!

---

## 🧑‍💻 How to Use the App

* On the **Home page**, refresh the view to generate new galaxy images.
* Click the `Colorize` button to color the grayscale image using the pretrained Pix2Pix Generator.
* On the **Upload page**, manually upload galaxy images (e.g., from the Galaxy Zoo test set).
* The app will display both the grayscale (L-channel) and the colorized RGB output.

---

## 🗂️ Image Storage

The application saves processed images in the following directories:

| Folder                    | Description                             |
| ------------------------- | --------------------------------------- |
| `Generated_Galaxy_Images` | Stores AI-generated galaxy images       |
| `L_channel_Images`        | Stores uploaded grayscale galaxy images |
| `RGB_Generated_Images`    | Stores colorized RGB galaxy images      |

> 📌 **Note:** All images are named using the current date-time to ensure uniqueness.

---

## 💡 Technologies Used

* **FastAPI** – API backend
* **Streamlit** – UI frontend
* **Pix2Pix GAN** – Image-to-image translation model
* **Python** – Main development language

---

## 📷 Example Output

Step 1: Webpage after running the Streamlit Script

![image](https://github.com/user-attachments/assets/2ece264d-0825-4c23-83d5-a3946b92e869)



Step 2: Click on browse files to upload a PNG/JPG/JPEG image of the galaxy 

![image](https://github.com/user-attachments/assets/be8a62e4-2fcd-4edb-9566-29332f8dc016)



Step 3: After the image has been uploaded successfully, click on “Colorize” as shown

![image](https://github.com/user-attachments/assets/1913a7ac-47ac-42e5-8ca3-0d21facc9cb6)



Result: The Pix-2-Pix model runs in the backend to produce the colorized image 

![image](https://github.com/user-attachments/assets/dede2a6f-9205-47fd-a6d2-e2b54190cc6e)



---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---
