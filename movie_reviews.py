import opendatasets as od
import pandas as pd
import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

class MovieReviews:
    def __init__ (self, ratings):
        self.rating=ratings
        
        #This will split our data for training with 75% of it for training and 25% of it for testing
        self.review_train, self.review_test, self.sentiment_train, self.sentiment_test= train_test_split(self.rating['review'],self.rating['sentiment'],random_state=0)
        
        #creates the tool vect and then fits our training data to 
        #min_df deletes words not in 5 data sets this removes miss spellings and things that may not be in our test set
        self.vect= CountVectorizer(min_df=5, stop_words="english").fit(self.review_train)
        self.ReviewsTrain=self.vect.transform(self.review_train)
        
    def log_grid(self):
        self.Log=LogisticRegression(max_iter=200, solver='saga',verbose=0)

        #scores=cross_val_score(Log, ReviewsTrain, sentiment_train, cv=5)\
        #testing for the best C parameter for LogReg small C is normally better for normal data with alot of useless characters
        # with stop words C=0.1 is the best
        self.parameters= {'C':[0.001, 0.01, 0.1, 1,10]}
        self.grid=GridSearchCV(self.Log, self.parameters, cv=5)
        self.grid.fit(self.ReviewsTrain,self.sentiment_train)
        print("The best score is ",self.grid.best_score_)
        print("The best parameter is ",self.grid.best_params_)

        #transform our test set so it fits the needed dimensions of the matrix for an accurate prediction
        self.X_test=self.vect.transform(self.review_test)
        print("The test score is ",self.grid.score(self.X_test,self.sentiment_test))
                
    def input(self, input):
        #transform our test set so it fits the needed dimensions of the matrix for an accurate prediction
        self.transform=self.vect.transform([input])

        #predicts whether the word is a positive or negative sentiment. 
        self.prediction=self.grid.predict(self.transform)
        return self.prediction 


print('now im doing something')