import soccerdata as sd

whoscored = sd.WhoScored(leagues="ENG-Premier League", seasons=2021)

epl_schedule = whoscored.read_schedule()
print(epl_schedule.head())

missing_players = whoscored.read_missing_players(match_id=1485184)
print(missing_players.head())
