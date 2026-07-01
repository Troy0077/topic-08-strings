"""
CIS Intro to Programming - Week 4 Assignment
File: solution.py
Purpose: A 12-Team College Football Playoff bracket generator using dictionaries and lists.
"""

def main():
    print("=== 12-TEAM COLLEGE FOOTBALL PLAYOFF BRACKET ===")
    print("Processing tournament seedings and first-round matchups.\n")

playoff_seeds = {
        1: "Indiana",
        2: "Ohio State",
        3: "Georgia",
        4: "Texas Tech",
        5: "Oregon",
        6: "Ole Miss",
        7: "Texas A&M",
        8: "Oklahoma",
        9: "Alabama",
        10: "Miami",
        11: "Tulane",
        12: "James Madison"
    }

teams_with_byes = []
    first_round_teams = []

for seed, team in playoff_seeds.items():
        if seed <= 4:

          teams_with_byes.append(team)
        else:

          first_round_teams.append(team)

print("--- Teams Receiving a First-Round Bye ---")
    for index, team in enumerate(teams_with_byes, 1):

      print(f"Seed #{index}: {team.upper()}")
    print("-----------------------------------------\n")

print("--- First Round Matchups (Hosted on Campus) ---")

seed_pairs = [(5, 12), (6, 11), (7, 10), (8, 9)]

for high_seed, low_seed in seed_pairs:

  home_team = playoff_seeds[high_seed]
        away_team = playoff_seeds[low_seed]

print(f"Matchup: Seed #{high_seed} {home_team} vs. Seed #{low_seed} {away_team}")
        print(f"  Location: Game hosted at {home_team}\n")

print("-----------------------------------------")
    search_team = input("Enter a team name to search their current playoff status: ").strip()

found = False
    for seed, team in playoff_seeds.items():

      if search_team.lower() == team.lower():
            found = True
            print(f"\nResult: {team} is in the bracket as Seed #{seed}.")
            
            if seed <= 4:
                print("Status: Advanced directly to the Quarterfinals.")
            else:
                print(f"Status: Playing in the First Round.")
            break

    if not found:
        print(f"\nResult: '{search_team}' did not qualify for the 12-team playoff bracket.")

if __name__ == "__main__":
    main()
