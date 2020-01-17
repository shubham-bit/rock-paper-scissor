import random

continueGame=True
choices = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissors"
}
menuOptions = "R - Rock\nP - Paper\nS - Scissors"

def decideWinner(selected):
    cpu = selected.get("cpu")
    usr = selected.get("usr")

    if cpu == usr:
        return "draw"
    elif (cpu == choices.get("r") and usr != choices.get("p") or
        cpu == choices.get("p") and usr != choices.get("s") or
        cpu == choices.get("s") and usr != choices.get("r")):
        return "cpu"
    else:
        return "usr"

name = input("Enter a name: ")
players = {
    "cpu": "CPU",
    "usr": name,
    "draw": "It's a draw"
}

while continueGame:
    cpu = random.choice('rps')

    print("\n" + menuOptions)
    usr = input("\nChoose: ")
    usr = usr.lower()
    if (choices.get(usr) == None):
        print("\nWrong response")
        continueGame = input("\nTry again?(Y/N): ").lower() == "y" or False
        continue

    winner = decideWinner({
        "cpu": choices.get(cpu),
        "usr": choices.get(usr)
    })

    print("\nCPU: " + choices.get(cpu) + "\n" + name + " " + choices.get(usr))
    print("\n==============")
    print("Winner: " + players.get(winner))
    print("==============")
    continueGame = input("\nTry again?(Y/N): ").lower() == "y" or False

print("\nLet's play again")
