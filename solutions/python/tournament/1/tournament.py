def tally(rows):
    
    table = {}

    
    for row in rows:

        team1, team2, result = row.split(';')

        
        if team1 not in table:
            table[team1] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}

        if team2 not in table:
            table[team2] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}

    
        table[team1]["MP"] += 1
        table[team2]["MP"] += 1

        
        if result == "win":
            table[team1]["W"] += 1
            table[team1]["P"] += 3

            table[team2]["L"] += 1

        elif result == "loss":
            table[team2]["W"] += 1
            table[team2]["P"] += 3

            table[team1]["L"] += 1

        elif result == "draw":
            table[team1]["D"] += 1
            table[team2]["D"] += 1

            table[team1]["P"] += 1
            table[team2]["P"] += 1

    sorted_teams = sorted(
        table.items(),
        key=lambda item: (-item[1]["P"], item[0])
    )

    
    header = "Team                           | MP |  W |  D |  L |  P"
    lines = [header]

    for team, stats in sorted_teams:
        line = (
            f"{team:<31}| "
            f"{stats['MP']:>2} | "
            f"{stats['W']:>2} | "
            f"{stats['D']:>2} | "
            f"{stats['L']:>2} | "
            f"{stats['P']:>2}"
        )
        lines.append(line)

    return lines

