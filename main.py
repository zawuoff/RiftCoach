import data, stats

print(
    "\n"
    f"RiftCoach Match Review\n"
    "========================\n"
    f"Games Analysed: {len(data.matches)}\n"
    f"Win rate: {stats.winrate(data.matches)}\n"
    f"Average KDA: {stats.avg_kda(data.matches)}\n"
    f"Average CS per min: {stats.avg_cs(data.matches)}\n"
    f"Best Champion: {stats.find_best_champ(data.matches)}"
)

if stats.avg_kda(data.matches) < 3:
    print("Overall focus: play safer and reduce deaths")
elif stats.avg_cs(data.matches) < 6:
    print("Overall focus: improve farming")
else:
    print("Overall focus: good overall performance")

print("=============================")

for match in data.matches:
    cs_per_minute = stats.calculate_cs_per_min(match["cs"], match["game_minutes"])
    kda = stats.calculate_kda(match["kills"], match["deaths"], match["assists"])

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
