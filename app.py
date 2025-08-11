import streamlit as st
from transformers import pipeline
import warnings

warnings.filterwarnings("ignore")

# ---------------------------
# Title & Description
# ---------------------------
st.set_page_config(page_title="Article Q&A and Summarizer", page_icon="📝", layout="centered")
st.title("📝 Article Q&A and Summarizer")
st.write("Paste an article below, ask a question, and get a summary!")

# ---------------------------
# Load Models (cached)
# ---------------------------
@st.cache_resource
def load_qa_model():
    return pipeline("question-answering", model="deepset/roberta-base-squad2")

@st.cache_resource
def load_summarizer():
    return pipeline("summarization")

qa_model = load_qa_model()
summarizer_model = load_summarizer()

# ---------------------------
# Helper function to split into chunks
# ---------------------------
def generate_chunks(inp_str):
    max_chunk = 500
    inp_str = inp_str.replace('.', '.<eos>')
    inp_str = inp_str.replace('?', '?<eos>')
    inp_str = inp_str.replace('!', '!<eos>')

    sentences = inp_str.split('<eos>')
    current_chunk = 0
    chunks = []
    for sentence in sentences:
        if len(chunks) == current_chunk + 1:
            if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
                chunks[current_chunk].extend(sentence.split(' '))
            else:
                current_chunk += 1
                chunks.append(sentence.split(' '))
        else:
            chunks.append(sentence.split(' '))

    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = ' '.join(chunks[chunk_id])
    return chunks

# ---------------------------
# Inputs
# ---------------------------
article = st.text_area("📄 Paste your article here:", height=250)
question = st.text_input("❓ Ask a question about the article:")
min_len = st.number_input("Minimum summary length", min_value=10, max_value=200, value=10)
max_len = st.number_input("Maximum summary length", min_value=20, max_value=500, value=50)

# ---------------------------
# Process Button
# ---------------------------
if st.button("Run Q&A and Summarize"):
    if article.strip():
        # Question Answering
        if question.strip():
            answer = qa_model(question=question, context=article)
            st.subheader("Answer to your question:")
            st.write(answer['answer'])
        else:
            st.info("No question entered. Skipping Q&A.")

        # Summarization
        chunks = generate_chunks(article)
        res = summarizer_model(chunks, max_length=max_len, min_length=min_len)
        summary_text = ' '.join([summ['summary_text'] for summ in res])

        st.subheader("Article Summary:")
        st.write(summary_text)

    else:
        st.error("Please paste an article first.")
