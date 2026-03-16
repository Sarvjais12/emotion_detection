# 🧠 Emotion-Aware Customer Support Agent

[![Live Demo](https://img.shields.io/badge/Live_Demo-Hugging_Face-ffd700?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/Sarvjais12/customer_support_emotion_detection)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)

> A multimodal Artificial Intelligence system designed to analyze customer sentiment and facial expressions in real-time. Built to empower customer support pipelines with adaptive, emotion-aware response logic.

## 🚀 Overview

This repository contains the source code for an emotionally intelligent customer support agent. It utilizes a dual-modality approach to understand user frustration, joy, and neutral states during support interactions. 

By dynamically shifting response tones and escalation paths based on detected emotions, this architecture aims to significantly improve automated customer satisfaction workflows.

### 📊 Performance Metrics
* **NLP Classification Accuracy:** Achieved a **92% F1-Score** on multi-class customer service sentiment datasets.
* **Latency:** Optimized for real-time inference via Gradio on Hugging Face Spaces.

## 🏗️ System Architecture

The system is split into two core analytical pipelines:

1. **Natural Language Processing (NLP):**
   * Utilizes transformer-based architectures for real-time text sentiment detection.
   * Fine-tuned to understand the nuances of customer support dialogues (e.g., sarcasm, urgency, satisfaction).
2. **Computer Vision (CV):**
   * Integrates the **DeepFace** framework to analyze and classify facial expressions from user-uploaded images or webcam feeds.
   * Captures visual micro-expressions to complement textual sentiment analysis.

## 🛠️ Technology Stack

| Component | Technology |
| :--- | :--- |
| **Deep Learning Framework** | PyTorch |
| **NLP Backend** | Hugging Face Transformers |
| **Vision Backend** | DeepFace, OpenCV |
| **Deployment & UI** | Gradio, Docker |
| **Data Processing** | Pandas, NumPy |

## 💻 Installation & Setup

To run this project locally, ensure you have Python 3.8+ installed.

**1. Clone the repository:**
```bash
git clone [https://github.com/Sarvjais12/customer_support_emotion_detection.git](https://github.com/Sarvjais12/customer_support_emotion_detection.git)
cd customer_support_emotion_detection
2. Create a virtual environment (Recommended):

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies:

Bash
pip install -r requirements.txt
4. Run the application:

Bash
python app.py
The Gradio interface will launch locally at http://127.0.0.1:7860/.

🌐 Live Deployment
The production-ready model is containerized and currently hosted on Hugging Face Spaces.

👉 Interact with the Live Agent Here

🔮 Future Scope
Integration of speech-to-text (ASR) for real-time voice sentiment analysis.

Stateful memory orchestration (via LangGraph) to remember customer mood across multi-turn interactions.

Deployment of a lightweight API endpoint using FastAPI for seamless frontend integration.

👨‍💻 Author
Sarvagya Jaiswal Founding Machine Learning Engineer

Portfolio

LinkedIn

Hugging Face
