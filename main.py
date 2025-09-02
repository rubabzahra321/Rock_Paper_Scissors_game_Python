import random

print("🎮 Welcome to Rock, Paper, Scissors Game! 🎉")
print("Type 'rock', 'paper', or 'scissor' to play.\n")

# Dictionary to convert text to number
gamedict = {
    "rock": 1,
    "paper": 2,
    "scissor": 3
}

# Reverse dictionary to convert number to text
comp = {
    1: "rock",
    2: "paper",
    3: "scissor"
}

# Game loop
while True:
    # Take user input
    u = input("Enter your choice (rock/paper/scissor): ").lower()

    # Check for invalid input
    if u not in gamedict:
        print("❌ Invalid choice. Try again.\n")
        continue

    user = gamedict[u]
    c = random.choice([1, 2, 3])  # Computer's random choice

    print(f"🧠 Computer chose: {comp[c]}")
    print(f"👤 You chose: {u}")

    # Determine result
    if c == user:
        print("🤝 It's a draw!\n")
    elif (user == 1 and c == 3) or (user == 2 and c == 1) or (user == 3 and c == 2):
        print("🎉 You win!\n")
    else:
        print("💻 Computer wins!\n")

    # Ask to play again
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("👋 Thanks for playing! Goodbye.")
        break
