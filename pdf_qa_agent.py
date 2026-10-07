# PDF Question Answering Agent

import PyPDF2

pdf_file = "sample.pdf"

file = open(pdf_file, "rb")

reader = PyPDF2.PdfReader(file)

pdf_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        pdf_text += text + " "

pdf_text = pdf_text.lower()

print("PDF Question Answering Agent Started")
print("Type exit to stop")

while True:
    question = input("\nAsk keyword/question: ").lower()

    if question == "exit":
        print("Goodbye!")
        break

    words = question.split()
    found_words = []

    for word in words:
        if word in pdf_text:
            found_words.append(word)

    if found_words:
        print("Matched Words:", found_words)
        print("Answer: Related information is available in the PDF.")
    else:
        print("Answer: No matching information found.")