"""
Count Vectors can be helpful in understanding the type of text by the frequency of words in it. But its major disadvantages are:
Its inability in identifying more important and less important words for analysis.
It will just consider words that are abundant in a corpus as the most statistically significant word.
It also doesn't identify the relationships between words such as linguistic similarity between words.
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import numpy as np

# Path to the folder containing CVs (resumes)
cv_folder = "C:\\Users\\syssp\\OneDrive\\Desktop\\GoogleDrivePro\\Work\\VSCode\\DocumentSimilarity\\Big_data_raw\\mini_clean_cv"

# Path to the folder containing job descriptions (jds)
jd_folder = "C:\\Users\\syssp\\OneDrive\\Desktop\\GoogleDrivePro\\Work\\VSCode\\DocumentSimilarity\\Big_data_raw\\mini_clean_jd"

# Define a CountVectorizer with appropriate settings
count_vectorizer = CountVectorizer(lowercase=True, stop_words='english')

# Lists to store CV and job description texts
cv_texts = []
jd_texts = []

# Load CVs
for filename in os.listdir(cv_folder):
    if filename.endswith(".txt"):
        cv_path = os.path.join(cv_folder, filename)
        with open(cv_path, 'r', encoding='utf-8') as cv_file:
            cv_text = cv_file.read()
        cv_texts.append(cv_text)

# Load job descriptions (jds)
for filename in os.listdir(jd_folder):
    if filename.endswith(".txt"):
        jd_path = os.path.join(jd_folder, filename)
        with open(jd_path, 'r', encoding='utf-8') as jd_file:
            jd_text = jd_file.read()
        jd_texts.append(jd_text)

# Fit and transform the CV and job description texts to Count vectors
cv_count_vectors = count_vectorizer.fit_transform(cv_texts)
jd_count_vectors = count_vectorizer.transform(jd_texts)

# Calculate cosine similarity between each CV's Count vector and job descriptions' Count vectors
for cv_idx, cv_count_vector in enumerate(cv_count_vectors):
    similarity_scores = cosine_similarity(cv_count_vector, jd_count_vectors)
    print(f"CV {cv_idx+1} Similarity Scores:")
    for jd_idx, score in enumerate(similarity_scores[0]):
        print(f"  Job Description {jd_idx+1}: {score}")
