class FlightTable:
    def __init__(self):
        self.data = [
            {"Location": "Mumbai", "Team 01": "India", "Team 02": "Sri Lanka", "Timing": "DAY"},
            {"Location": "Delhi", "Team 01": "England", "Team 02": "Australia", "Timing": "DAY-NIGHT"},
            {"Location": "Chennai", "Team 01": "India", "Team 02": "South Africa", "Timing": "DAY"},
            {"Location": "Indore", "Team 01": "England", "Team 02": "Sri Lanka", "Timing": "DAY-NIGHT"},
            {"Location": "Mohali", "Team 01": "Australia", "Team 02": "South Africa", "Timing": "DAY-NIGHT"},
            {"Location": "Delhi", "Team 01": "India", "Team 02": "Australia", "Timing": "DAY"}
        ]
    
    def search_by_team(self, team_name):
        matches = []
        for match in self.data:
            if team_name in (match["Team 01"], match["Team 02"]):
                matches.append(match)
        return matches
    
    def search_by_location(self, location):
        matches = []
        for match in self.data:
            if match["Location"] == location:
                matches.append(match)
        return matches
    
    def search_by_timing(self, timing):
        matches = []
        for match in self.data:
            if match["Timing"] == timing:
                matches.append(match)
        return matches
    
def main():
    table = FlightTable()
    
    while True:
        print("Choose search parameter:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        choice = int(input())
        
        if choice == 1:
            team_name = input("Enter team name: ")
            matches = table.search_by_team(team_name)
        elif choice == 2:
            location = input("Enter location: ")
            matches = table.search_by_location(location)
        elif choice == 3:
            timing = input("Enter timing: ")
            matches = table.search_by_timing(timing)
        else:
            print("Invalid choice")
            continue
        
        if not matches:
            print("No matches found.")
        else:
            print("Match Table:")
            for match in matches:
                print(match)
        
        another_search = input("Do you want to perform another search? (yes/no): ")
        if another_search.lower() != "yes":
            break

if __name__ == "__main__":
    main()
## Edward Norton11 ##
