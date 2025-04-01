import soccerdata as sd

espn = sd.ESPN(leagues = "ENG-Premier League", seasons = 2021)

# Game schedule
epl_schedule = espn.read_schedule()
print(epl_schedule.head())

# Match sheet data
match_sheet = espn.read_matchsheet(match_id=541465)
print(match_sheet.head())

# Line ups
lineups = espn.read_lineup(match_id=541465)
print(lineups.head())