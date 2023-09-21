# Plagiarism Detection Tool

This is a Python program that allows you to detect plagiarism in text documents using cosine similarity of sentence embeddings. The program utilizes the Sentence Transformers library to calculate the similarity between two text documents and highlights plagiarized sections with different colors based on the similarity score.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed.
- Required Python libraries installed. You can install them using `pip`:

  ```shell
  pip install sentence-transformers torch tkinter
## Technologies Used

- **Python:** The program is written in Python, making use of various libraries and modules for text processing and user interface development.
- **Sentence Transformers:** Sentence Transformers is a Python library that provides pre-trained models for generating sentence embeddings. It is used to calculate the similarity between text documents.
- **Tkinter:** Tkinter is a standard Python interface to the Tk GUI toolkit and is used to create the graphical user interface (GUI) for this tool.
## Usage
1.) Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/plagiarism-detection.git
```
2.) Navigate to the project directory:
```bash
cd plagiarism-detection
```
3.) Run the plagiarism detection tool:
```bash
python plagiarism_detection.py
```
4.) The GUI window will appear, allowing you to enter the original text and the submitted text for comparison.

5.) Click the "Detect Plagiarism" button to calculate the similarity score and highlight plagiarized sections in the submitted text.

6.) The program will display the similarity score and highlight plagiarized sections in the submitted text with different colors.

## Purpose

The Plagiarism Detection Tool serves the following purposes:

- **Plagiarism Detection:** The primary purpose of this tool is to detect plagiarism in text documents. It calculates the cosine similarity between two text documents and highlights plagiarized sections based on the similarity score.

- **Academic Integrity:** This tool can be especially useful in an academic context, where educators can use it to check for plagiarism in student assignments, research papers, and essays, ensuring academic integrity.

- **Content Validation:** Content creators and publishers can use this tool to verify the originality of submitted content, ensuring that it does not infringe upon copyright or contain plagiarized material.

- **Educational Tool:** It can be used as an educational tool to teach students about plagiarism, similarity scores, and the importance of originality in writing.

- **User-Friendly Interface:** The graphical user interface (GUI) makes it easy for users to input text documents, initiate the plagiarism detection process, and visualize the results with highlighted plagiarized sections.

- **Customization:** Users can adjust the similarity thresholds to define what constitutes high, medium, and low similarity, allowing for flexibility in plagiarism detection criteria.
