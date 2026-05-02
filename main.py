import data

def calculate_kda(kills, deaths, assists):
    if deaths == 0:
        return kills + assists
    else:
        return (kills + assists) / deaths

def calculate_cs_per_min(cs, game_minutes):
    if cs == 0:
        return "0 CS"
    else:
        return cs/game_minutes

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
