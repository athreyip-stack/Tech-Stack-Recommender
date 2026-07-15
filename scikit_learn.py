from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Dataset of job roles and required skills
jobs = {
    "Data Scientist": "Python SQL Machine Learning Data Analysis Statistics",
    "Backend Developer": "Java Python SQL APIs Database",
    "DevOps Engineer": "AWS Docker Kubernetes CI/CD Linux Git",
    "Cloud Engineer": "AWS Cloud Computing Docker Kubernetes Linux",
    "AI Engineer": "Python Machine Learning Deep Learning TensorFlow NLP",
    "Web Developer": "HTML CSS JavaScript React NodeJS"
}

# Take user skills as input
print("Enter at least 3 skills:")
user_skills = input("Skills (comma separated): ")

# Convert input into text format
user_profile = " ".join([skill.strip() for skill in user_skills.split(",")])

# Combine job descriptions and user profile
documents = list(jobs.values()) + [user_profile]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# User vector (last row)
user_vector = tfidf_matrix[-1]

# Job vectors
job_vectors = tfidf_matrix[:-1]

# Calculate cosine similarity
scores = cosine_similarity(user_vector, job_vectors).flatten()

# Rank jobs
results = list(zip(jobs.keys(), scores))
results.sort(key=lambda x: x[1], reverse=True)

# Display Top 3 Recommendations
print("\nTop 3 Recommended Career Paths:")
for role, score in results[:3]:
    print(f"{role} --> Match Score: {score:.2f}")
