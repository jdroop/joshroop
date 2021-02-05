from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
import pandas as pd 

#Call the API endpoint passing in lebron's ID & which season 
gamelog = playergamelog.PlayerGameLog(player_id='1627763', season = '2020')
gamelogAll = playergamelog.PlayerGameLog(player_id='1627763', season = SeasonAll.all)
#Converts gamelog object into a pandas dataframe
#can also convert to JSON or dictionary  
df = gamelogAll.get_data_frames()
print(df)


# # If you want all seasons, you must import the SeasonAll parameter 
# from nba_api.stats.library.parameters import SeasonAll

# gamelog_bron_all = playergamelog.PlayerGameLog(player_id='2544', season = SeasonAll.all)

# df_bron_games_all = gamelog_bron_all.get_data_frames()
