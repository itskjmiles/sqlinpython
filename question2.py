import sqlite3

def list_distinct_trainers():
    try:
        with sqlite3.connect('gym_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT DISTINCT trainer_id FROM Members")
            trainers = cursor.fetchall()
            print("Distinct Trainers:")
            for trainer in trainers:
                print(trainer[0])
    except sqlite3.Error as e:
        print("Error:", e)

def count_members_per_trainer():
    try:
        with sqlite3.connect('gym_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT trainer_id, COUNT(id) FROM Members GROUP BY trainer_id")
            trainer_counts = cursor.fetchall()
            print("Members per Trainer:")
            for trainer_count in trainer_counts:
                print("Trainer ID:", trainer_count[0], "- Member Count:", trainer_count[1])
    except sqlite3.Error as e:
        print("Error:", e)

def get_members_in_age_range(start_age, end_age):
    try:
        with sqlite3.connect('gym_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name, age, trainer_id FROM Members WHERE age BETWEEN ? AND ?", (start_age, end_age))
            members = cursor.fetchall()
            print(f"Members between ages {start_age} and {end_age}:")
            for member in members:
                print("Name:", member[0], "- Age:", member[1], "- Trainer ID:", member[2])
    except sqlite3.Error as e:
        print("Error:", e)

if __name__ == "__main__":
    list_distinct_trainers()  
    count_members_per_trainer()  
    get_members_in_age_range(25, 30)  
