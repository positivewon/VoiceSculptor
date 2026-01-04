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
    <a href="https://github.com/ASLP-lab/VoiceSculptor"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="Apache-2.0"></a>
</div>

## ✨ Demo Video

<div align="center">

<https://github.com/user-attachments/assets/88c7230f-3ad8-4f37-b7fb-33a52f2b469d>

</div>

## 🔥 News


- **[2026-1-2]** We opened the repository and uploaded the voice design models! You get it here:[VoiceSculptor](https://huggingface.co/collections/ASLP-lab/voicesculptor)

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
python build_rag.py
```


## 📋 TODO

-   [x] 🌐 **Demo website**
-   [x] 🔓 **Release inference code**
-   [x] 🤗 **Release HuggingFace model**
-   [] 🤗 **HuggingFace Space**
-   [] 📝 **Paper release**
-   [] 🔓 **Release gradio code**
-   [] 🔓 **Release RAG code**
-   [] 🔓 **Support vLLM**
-   [] 🔓 **Release training code**
-   

## Citation

```bibtex
@misc{du2024cosyvoice2scalablestreaming,
      title={CosyVoice 2: Scalable Streaming Speech Synthesis with Large Language Models},
      author={Zhihao Du and Yuxuan Wang and Qian Chen and Xian Shi and Xiang Lv and Tianyu Zhao and Zhifu Gao and Yexin Yang and Changfeng Gao and Hui Wang and Fan Yu and Huadai Liu and Zhengyan Sheng and Yue Gu and Chong Deng and Wen Wang and Shiliang Zhang and Zhijie Yan and Jingren Zhou},
      year={2024},
      eprint={2412.10117},
      archivePrefix={arXiv},
      primaryClass={cs.SD},
      url={https://arxiv.org/abs/2412.10117},
}
@misc{ye2025llasascalingtraintimeinferencetime,
      title={Llasa: Scaling Train-Time and Inference-Time Compute for Llama-based Speech Synthesis},
      author={Zhen Ye and Xinfa Zhu and Chi-Min Chan and Xinsheng Wang and Xu Tan and Jiahe Lei and Yi Peng and Haohe Liu and Yizhu Jin and Zheqi Dai and Hongzhan Lin and Jianyi Chen and Xingjian Du and Liumeng Xue and Yunlin Chen and Zhifei Li and Lei Xie and Qiuqiang Kong and Yike Guo and Wei Xue},
      year={2025},
      eprint={2502.04128},
      archivePrefix={arXiv},
      primaryClass={eess.AS},
      url={https://arxiv.org/abs/2502.04128},
}
@misc{huang2025instructttsevalbenchmarkingcomplexnaturallanguage,
      title={InstructTTSEval: Benchmarking Complex Natural-Language Instruction Following in Text-to-Speech Systems}, 
      author={Kexin Huang and Qian Tu and Liwei Fan and Chenchen Yang and Dong Zhang and Shimin Li and Zhaoye Fei and Qinyuan Cheng and Xipeng Qiu},
      year={2025},
      eprint={2506.16381},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2506.16381},
}
@misc{wang2025sparkttsefficientllmbasedtexttospeech,
      title={Spark-TTS: An Efficient LLM-Based Text-to-Speech Model with Single-Stream Decoupled Speech Tokens}, 
      author={Xinsheng Wang and Mingqi Jiang and Ziyang Ma and Ziyu Zhang and Songxiang Liu and Linqin Li and Zheng Liang and Qixi Zheng and Rui Wang and Xiaoqin Feng and Weizhen Bian and Zhen Ye and Sitong Cheng and Ruibin Yuan and Zhixian Zhao and Xinfa Zhu and Jiahao Pan and Liumeng Xue and Pengcheng Zhu and Yunlin Chen and Zhifei Li and Xie Chen and Lei Xie and Yike Guo and Wei Xue},
      year={2025},
      eprint={2503.01710},
      archivePrefix={arXiv},
      primaryClass={cs.SD},
      url={https://arxiv.org/abs/2503.01710}, 
}
```

## License

We use the Apache 2.0 license. Researchers and developers are free to use the codes and model weights of our VoiceSculptor. Check the license at [LICENSE](LICENSE) for more details.

## Acknowledge
- This repo benefits from [LLaSA]https://github.com/zhenye234/LLaSA_training
- This repo benefits from [CosyVoice](https://github.com/FunAudioLLM/CosyVoice)


##  Usage Disclaimer
Additional Notice on Generated Voices

This project provides a speech synthesis model for voice design, intended for academic research, educational purposes, and legitimate applications, such as personalized speech synthesis, assistive technologies, and linguistic research.

Please note:

Do not use this model for unauthorized voice cloning, impersonation, fraud, scams, deepfakes, or any illegal or malicious activities.

Ensure compliance with local laws and regulations when using this model and uphold ethical standards.

The developers assume no liability for any misuse of this model.

Important clarification regarding generated voices:

As a generative model, the voices produced by this system are synthetic outputs inferred by the model, not recordings of real human voices.

The generated voice characteristics do not represent or reproduce any specific real individual, and are not derived from or intended to imitate identifiable persons.

We advocate for the responsible development and use of AI and encourage the community to uphold safety and ethical principles in AI research and applications. If you have any concerns regarding ethics, safety, or potential misuse, please contact us.

## Contact Us
If you are interested in leaving a message to our work, feel free to email jingbin.hu@mail.nwpu.edu.cn or lxie@nwpu.edu.cn

You’re welcome to join our WeChat group for technical discussions, updates.
<p align="center">
  <!-- <em>Due to group limits, if you can't scan the QR code, please add my WeChat for group access  -->
      <!-- : <strong>Tiamo James</strong></em> -->
  <br>
  <span style="display: inline-block; margin-right: 10px;">
    <img src="assets/wechat.png" width="300" alt="WeChat Group QR Code"/>
  </span>
  <!-- <span style="display: inline-block;">
    <img src="assets/wechat_tiamo.jpg" width="300" alt="WeChat QR Code"/>
  </span> -->
</p>
