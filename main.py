from bs4 import BeautifulSoup
import requests
import pandas as pd

#setting dataframe print settings to max
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

#setting up test parameters
years = ["2013", "2014", "2015", "2016", "2017"]
positions = ["QB", "rb", "wr", "te"]

#importing raw draft data
draft_data_raw = pd.read_csv("Historic Draft Picks.csv", header = None)

#manipulating draft data
