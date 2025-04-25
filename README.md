
# 🎬 Movie Recommendation System

This project is a simple movie recommendation system using collaborative filtering on the [MovieLens 100k Dataset](https://grouplens.org/datasets/movielens/100k/).

## 🚀 Features
- Recommend similar movies based on a selected movie
- Uses Pearson correlation for collaborative filtering
- Filters recommendations by popularity (min 100 ratings)

## 🛠️ Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download and unzip the MovieLens 100k dataset:  
   [https://grouplens.org/datasets/movielens/100k/](https://grouplens.org/datasets/movielens/100k/)  
   Place `u.data` and `u.item` inside the `data/` folder.

4. Run the script:
```bash
python movie_recommender.py
```

## ✅ Example

```
Enter a movie title (e.g., Star Wars (1977)):
```

## 📦 Dependencies
- pandas
- numpy
- scikit-learn

## 🧠 To Do
- Add Streamlit web interface
- Improve filtering options
- Deploy online
