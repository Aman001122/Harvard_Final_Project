# Harvard_Final_Project.py

def main():
    print("Welcome to the Habit Tracker App!")
    print("This application helps you monitor your daily habits and track your progress.\n")
    
    habits = {}
    
    while True:
        print("\nMenu Options:")
        print("1. Add a new habit")
        print("2. Log a habit completion")
        print("3. Check habit statistics")
        print("4. Exit the application")
        
        selection = input("Please choose an option (1-4): ")
        
        if selection == '1':
            add_habit(habits)
        elif selection == '2':
            log_completion(habits)
        elif selection == '3':
            display_statistics(habits)
        elif selection == '4':
            print("Thank you for using the Habit Tracker! Keep up the good work!")
            break
        else:
            print("Invalid selection. Please try again.")

# Harvard_Final_Project.py

def add_habit(habits, habit_name=None):
    """Add a new habit to the tracker."""
    if habit_name is None:
        habit_name = input("What habit would you like to track? ")
    habits[habit_name] = {'target_days': 30, 'logged_days': 0}
    print(f"Habit '{habit_name}' added.")

def log_completion(habits, habit_name=None):
    """Log a completed habit."""
    if habit_name is None:
        habit_name = input("Which habit did you complete today? ")
    if habit_name in habits:
        habits[habit_name]['logged_days'] += 1
        print(f"Habit '{habit_name}' logged for completion.")
    else:
        print(f"Habit '{habit_name}' not found.")
        
def display_statistics(habits):
    """Display the completion statistics for each habit."""
    if not habits:
        print("You haven't added any habits yet.")
        return
    for habit, data in habits.items():
        completion_percentage = (data['logged_days'] / data['target_days']) * 100
        print(f"{habit}: {data['logged_days']} out of {data['target_days']} days completed ({completion_percentage:.2f}%)")


if __name__ == "__main__":
    main()
