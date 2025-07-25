# 🖼️ Chatbot for Image Summary

This project is a **multimodal AI chatbot** that takes an image as input, extracts its content using OCR and captioning, and generates a human-readable summary or answers questions using **Large Language Models (LLMs)**.

Built during my time at **TAO Digital**, the chatbot follows an **agentic architecture** where individual components act as specialized agents—handling tasks like image preprocessing, OCR, image captioning, prompt generation, and response generation.

## 🔍 Features

- 🧠 **LLM-powered summarization** using OpenAI GPT models  
- 📸 **Image input** via file upload  
- 🔤 **OCR extraction** using `pytesseract`  
- 🖼️ **Image captioning** using BLIP (Bootstrapped Language Image Pretraining)  
- 🗨️ **Interactive chatbot** interface to ask questions based on the image content  
- 🧩 **Agentic framework** where each processing stage acts as a modular agent

## 🧰 Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **LLM**: OpenAI GPT (via API)  
- **OCR**: Tesseract OCR via `pytesseract`  
- **Captioning**: Salesforce BLIP  
- **Libraries**: `transformers`, `PIL`, `streamlit`, `openai`, `pytesseract`, `torch`

## 🗂️ Architecture

```
[Image Input] → [OCR Agent] → [Captioning Agent] → [LLM Prompt Generator] → [Chatbot Response]
```

Each agent has a specific role, passing its output to the next, forming a pipeline that closely resembles an **agentic framework** commonly used in modern LLM applications.

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/BharatVarma007/Chatbot-for-image-summery.git
cd Chatbot-for-image-summery
```

### 2. Set Up the Environment

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Add Your OpenAI API Key

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_api_key
```

### 4. Run the App

```bash
streamlit run app.py
```

Upload an image, and the chatbot will display a caption, extract text using OCR, and summarize or respond to your queries about the image.

## 📌 Example Use Case

Upload a screenshot of a document or image with text. The chatbot will:

- Extract the text content
- Generate a natural language summary
- Let you ask follow-up questions about the image content

## 🧠 Agentic Principles Applied

This project modularizes AI components like:

- OCR (Perception Agent)
- Image Captioning (Vision-Language Agent)
- Prompting (Instruction Agent)
- LLM Response (Reasoning Agent)

These "agents" are composed in sequence to form a complete understanding pipeline, showcasing **early-stage agentic AI design**.

## 📎 Resources

- [BLIP (Salesforce)](https://github.com/salesforce/BLIP)
- [OpenAI API](https://platform.openai.com/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

## 📜 License

MIT License

---

Feel free to fork or contribute!
