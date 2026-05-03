import data

def calculate_kda(kills, deaths, assists):
    if deaths == 0:
        return kills + assists
    else:
        return (kills + assists) / deaths

def calculate_cs_per_min(cs, game_minutes):
    if cs == 0:
        return 0.0
    else:
        return cs/game_minutes

def winrate(matches_list):
    wins = 0
    for match in matches_list:
        if match["win"] == "True":
            wins +=1
    winrate = wins/len(matches_list) * 100
    return round(winrate,1)

def avg_cs(matches_list):
    cs_per_minute_total = 0
    for match in matches_list:
        cs_per_minute_total += calculate_cs_per_min(match["cs"], match["game_minutes"])
    cs_per_minute_avg = cs_per_minute_total/len(matches_list) 
    return round(cs_per_minute_avg,1)

def avg_kda(matches_list):
    total_kda = 0
    for match in matches_list:
        total_kda += calculate_kda(match["kills"], match["deaths"], match["assists"])
    average_kda = total_kda/ len(matches_list)
    return average_kda

def find_best_champ(matches_list):
    best_champ = ""
    best_kda = 0
    for match in matches_list:
        current_kda = calculate_kda(match["kills"], match["deaths"], match["assists"])
        if current_kda > best_kda:
            best_kda = current_kda
            best_champ = match["champion"]
    return best_champ


print(
    f"RiftCoach Match Review\n"
    "========================\n"
    f"Games Analysed: {len(data.matches)}\n"
    f"Win rate: {winrate(data.matches)}\n"
    f"Average KDA: {avg_kda(data.matches)}\n"
    f"Average CS per min: {avg_cs(data.matches)}\n"
    f"Best Champion: {find_best_champ(data.matches)}"
)

if avg_kda(data.matches) < 3:
    print("Overall focus: play safer and reduce deaths")
elif avg_cs(data.matches) < 6:
    print("Overall focus: improve farming")
else:
    print("Overall focus: good overall performance")

print("=============================")

for match in data.matches:
    cs_per_minute = calculate_cs_per_min(match["cs"], match["game_minutes"])
    kda = calculate_kda(match["kills"], match["deaths"], match["assists"])

    print(
    f"Champion: {match['champion']}\n"
    f"KDA: {kda}\n"
    f"CS/min: {cs_per_minute}\n"
    "Feedback:"
    )

    if kda > 3:
        print("Good fighting performance.")
    else: 
        print("Try to die less")
    
    if cs_per_minute > 7:
        print("You are cs-ing pretty well this game")
    else:
        print("Try to last hit well!")
    
    print("---------------------------------------")


print()