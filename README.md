# Movie-recommender
My first GitHub project

This project aims to build a movie recommender machine learning system. It takes in movies you have watched and liked, addresses any comments you have on them, and then returns a movie you may like but have not watched yet.

The first part of this project that I have been working on is sentiment analysis of movie reviews. It utilizes data provided by Kaggle and the bag-of-words technique to analyze the meaning of words, determining whether they are positive or negative. 
All that is left for this part is to fully integrate my code into a class and get this class working, and then explore the use of an n-grams technique to analyze multiple words simultaneously. This should give me a higher cross-validation score. 

From experimenting on Jupyter Notebook, n-grams do not improve the cross-validation score, so for now I will stick to just a bag of words. I am looking into lemmatization, which might speed up the logistic regression by decreasing the number of items in the matrix. 

The next part is going to be some sort of grading system put together, so it can link it to a possible movie you might like. There is still a lot of work that needs to go into this part. I am looking into using a content-based recommendation system for this one 
