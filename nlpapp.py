#import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import nltk
import textblob
from textblob import TextBlob
from nltk import ngrams
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from gensim.summarization import summarize
from summa.summarizer import summarize

#main script
def main():
  #creat text box where user will write text to be analysed and extract meaningful information 
  word = st.text_area("Enter text ", height = 120)
  text = TextBlob(word)
