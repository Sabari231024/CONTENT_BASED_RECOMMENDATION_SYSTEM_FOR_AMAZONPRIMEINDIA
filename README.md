# CONTENT_BASED_RECOMMENDATION_SYSTEM_FOR_AMAZONPRIMEINDIA

**Overview:**

This repository contains code for a movie recommendation system implemented using content-based filtering with k-nearest neighbors (k-NN) algorithm. The recommendation system suggests similar movies to users based on the features of movies they have previously watched.

**Dataset:**
The dataset used for this recommendation system contains information about various movies, including their genres, moods, content advisory, audio languages, subtitles, directors, producers, starring actors, studio, and runtime. Additionally, the dataset includes IMDb ratings for each movie. This dataset is taken from kaggle Amazonprime india shows/movies.

**Features:**
Genre: The genre(s) of the movie.
Moods: The mood(s) associated with the movie.
Content Advisory: Advisory information about the content of the movie (e.g., PG-13, R, etc.).
Audio Languages: Languages available for audio in the movie.
Subtitles: Languages available for subtitles in the movie.
Directors: Director(s) of the movie.
Producers: Producer(s) of the movie.
Starring: Actors starring in the movie.
Studio: Studio producing the movie.
Runtime: Duration of the movie in minutes.
IMDb Rating: Rating of the movie on IMDb.

**Implementation:**
The recommendation system is implemented using Python and utilizes the scikit-learn library for preprocessing and k-NN modeling. The code preprocesses the dataset, transforms features using standardization and one-hot encoding, builds a k-NN model, and suggests similar movies based on user input. Data cleaning and preprocessing was done inorder to fill the missing data in IMDB rating . webscrapping was done using the tool PymovieDb and then that code was implemented through batch processing , which is done in addon_imdb_rating.


