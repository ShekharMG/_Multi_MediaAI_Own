# 🎥 MultiMedia AI

This project is a **Proof of Concept (POC)** showcasing multimodal AI orchestration.  
It generates an **image from text**, creates **narration audio**, and combines them into a **video** using open-source models and free tools.

---

## 🚀 Features
- **Text → Image** using Stable Diffusion (Hugging Face Diffusers)
- **Text → Audio** using gTTS (Google Text-to-Speech)
- **Combine** into video with MoviePy
- Lightweight (runs on CPU, no GPU required)

---

## 📂 Project Structure
│── main.py # Main script
│── requirements.txt # Dependencies
│── README.md # Project documentation
│── poc_outputs/ # Generated outputs
│ ├── generated_image.png
│ ├── narration.wav
│ ├── final_demo.mp4


---

## ⚙️ Installation & Setup (Windows)

### 1. Clone repository
```powershell
   git clone https://github.com/your-username/multimodal_poc_simple.git
   cd multimodalAI
```
### 2. Create virtual environment
py -3.10 -m venv venv
.\venv\Scripts\activate

### 3. Install requirements
pip install --upgrade pip
pip install -r requirements.txt
pip install imageio[ffmpeg] pydub

### 4. ▶️ Run the Program
python main.py

