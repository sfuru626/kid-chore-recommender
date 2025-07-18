# Kid Chore Recommender

chore_ideas = {
    'toddler': {
        'active': ['Put away toys', 'Help load laundry', 'Wipe table'],
        'quiet': ['Sort socks', 'Help hand you items while cleaning', 'Place books on shelf']
    },
    'young kid': {
        'active': ['Feed pets', 'Sweep floor', 'Set the table'],
        'quiet': ['Fold towels', 'Dust shelves', 'Match socks']
    },
    'tween': {
        'active': ['Vacuum a room', 'Take out the trash', 'Rake leaves'],
        'quiet': ['Organize bookshelf', 'Clean bathroom sink', 'Fold laundry']
    },
    'teen': {
        'active': ['Wash the car', 'Mow the lawn', 'Move trash bins'],
        'quiet': ['Plan a meal', 'Budget groceries', 'Clean the fridge']
    }
}

print("👋 Welcome to the Kid Chore Recommender!")
print("Let's find some helpful and age-appropriate chores.\n")

age_group = input("What age group is the child? (toddler, young kid, tween, teen): ").lower()

if age_group not in chore_ideas:
    print(f"Sorry, '{age_group}' is not a valid age group. Please try again.")
else:
    personality = input("Would you describe the child as 'active' or 'quiet'?: ").lower()

    if personality not in chore_ideas[age_group]:
        print(f"Sorry, we don't have chores for '{personality}' personalities in the '{age_group}' group.")
    else:
        print(f"\nHere are some chore ideas for a {personality} {age_group}:")
        for chore in chore_ideas[age_group][personality]:
            print(f"- {chore}")

        print("\nThanks for using the Chore Recommender! ✅")
