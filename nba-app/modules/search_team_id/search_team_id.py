from nba_api.stats.static import teams 

teams = teams.get_teams()
IND = [x for x in teams if x['full_name'] == 'Indiana Pacers'][0]
IND_id = IND['id']

print(IND_id)
print('Successfully found ID')