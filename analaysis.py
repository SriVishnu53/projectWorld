# Importing necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Streamlit app function
def app():
    # Check if the user is logged in
    if st.session_state.username != '':
        user_text = st.text_input('Enter Text content', max_chars=860)

        model_results = st.container()
        sentiment_analysis = st.container()

        with model_results:
            st.subheader('Prediction:')
            if user_text:
                user_text = re.sub('[%s]' % re.escape(string.punctuation), '', user_text)

                # tokenizing
                stop_words = list(stopwords.words('english'))
                tokens = nltk.word_tokenize(user_text)

                # removing stop words
                stopwords_removed = [token.lower() for token in tokens if token.lower() not in stop_words]

                # taking root word
                lemmatizer = WordNetLemmatizer()
                lemmatized_output = [lemmatizer.lemmatize(word) for word in stopwords_removed]

                # instantiating count vectorizor
                count = CountVectorizer(stop_words=stop_words)
                X_train = pickle.load(open(r'D:\Project code\Sentiment Analysis For Hate Speech Detection Using Machine Learning And Deep Learning With StreamLit Frame work\Source code\pickle/X_train_2.pkl', 'rb'))
                X_test = lemmatized_output
                X_train_count = count.fit_transform(X_train)
                X_test_count = count.transform(X_test)

                # loading in model
                final_model = pickle.load(open(r'D:\Project code\Sentiment Analysis For Hate Speech Detection Using Machine Learning And Deep Learning With StreamLit Frame work\Source code\pickle/final_log_reg_count_model.pkl', 'rb'))

                # apply model to make predictions
                prediction = final_model.predict(X_test_count[0])

                # Display prediction result
                if prediction == 0:
                    st.subheader('**Not Hate Speech**')
                else:
                    st.subheader('**Hate Speech**')
                st.text('')

        with sentiment_analysis:
            if user_text:
                analyzer = SentimentIntensityAnalyzer()
                sentiment_dict = analyzer.polarity_scores(user_text)

                if sentiment_dict['compound'] >= 0.05:
                    category = ("**Positive ✅**")
                elif sentiment_dict['compound'] <= -0.05:
                    category = ("**Negative 🚫**")
                else:
                    category = ("**Neutral ☑️**")

                # score breakdown section with columns
                breakdown, graph = st.columns(2)

                with breakdown:
                    st.write("Your text content is rated as", category)
                    st.write("**Compound Score**: ", sentiment_dict['compound'])
                    st.write("**Polarity Breakdown:**")
                    st.write(sentiment_dict['neg'] * 100, "% Negative")
                    st.write(sentiment_dict['neu'] * 100, "% Neutral")
                    st.write(sentiment_dict['pos'] * 100, "% Positive")

                with graph:
                    sentiment_graph = pd.DataFrame.from_dict(sentiment_dict, orient='index').drop(['compound'])
                    st.bar_chart(sentiment_graph)

    else:
         st.text("Please log in first to access the page")