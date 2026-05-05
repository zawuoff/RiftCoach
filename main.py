import data, stats

def get_kda(kda):
    if kda >= 3:
        return "Good fighting performance."
    else:
        return "Try to die less"

def get_cs_per_min(cs):
    if cs >= 7:
        return "You are cs-ing pretty well this game"
    else:
        return "Try to last hit well!"

def print_overall_summary():
    print(
        "\n"
        f"RiftCoach Match Review\n"
        "========================\n"
        f"Games Analysed: {len(data.matches)}\n"
        f"Win rate: {stats.winrate(data.matches)}\n"
        f"Average KDA: {stats.avg_kda(data.matches)}\n"
        f"Average CS per min: {stats.avg_cs(data.matches)}\n"
        f"Average Vision Score: {stats.avg_vision_score(data.matches)}\n"
        f"Best Champion: {stats.find_best_champ(data.matches)}"
    )

    if stats.avg_kda(data.matches) <= 3:
        print("Overall focus: play safer and reduce deaths")
    elif stats.avg_cs(data.matches) <= 6:
        print("Overall focus: improve farming")
    elif stats.avg_vision_score(data.matches) <= 25:
        print("Overall focus: improve warding")
    else:
        print("Overall focus: good overall performance")

    print("=============================")


def print_match_review(matches):
        cs_per_minute = stats.calculate_cs_per_min(matches["cs"], matches["game_minutes"])
        kda = stats.calculate_kda(matches["kills"], matches["deaths"], matches["assists"])

        print(
        f"Champion: {matches['champion']}\n"
        f"KDA: {kda}\n"
        f"CS/min: {cs_per_minute}\n"
        "Feedback:"
        )
        print(get_kda(kda))
        print(get_cs_per_min(cs_per_minute))
        print("---------------------------------------")
    

def print_individual_summary(matches):
    for match in matches:
        print_match_review(match)

def main():
    print_overall_summary()
    print_individual_summary(data.matches)
    

main()