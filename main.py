from bs4 import BeautifulSoup
import requests
import pandas as pd

#setting dataframe print settings to max
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

#setting up test parameters
years = ["2013", "2014", "2015", "2016", "2017", "2018", "2019"]
positions = ["QB", "RB", "WR", "TE"]
output_dicts={}

#importing raw draft data
draft_data_raw = pd.read_csv("Historic Draft Picks.csv", header = 1)

#manipulating draft data
draft_data = draft_data_raw.filter(["Year", "Rnd", "Pick", "Player", "Pos","Tm"], axis = 1)
draft_data["Player"] = draft_data["Player"].str[:-9]

#import performance data
#for position in positions:
    #for year in years:
        #df = pd.read_csv(position+year+".csv", header = 1)
        #df = df.filter(["Rk", "Player"], axis = 1)
        #df["Player"] = df["Player"].str[:-9]

        #player = df["Player"].tolist()
        #rank = df["Rk"].tolist()

        #output_dicts[position+year] = dict(zip(player, rank))

#print(output_dicts)

#Building new df columns
#Below code generates a list of all players I have performance stats for
complete_player_performance_names = []
for position in positions:
    for year in years:
        df = pd.read_csv(position + year + ".csv", header=1)
        df = df.filter(["Rk", "Player"], axis=1)
        df["Player"] = df["Player"].str[:-9]

        players = df["Player"].tolist()
        rank = df["Rk"].tolist()

        for player in players:
            if player not in complete_player_performance_names:
                complete_player_performance_names.append(player)
print(complete_player_performance_names)

draft_data[year] = draft_data["Player"].map(dictionary of performance)

player_ranks=[]