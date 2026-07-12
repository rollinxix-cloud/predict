import json
import os

DATA_FILE = 'matches.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def add_matchup():
    print("\n--- ADD NEW EFOOTBALL MATCHUP ---")
    p1_name = input("Player 1 Name: ")
    p1_rating = input("Player 1 eSports Rating (e.g., 92): ")
    p1_img = input("Player 1 Card Image URL (or leave blank for default): ") or "https://via.placeholder.com/150/1e1e24/fff?text=P1"
    
    p2_name = input("Player 2 Name: ")
    p2_rating = input("Player 2 eSports Rating (e.g., 89): ")
    p2_img = input("Player 2 Card Image URL (or leave blank for default): ") or "https://via.placeholder.com/150/1e1e24/fff?text=P2"
    
    match_type = input("Match Type (League / Knockout / Friendly): ")
    
    matchup = {
        "id": len(load_data()) + 1,
        "match_type": match_type,
        "player1": {"name": p1_name, "rating": p1_rating, "image": p1_img},
        "player2": {"name": p2_name, "rating": p2_rating, "image": p2_img},
        "markets": {
            "full_time": ["1", "X", "2"],
            "first_half": ["1 HT", "X HT", "2 HT"],
            "second_half": ["1 FT", "X FT", "2 FT"],
            "correct_score": True
        }
    }
    
    data = load_data()
    data.append(matchup)
    save_data(data)
    print(f"\n Success! Matchup #{matchup['id']} added. Now push matches.json and index.html to GitHub!")

if __name__ == "__main__":
    add_matchup()
