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

**

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

Let me know if you'd like to include badges (e.g., Python version, license, Streamlit/FastAPI badges), or add sections like **Authors**, **Roadmap**, or **Acknowledgements**.
"# galaxy-image-colorizer" 
