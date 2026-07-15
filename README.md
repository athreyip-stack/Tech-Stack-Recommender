Tech Stack Recommender using TF-IDF and Cosine Similarity

Overview

The **Tech Stack Recommender** is a simple machine learning project that recommends suitable career paths based on a user's technical skills. Users enter their skills, and the system compares them with predefined job profiles using **TF-IDF Vectorization** and **Cosine Similarity** to recommend the top matching career options.


Features

* Accepts user skills as input.
* Uses **TF-IDF** to convert text into numerical vectors.
* Calculates similarity using **Cosine Similarity**.
* Recommends the **Top 3** matching career paths.
* Simple command-line interface.


Technologies Used

* Python 3
* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity


Project Structure

Tech-Stack-Recommender/
│── recommender.py
│── README.md

How to Run

Run the Python file:

```bash
python recommender.py
```

Enter your skills when prompted.

Example Input

```
Python, Machine Learning, SQL
```

Example Output

```
Top 3 Recommended Career Paths

Data Scientist      --> Match Score: 0.82
AI Engineer         --> Match Score: 0.74
Backend Developer   --> Match Score: 0.51
```

How It Works

1. User enters at least three technical skills.
2. Job profiles are stored with their required skills.
3. TF-IDF converts skills into feature vectors.
4. Cosine Similarity compares the user profile with each job profile.
5. The system ranks the similarity scores.
6. The top three matching careers are displayed.

---

Algorithm

* Input Skills
* TF-IDF Vectorization
* Cosine Similarity Calculation
* Score Ranking
* Top 3 Career Recommendations

---

Future Enhancements

* Add a larger dataset of job roles.
* Build a web interface using Flask or Streamlit.
* Integrate real-time job data from APIs.
* Provide personalized learning resources based on missing skills.

---
 three career recommendations with the highest match scores.
