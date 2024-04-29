import sqlite3

def create_database():
    with sqlite3.connect('gym_database.db') as conn:
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Departments (
            department_id INTEGER PRIMARY KEY,
            department_name TEXT
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Members (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            trainer_id INTEGER,
            FOREIGN KEY (trainer_id) REFERENCES Trainers(id)
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Trainers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department_id INTEGER,
            FOREIGN KEY (department_id) REFERENCES Departments(department_id)
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS WorkoutSessions (
            session_id INTEGER PRIMARY KEY,
            member_id INTEGER,
            date TEXT,
            duration_minutes INTEGER,
            calories_burned INTEGER,
            FOREIGN KEY (member_id) REFERENCES Members(id)
        )
        ''')

def add_member(name, age, trainer_id):
    try:
        with sqlite3.connect('gym_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Members (name, age, trainer_id) VALUES (?, ?, ?)", (name, age, trainer_id))
            print("Member added successfully!")
    except sqlite3.IntegrityError as e:
        print("Error:", e)

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
        with sqlite3.connect('gym_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (?, ?, ?, ?)", (member_id, date, duration_minutes, calories_burned))
            print("Workout session added successfully!")
    except sqlite3.IntegrityError as e:
        print("Error:", e)

def update_member_age(member_id, new_age):
    try:
        with sqlite3.connect('gym_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Members SET age = ? WHERE id = ?", (new_age, member_id))
            print("Member age updated successfully!")
    except sqlite3.IntegrityError as e:
        print("Error:", e)

def delete_workout_session(session_id):
    try:
        with sqlite3.connect('gym_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM WorkoutSessions WHERE session_id = ?", (session_id,))
            print("Workout session deleted successfully!")
    except sqlite3.IntegrityError as e:
        print("Error:", e)

if __name__ == "__main__":
    create_database()  
    
    add_member('John Doe', 30, 1)
    add_workout_session(1, '2024-04-28', 60, 300)
    update_member_age(1, 35)
    delete_workout_session(1)
