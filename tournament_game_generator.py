def get_number_of_teams():

    while True:
        num_teams = int(input("Enter the number of teams in the tournament: "))

        if num_teams % 2 != 0:
            print("The number of teams has to be even, try again.")

        if num_teams < 2:
            print("The minimum number of teams is 2, try again.")

        if num_teams >= 2 and num_teams % 2 == 0:
            break

    return num_teams


def get_team_names(num_teams):
    team_names = []
    for num in range(1, num_teams + 1):
        while True:
            team_name = input(f"Enter the name for team #{num}: ")
            if len(team_name) < 2:
                print("Team names must have at least 2 characters, try again.")
            elif len(team_name.split()) >= 3:
                print("Team names may have at most 2 words, try again.")
            else:
                break
        team_names.append(team_name)
    return team_names


def get_number_of_games_played(num_teams):
    while True:
        games_played = int(
            input("Enter the number of games played by each team: "))
        if games_played >= num_teams - 1:
            break
        else:
            print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
    return games_played


def get_team_wins(team_names, games_played):
    team_wins = []
    for i in range(len(team_names)):
        while True:
            num_wins_each = int(
                input(f"Enter the number of wins Team {team_names[i]} had: "))
            if num_wins_each < 0:
                print("The minimum number of wins is 0, try again.")
            if num_wins_each > games_played:
                print(
                    f"The maximum number of wins is {games_played}, try again.")
            else:
                break
        team_wins.append((team_names[i], num_wins_each))
    return team_wins


num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)
# print(team_wins)

print("Generating the games to be played in the first round of the tournament...")

wins_in_order = sorted(team_wins, key=lambda x: x[1])
# print(wins_in_order)

team_pairing = []
for i in range(len(wins_in_order)//2):
    home_team = wins_in_order[i][0]
    away_team = wins_in_order[(-i) - 1][0]
    team_pairing.append((home_team, away_team))

# print(team_pairing)
for home_team, away_team in team_pairing:
    print(f"Home: {home_team} VS Away: {away_team}")
