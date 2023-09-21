import os
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from sentence_transformers import SentenceTransformer, util
import torch

# Define a function to read the text from a file
def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

# Define a function to calculate the cosine similarity
def calculate_similarity(text1, text2):
    # Load a more advanced sentence embedding model
    model = SentenceTransformer('paraphrase-mpnet-base-v2')

    # Encode the text from both files
    embeddings1 = model.encode(text1, convert_to_tensor=True)
    embeddings2 = model.encode(text2, convert_to_tensor=True)

    # Calculate the cosine similarity between the sentence embeddings
    cosine_similarity = util.pytorch_cos_sim(embeddings1, embeddings2)

    return cosine_similarity.item()

# Function to detect plagiarism and highlight
def detect_plagiarism():
    text1 = text_area1.get("1.0", tk.END)
    text2 = text_area2.get("1.0", tk.END)

    # Calculate the similarity score between the two texts
    similarity_score = calculate_similarity(text1, text2)

    # Display the similarity score
    similarity_score_label.config(text=f'Similarity Score: {similarity_score*100:.2f}%')

    # Highlight plagiarized sections in the text
    highlighted_text = highlight_similar_sentences(text2, text1, similarity_score)

    # Clear the contents of Text 2
    text_area2.delete("1.0", tk.END)

    text_area2.insert(tk.END, highlighted_text.get("1.0", tk.END))

# Function to highlight similar sentences with different colors based on similarity score
def highlight_similar_sentences(text_to_highlight, text_to_compare, similarity_score):
    # Load a more advanced sentence embedding model
    model = SentenceTransformer('paraphrase-mpnet-base-v2')

    # Encode the sentences in both texts
    sentences_to_highlight = [s.strip() for s in text_to_highlight.split('.') if s.strip()]
    sentences_to_compare = [s.strip() for s in text_to_compare.split('.') if s.strip()]
    sentence_embeddings_to_highlight = model.encode(sentences_to_highlight, convert_to_tensor=True)
    sentence_embeddings_to_compare = model.encode(sentences_to_compare, convert_to_tensor=True)

    # Calculate the cosine similarity between each pair of sentence embeddings
    cosine_similarities = util.pytorch_cos_sim(sentence_embeddings_to_highlight, sentence_embeddings_to_compare)

    color_code_frame = tk.Frame(content_frame)
    color_code_frame.grid(column=0, row=4, columnspan=2, pady=5, sticky='w')

    # Create labels for color explanations
    red_label = tk.Label(color_code_frame, text="Red: High Similarity", fg='red')
    red_label.grid(column=0, row=0, padx=10, pady=5, sticky='w')

    yellow_label = tk.Label(color_code_frame, text="Yellow: Medium Similarity", fg='dark orange')
    yellow_label.grid(column=1, row=0, padx=10, pady=5, sticky='w')

    # Create a ScrolledText widget for displaying the highlighted text
    highlighted_text_widget = scrolledtext.ScrolledText(window, width=50, height=10)
    highlighted_text_widget.grid(column=0, row=7, columnspan=2)

    for i, sentence in enumerate(sentences_to_highlight):
        max_similarity_index = torch.argmax(cosine_similarities[i])
        max_similarity = cosine_similarities[i][max_similarity_index].item()

        if max_similarity >= 0.9:  # High similarity threshold
            # Highlight in red
            highlighted_text_widget.insert(tk.END, sentence, 'highlighted_high')
        elif 0.75 <= max_similarity < 0.9:  # Medium similarity threshold
            # Highlight in yellow
            highlighted_text_widget.insert(tk.END, sentence, 'highlighted_medium')
        else:
            # No highlight for low similarity
            highlighted_text_widget.insert(tk.END, sentence)

        if i < len(sentences_to_highlight) - 1:
            highlighted_text_widget.insert(tk.END, '\n')

    # Configure the 'highlighted_high' tag with a red background
    highlighted_text_widget.tag_configure('highlighted_high', background='red')
    # Configure the 'highlighted_medium' tag with a yellow background
    highlighted_text_widget.tag_configure('highlighted_medium', background='yellow')

    return highlighted_text_widget

# Create a GUI window
window = tk.Tk()
window.title("Plagiarism Detection")

# Create a frame for the content
content_frame = tk.Frame(window)
content_frame.grid(column=0, row=0, padx=20, pady=20)

# Create labels for Text 1 and Text 2
text_area1_label = tk.Label(content_frame, text="Original Text:")
text_area1_label.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)

text_area2_label = tk.Label(content_frame, text="Submitted Text:")
text_area2_label.grid(column=1, row=0, padx=10, pady=5, sticky=tk.W)

# Create two text areas for input texts
text_area1 = scrolledtext.ScrolledText(content_frame, width=50, height=10)
text_area1.grid(column=0, row=1, padx=10, pady=5, sticky='w')

text_area2 = scrolledtext.ScrolledText(content_frame, width=50, height=10)
text_area2.grid(column=1, row=1, padx=10, pady=5, sticky='w')

# Create a button to trigger the plagiarism detection function
button = tk.Button(content_frame, text="Detect Plagiarism", command=detect_plagiarism)
button.grid(column=0, row=2, columnspan=2, pady=10)

# Create a label to display the similarity score
similarity_score_label = tk.Label(content_frame, text="", font=("Arial", 12))
similarity_score_label.grid(column=0, row=3, columnspan=2, pady=5)

window.mainloop()