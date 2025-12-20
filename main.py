from upgrade import Upgrade

# main.py
def main():
    coins = 0
    enter = 1

    upgrades = [
        Upgrade("Enter+1", "Increases coins gained from pressing Enter", 50, "enter"),
        Upgrade("Enter+2", "Increases coins gained from pressing Enter", 2500, "enter"),
        Upgrade("Enter+3", "Increases coins gained from pressing Enter", 125000, "enter"),
        Upgrade("Enter+4", "Increases coins gained from pressing Enter", 6250000, "enter"),
        Upgrade("Enter+5", "Increases coins gained from pressing Enter", 312500000, "enter")
    ]
    
    input("Press enter to get coins!")

    while(True):
        coins+=enter
        available = []
        for i in range(0, len(upgrades)):
            upgr = upgrades[i]
            if upgr.cost <= coins:
                available.append([i, upgr])
                print(f'{len(available)} - {upgr.name} | {upgr.cost} coins | {upgr.desc}')
        print(f'Coins: {coins}')

        inp = input()
        
        if (inp != ""):
            try:
                # Implement Upgrade Stucture



main()