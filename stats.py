def calculate_kda(kills, deaths, assists):
    if deaths == 0:
        return kills + assists
    else:
        return (kills + assists) / deaths

def calculate_cs_per_min(cs, game_minutes):
    if game_minutes <= 0:
        return 0.0
    if cs == 0:
        return 0.0
    return cs / game_minutes

def winrate(matches_list):
    if not matches_list:
        return 0.0
    wins = 0
    for match in matches_list:
        if match["win"]:
            wins += 1
    winrate = wins / len(matches_list) * 100
    return round(winrate, 1)

def avg_cs(matches_list):
    if not matches_list:
        return 0.0
    cs_per_minute_total = 0
    for match in matches_list:
        cs_per_minute_total += calculate_cs_per_min(match["cs"], match["game_minutes"])
    cs_per_minute_avg = cs_per_minute_total / len(matches_list)
    return round(cs_per_minute_avg, 1)

def avg_kda(matches_list):
    if not matches_list:
        return 0.0
    total_kda = 0
    for match in matches_list:
        total_kda += calculate_kda(match["kills"], match["deaths"], match["assists"])
    average_kda = total_kda / len(matches_list)
    return average_kda

def avg_vision_score(matches_list):
    if not matches_list:
        return 0.0
    total_vision_score = 0
    for match in matches_list:
        total_vision_score += match["vision_score"]
    return round(total_vision_score / len(matches_list), 1)

def find_best_champ(matches_list):
    if not matches_list:
        return ""
    best_champ = ""
    best_kda = 0
    for match in matches_list:
        current_kda = calculate_kda(match["kills"], match["deaths"], match["assists"])
        if current_kda > best_kda:
            best_kda = current_kda
            best_champ = match["champion"]
    return best_champ
