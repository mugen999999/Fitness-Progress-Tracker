import csv
import os

PROGRESS_FILE = "data/progress.csv"

def initialize():
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Exercise", "Sets", "Reps", "Weight (kg)", "Duration (min)"])  # Header row

def add_workout(date, exercise, sets, reps, weight, duration):
    with open(PROGRESS_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, exercise, sets, reps, weight, duration])

def view_workouts():
    with open(PROGRESS_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def main():
    initialize()
    while True:
        print("\n1. Add Workout\n2. View Workout History\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            exercise = input("Enter exercise name: ")
            sets = input("Enter number of sets: ")
            reps = input("Enter number of reps: ")
            weight = input("Enter weight used (kg): ")
            duration = input("Enter duration (min): ")
            add_workout(date, exercise, sets, reps, weight, duration)
        elif choice == "2":
            view_workouts()
        elif choice == "3":
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()

