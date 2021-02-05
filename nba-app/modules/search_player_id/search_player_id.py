from nba_api.stats.static import players

player_dict = players.get_players()

player = [player for player in player_dict if player['full_name'] == 'Malcolm Brogdon'][0]
player_id = player['id']

print(player_id)
print('successfully found ID')