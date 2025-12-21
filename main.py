from upgrade import Upgrade
import time
import math

# main.py
def main():
    coins = 0
    enter = 1
    snails = 0
    last_time = time.time()
    time_passed = 0

    upgrades = [
        Upgrade("Enter+1", "Increases coins gained from pressing Enter", 50, "enter"),
        Upgrade("Enter+2", "Increases coins gained from pressing Enter", 2500, "enter"),
        Upgrade("Enter+3", "Increases coins gained from pressing Enter", 125000, "enter"),
        Upgrade("Enter+4", "Increases coins gained from pressing Enter", 6250000, "enter"),
        Upgrade("Enter+5", "Increases coins gained from pressing Enter", 312500000, "enter"),
        Upgrade("Snails", "Hire snails to press enter for you", 75, "snails"),
        Upgrade("Snails+1", "Hire more snails to press enter for you", 5625, "snails"),
        Upgrade("Snails+2", "Hire more snails to press enter for you", 421875, "snails"),
        Upgrade("Snails+3", "Hire more snails to press enter for you", 31640625, "snails"),
        Upgrade("Snails+4", "Hire more snails to press enter for you", 2373046875, "snails"),
        Upgrade("Snails+5", "Hire more snails to press enter for you", 177978515625, "snails")
    ]
    
    input("Press enter to get coins!")

    while(True):
        print('\n\n\n\n\n\n')
        before = coins
        coins+=enter + math.floor(time_passed*snails)
        available = []

        print('Available Upgrades\n===============')
        for i in range(0, len(upgrades)):
            upgr = upgrades[i]
            if upgr.cost <= coins:
                available.append([i, upgr])
                print(f'{len(available)} - {upgr.name} | {upgr.cost} coins | {upgr.desc}')

        if len(available) == 0:
            print("None")

        print(f'\nBefore = {before}\nEnter = +{enter}')
        if snails > 0:
            print(f'Snails = +{math.floor(snails * time_passed)} ({snails} * {math.floor(time_passed)} seconds)')
        print(f'==========\nCoins: {math.floor(coins)}')

        inp = input()
        time_passed = time.time() - last_time
        last_time = time.time()
        
        if (inp != ""):
            # Adjust to account for 0 element
            inp = int(inp)- 1
            try:
                # Remove from upgrade list
                upgrades.pop(available[inp][0])

                # Perform Upgrade
                upgr = available[inp][1]

                # Take cost of upgrade
                coins -= upgr.cost

                match (upgr.func):
                    case "enter":
                        enter += 1
                    case "snails":
                        snails += 0.1
            except:
                print("Input does not match an available option")






main()