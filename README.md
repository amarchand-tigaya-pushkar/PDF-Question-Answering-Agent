# 📄 PDF Question Answering Agent

A beginner-friendly Python Agentic AI project that reads text from a PDF and searches the document for matching words based on the user's question.

## 🎯 Project Goal

Create an agent that reads a PDF and answers questions from it.

## 🔄 Workflow

```text
Upload PDF
    ↓
Extract text from PDF
    ↓
User asks question
    ↓
Agent searches PDF text
    ↓
Agent gives answer
```

## 🛠️ Tools Required

- Python
- VS Code
- PyPDF2
- Basic `input()`
- If-Else
- String Matching

## 📁 Project Structure

```text
PDF-Question-Answering-Agent/
├── pdf_qa_agent.py
├── sample.pdf
├── README.md
└── requirements.txt
```

## 📦 Installation

Install PyPDF2:

```bash
pip install PyPDF2
```

## 📄 Add Your PDF

Keep your PDF in the same folder as the Python file.

Rename your PDF:

```text
sample.pdf
```

Example:

```text
PDF-Question-Answering-Agent/
├── pdf_qa_agent.py
├── sample.pdf
├── README.md
└── requirements.txt
```

## ▶️ Run the Project

```bash
python pdf_qa_agent.py
```

## 💻 Example

```text
PDF Question Answering Agent Started
Type exit to stop

Ask keyword/question: machine learning

Matched Words: ['machine', 'learning']
Answer: Related information is available in the PDF.
```

If no matching word is found:

```text
Answer: No matching information found.
```

## 🧠 How It Works

### PyPDF2

PyPDF2 is used to read the PDF file.

### PdfReader

```python
reader = PyPDF2.PdfReader(file)
```

Reads the PDF pages.

### extract_text()

```python
text = page.extract_text()
```

Extracts text from each PDF page.

### lower()

```python
pdf_text = pdf_text.lower()
```

Converts PDF text to lowercase.

### split()

```python
words = question.split()
```

Breaks the user's question into individual words.

### Keyword Matching

```python
for word in words:
    if word in pdf_text:
        found_words.append(word)
```

Checks whether the words from the question are available in the PDF text.

## 🤖 Agentic AI Thinking

### User Goal

```text
Ask question from PDF
```

### Agent Steps

1. Read PDF
2. Extract text
3. Understand user question
4. Search matching words
5. Return answer

## 🚀 Project Extensions

1. Add Streamlit interface
2. Upload PDF from browser
3. Add multiple PDFs
4. Add OpenAI API
5. Add LangChain
6. Add ChromaDB vector database
7. Add RAG system
8. Add voice question answering

## 📚 Concepts Learned

- PDF reading
- PyPDF2
- Text extraction
- Python loops
- Conditions
- String matching
- `split()`
- `lower()`
- Keyword search
- Basic AI agent workflow

## 📌 Description

A PDF Question Answering Agent reads text from a PDF and answers user questions by searching matching words inside the document. It helps beginners understand PDF reading, text extraction, loops, conditions, and basic AI agent workflow.