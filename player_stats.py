from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog

player = players.find_players_by_full_name("LeBron James")[0]
log = playergamelog.PlayerGameLog(player_id=player["id"], season="2025-26")
df = log.get_data_frames()[0]

print(player["full_name"], "- last 10 games")
print(df[["GAME_DATE", "MATCHUP", "PTS", "REB", "AST"]].head(10))
