# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built with **Python**, **Streamlit**, **Pandas**, and **Scikit-learn**. The application recommends movies similar to a selected movie using cosine similarity and displays movie posters fetched dynamically from the TMDB API.

---

## 🚀 Features

* 🎥 Content-based movie recommendation
* 🔍 Search and select movies from a dropdown
* ⭐ Top 5 similar movie recommendations
* 🖼️ Dynamic movie posters using the TMDB API
* ⚡ Fast recommendation using a precomputed similarity matrix
* 💻 Interactive web interface built with Streamlit

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Requests
* Pickle
* TMDB API

---

## 📂 Project Structure

```
Movie-Recommendation-System/
│
├── app.py                     # Streamlit application
├── movie-recommender.ipynb    # Data preprocessing and model creation
├── movie_dict.pkl             # Movie metadata
├── movies.pkl                 # Original processed dataset
├── similarity.pkl             # Cosine similarity matrix
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
├── .gitignore
├── Procfile
└── setup.sh
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Movie-Recommendation-System.git
```

### 2. Navigate to the project folder

```bash
cd Movie-Recommendation-System
```

### 3. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser.

---

## 🧠 How It Works

1. Load the movie dataset.
2. Preprocess movie metadata.
3. Create feature tags by combining relevant movie information.
4. Convert text into vectors.
5. Compute cosine similarity between all movies.
6. When a user selects a movie, retrieve the five most similar movies.
7. Fetch movie posters from the TMDB API.
8. Display recommendations in the Streamlit interface.

---

## 📸 Screenshots

You can add screenshots of your application inside a `screenshots/` folder.

Example:

```
screenshots/
├── home.png
├── recommendations.png
```

Then include them in the README:

```markdown
![Home](screenshots/home.png)

![Recommendations](screenshots/recommendations.png)
```

---

## 🔑 TMDB API

Movie posters are retrieved using **The Movie Database (TMDB) API**.

To use your own API key:

1. Create an account on TMDB.
2. Generate an API key.
3. Replace the API key inside `app.py`.

---

## 📌 Future Improvements

* Movie search with autocomplete
* Movie ratings and genres
* Release year display
* Trailer integration
* IMDb links
* User authentication
* Hybrid recommendation system
* Responsive UI improvements
* Recommendation history

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## 📄 License

This project is created for educational and portfolio purposes.

---

## 👨‍💻 Author

**Mahesh Pharswan**

GitHub: https://github.com/YOUR_USERNAME

---

⭐ If you found this project useful, consider giving it a star on GitHub!
