# 📝 Article Q&A and Summarizer

A simple **Streamlit** web application that:
- Answers questions from a given article using a **Question Answering (Q&A) model**.
- Summarizes long articles into concise text using a **Summarization model**.

Built with [Hugging Face Transformers](https://huggingface.co/transformers/) and [Streamlit](https://streamlit.io/).

---

## 🚀 Features

- **Paste an article** directly into the app.
- **Ask any question** about the article and get an accurate answer.
- **Generate a summary** of the article with adjustable min/max length.
- **Powered by state-of-the-art NLP models**:
  - `deepset/roberta-base-squad2` for Question Answering.
  - Default Hugging Face `summarization` pipeline for summarizing.

---

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/article-qa-summarizer.git
   cd article-qa-summarizer
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate      # For Linux/Mac
   venv\Scripts\activate         # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠 Requirements

The main dependencies are:
```
streamlit
transformers
torch
```

You can install them using:
```bash
pip install streamlit transformers torch
```

---

## ▶️ Running the App

Run the app locally:
```bash
streamlit run app.py
```
Then open the link shown in your terminal (usually `http://localhost:8501`).

---

## 🌐 Deployment

You can deploy this app for free using:
- **[Streamlit Cloud](https://streamlit.io/cloud)**
- **[Hugging Face Spaces](https://huggingface.co/spaces)**
- **Render** or any other Python web hosting platform.

For **Streamlit Cloud**:
1. Push your code to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io) and connect your repo.
3. Select your branch and `app.py` file, then deploy.

---

## 📂 Project Structure

```
.
├── app.py               # Streamlit app script
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 💡 How It Works

1. **User Input**:
   - Paste an article into the text area.
   - Optionally, enter a question.

2. **Question Answering**:
   - Uses `deepset/roberta-base-squad2` to extract the most relevant answer from the article.

3. **Summarization**:
   - Splits the article into chunks (max 500 tokens each).
   - Feeds chunks into the Hugging Face `summarization` pipeline.
   - Joins all summaries into a final summary text.

---

## 🖼 Example

**Article:**
> Albert Einstein was a German-born theoretical physicist who developed the theory of relativity, one of the two pillars of modern physics...

**Question:**  
> What is Albert Einstein best known for?

**Answer:**  
> mass–energy equivalence formula, E = mc²

**Summary:**  
> Albert Einstein, a German-born physicist, developed the theory of relativity and the mass–energy equivalence formula E=mc². He received the 1921 Nobel Prize for the photoelectric effect.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🤝 Acknowledgements

- [Hugging Face Transformers](https://huggingface.co/transformers/) for the NLP models.
- [Streamlit](https://streamlit.io/) for making app development simple and interactive.
