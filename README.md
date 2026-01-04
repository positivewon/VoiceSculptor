<div align="center">
    <h1>
    VoiceSculptor
    </h1>
    <p>Official inference code for <br>
    <b><em>VoiceSculptor: Your Voice, Designed By You</em></b>
    </p>
    <p>
    <img src="assets/logo.png" style="width: 400px; height: 400px;">
    </p>
    <a href="https://hujingbin1.github.io/VoiceSculptor-Demo/"><img src="https://img.shields.io/badge/Demo-Page-lightgrey" alt="version"></a>
    <a href="https://huggingface.co/collections/ASLP-lab/voicesculptor"><img src='https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model-blue' alt="HF-model"></a>
    <a href="https://github.com/ASLP-lab/VoiceSculptor"><img src='https://img.shields.io/badge/Report-Github?label=Technical&color=red' alt="technical report"></a>
    <a href="https://huggingface.co/collections/ASLP-lab/voicesculptor"><img src='https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Demo-blue' alt="HF-demo"></a>
</div>

## Demo Video

<div>
  <https://github.com/user-attachments/assets/88c7230f-3ad8-4f37-b7fb-33a52f2b469d.mp4>
</div>

## 🚀 Getting Started

### 1. Environment Setup

Follow the steps below to clone the repository and install the required environment.

```bash
# Clone the repository and enter the directory
git clone https://github.com/ASLP-lab/VoiceSculptor.git
cd VoiceSculptor

# Create and activate a Conda environment
conda create -n VoiceSculptor python=3.10 -y
conda activate VoiceSculptor

# Install dependencies
pip install -r requirements.txt
```

### 2. Download Pre-trained Models

```bash
git lfs install
git clone https://huggingface.co/ASLP-lab/VoiceSculptor
```

### 3. Infer

```bash
python infer.py
```

### 4. Webui

```bash
python gradio.py
```


### 5. RAG

```bash
```


## 📋 TODO

-   [x] 🌐 **Demo website**
-   [x] 🔓 **Release inference code**
-   [x] 🤗 **HuggingFace model release**
-   [] 🤗 **HuggingFace Space**
-   [] 📝 **Paper release**
-   [] 🔓 **Release gradio code**
-   [] 🔓 **Release rag code**
-   [] 🔓 **Support vllm**
-   [] 🔓 **Release training code**