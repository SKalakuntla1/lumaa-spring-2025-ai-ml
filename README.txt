MOVIE RECOMMENDATION SYSTEM
==========================

A simple system that recommends movies based on your text queries.

DATASET
-------
- Uses Kaggle Movies Dataset (https://www.kaggle.com/datasets/harshshinde8/movies-csv)
- Creates a cleaned subset of 500 movies automatically
- Uses movie titles, genres, and plot overviews

SETUP
-----
1. Create virtual environment:
   Windows:
   > python -m venv venv
   > venv\Scripts\activate

   Mac/Linux:
   $ python3 -m venv venv
   $ source venv/bin/activate

2. Install required packages:
   > pip install -r requirements.txt

RUNNING
-------
1. Run the program:
   > python Reccomdation.py

2. Enter your query when prompted
   Example queries:
   - "action movies with superheroes"
   - "romantic comedy"
   - "sci-fi space"

EXAMPLE OUTPUT
-------------
Enter Query: action adventure with dragons

Top Recommendations:
                        original_title  similarity
1              How to Train Your Dragon   0.876
2              The Hobbit               0.745
3              Eragon                   0.723
4              DragonHeart             0.698
5              Reign of Fire           0.654

FILES
-----
Reccomdation.py      - Main program
movies_subset_500.csv - Movie dataset (created on first run)
requirements.txt      - Required Python packages 