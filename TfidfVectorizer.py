"""

TF-IDF is better than Count Vectorizers because it not only focuses on the frequency of words present in the corpus but also provides the importance of the words. 
We can then remove the words that are less important for analysis, hence making the model building less complex by reducing the input dimensions.
Even though TFIDF can provide a good understanding about the importance of words but just like Count Vectors, its disadvantage is:
It fails to provide linguistic information about the words such as the real meaning of the words, similarity with other words etc.
To train a model on the actual linguistic relationship of the words, there are two other word embedding techniques widely used in NLP, they are "word2vec" and "Glove".
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import numpy as np

# Path to the folder containing CVs (resumes)
cv_folder = "C:\\Users\\syssp\\OneDrive\\Desktop\\GoogleDrivePro\\Work\\VSCode\\DocumentSimilarity\\Big_data_raw\\mini_clean_cv"

# Path to the folder containing job descriptions (jds)
jd_folder = "C:\\Users\\syssp\\OneDrive\\Desktop\\GoogleDrivePro\\Work\\VSCode\\DocumentSimilarity\\Big_data_raw\\mini_clean_jd"

# Define a TF-IDF vectorizer with appropriate settings
tfidf_vectorizer = TfidfVectorizer(lowercase=True, stop_words='english')

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

# Fit and transform the CV and job description texts to TF-IDF vectors
cv_tfidf_vectors = tfidf_vectorizer.fit_transform(cv_texts)
jd_tfidf_vectors = tfidf_vectorizer.transform(jd_texts)

# Calculate cosine similarity between each CV's TF-IDF vector and job descriptions' TF-IDF vectors
for cv_idx, cv_tfidf_vector in enumerate(cv_tfidf_vectors):
    similarity_scores = cosine_similarity(cv_tfidf_vector, jd_tfidf_vectors)
    print(f"CV {cv_idx+1} Similarity Scores:")
    for jd_idx, score in enumerate(similarity_scores[0]):
        print(f"  Job Description {jd_idx+1}: {score}")
