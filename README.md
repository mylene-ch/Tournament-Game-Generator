# Tournament Game Scheduler

## Introduction
This project is a Python program designed to schedule games for the first round of an end-of-year tournament. The program ensures that teams with the most regular-season wins are paired with teams with the least wins, following specific rules and constraints. It takes user input for team details, validates the input, and outputs the game schedule.

---

## Features
- Input and validation of:
  - Number of teams (even and minimum of 2).
  - Team names (2-characters minimum, up to 2 words).
  - Number of games played (minimum to cover all matchups).
  - Wins for each team (between 0 and total games played).
- Game scheduling based on regular-season performance.
- User-friendly prompts and error messages for invalid inputs.

---

## Sample Usage
**Execution Example #1**:
```
Enter the number of teams in the tournament: 4
Enter the name for team #1: Python
Enter the name for team #2: Ruby
Enter the name for team #3: JavaScript
Enter the name for team #4: C#
Enter the number of games played by each team: 3
Enter the number of wins Team Python had: 2
Enter the number of wins Team Ruby had: 1
Enter the number of wins Team JavaScript had: 0
Enter the number of wins Team C# had: 3
Generating the games to be played in the first round of the tournament...
Home: JavaScript VS Away: C#
Home: Ruby VS Away: Python
```

**Execution Example #2**:
```
Enter the number of teams in the tournament: 6
Enter the name for team #1: AA
Enter the name for team #2: BB
Enter the name for team #3: CC
Enter the name for team #4: DD
Enter the name for team #5: EE
Enter the name for team #6: FF
Enter the number of games played by each team: 6
Enter the number of wins Team AA had: 1
Enter the number of wins Team BB had: 4
Enter the number of wins Team CC had: 3
Enter the number of wins Team DD had: 4
Enter the number of wins Team EE had: 2
Enter the number of wins Team FF had: 5
Generating the games to be played in the first round of the tournament...
Home: AA VS Away: FF
Home: EE VS Away: BB
Home: CC VS Away: DD
```

---

## How It Works
1. **Get Number of Teams**: The program ensures the number is even and at least 2.
2. **Get Team Names**: Each name is validated for length and word count.
3. **Games Played**: The number must meet the minimum required for all matchups.
4. **Wins**: Each team's wins are validated to fall within an acceptable range.
5. **Game Pairing**: Teams are paired such that higher-ranked teams face lower-ranked ones, with the lower-ranked team as the home team.

---

## Code Structure
The code is divided into modular functions for clarity:
- `get_number_of_teams()`: Validates and retrieves the number of teams.
- `get_team_names(num_teams)`: Collects and validates team names.
- `get_number_of_games_played(num_teams)`: Validates games played.
- `get_team_wins(team_names, games_played)`: Collects and validates win counts.
- Main script: Processes inputs, sorts teams by wins, and schedules games.

---

## Requirements
- Python 3.x

---

## Future Improvements
- Add support for multiple rounds.
- Allow customization of tournament rules.
- Enhance error handling for edge cases.

