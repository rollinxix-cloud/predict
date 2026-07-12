import json
import os

DATA_FILE = 'matches.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        print("\n[⚠️ WARNING]: matches.json was corrupted. Resetting it safely to avoid crashes.")
        save_data([])
        return []

def save_data(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"[❌ ERROR]: Could not save data: {e}")

def clear_all_matches():
    confirm = input("\nAre you sure you want to completely clear all matches? (yes/no): ").lower()
    if confirm == 'yes':
        save_data([])
        print("🧹 All matches have been cleared successfully!")
    else:
        print("Action cancelled.")

def add_matchup():
    print("\n--- EDN PREMIUM ODDS & MATCHUP CONFIGURATOR ---")
    
    p1_name = input("Player 1 Name: ").strip() or "Player 1"
    p1_rating = input("Player 1 OVR Rating: ").strip() or "90"
    p1_img = input("Player 1 Image Path (e.g., images/p1.png): ").strip() or "images/default.png"
    
    p2_name = input("Player 2 Name: ").strip() or "Player 2"
    p2_rating = input("Player 2 OVR Rating: ").strip() or "90"
    p2_img = input("Player 2 Image Path (e.g., images/p2.png): ").strip() or "images/default.png"
    
    match_type = input("Match Type (ULTIMATE PLAYER / ELITE LEAGUE / KNOCKOUT): ").upper().strip() or "MATCH"
    
    print("\n--- SET YOUR ODDS ---")
    odds_1 = input(f"Odds for {p1_name} Win (1): ").strip() or "1.0"
    odds_x = input("Odds for Draw (X): ").strip() or "1.0"
    odds_2 = input(f"Odds for {p2_name} Win (2): ").strip() or "1.0"
    
    odds_ht_1 = input("Odds 1st Half - 1 HT: ").strip() or "1.0"
    odds_ht_x = input("Odds 1st Half - X HT: ").strip() or "1.0"
    odds_ht_2 = input("Odds 1st Half - 2 HT: ").strip() or "1.0"
    
    odds_cs = input("Average Correct Score Multiplier (e.g., 7.5): ").strip() or "1.0"
    
    data = load_data()
    
    matchup = {
        "id": len(data) + 1,
        "match_type": match_type,
        "player1": {"name": p1_name, "rating": p1_rating, "image": p1_img},
        "player2": {"name": p2_name, "rating": p2_rating, "image": p2_img},
        "odds": {
            "full_time": {"1": odds_1, "X": odds_x, "2": odds_2},
            "half_time": {"1HT": odds_ht_1, "XHT": odds_ht_x, "2HT": odds_ht_2},
            "correct_score": odds_cs
        }
    }
    
    data.append(matchup)
    save_data(data)
    print(f"\n✅ Success! Matchup #{matchup['id']} saved to matches.json.")

def main_menu():
    while True:
        print("\n==============================")
        print("   EDN BACKEND MANAGEMENT   ")
        print("==============================")
        print("1. Add New Matchup")
        print("2. Clear/Reset All Matches (Remove Test Data)")
        print("3. Exit Program")
        choice = input("\nEnter choice (1-3): ").strip()
        
        if choice == '1':
            add_matchup()
        elif choice == '2':
            clear_all_matches()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main_menu()
