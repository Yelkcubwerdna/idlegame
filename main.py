from upgrade import Upgrade
import time
import math

# main.py
def main():
    coins = 0
    enter = 1
    snails = 0
    crows = 0
    monkeys = 0
    last_time = time.time()
    time_passed = 0
    time_passed_snails = 0
    time_passed_crows = 0
    time_passed_monkeys = 0

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
        Upgrade("Snails+5", "Hire more snails to press enter for you", 177978515625, "snails"),
        Upgrade("Crows", "Hire crows to press enter for you", 113, "crows"),
        Upgrade("Crows+1", "Hire more crows to press enter for you", 12656, "crows"),
        Upgrade("Crows+2", "Hire more crows to press enter for you", 1423828, "crows"),
        Upgrade("Crows+3", "Hire more crows to press enter for you", 160180664, "crows"),
        Upgrade("Crows+4", "Hire more crows to press enter for you", 1.8020325e10, "crows"),
        Upgrade("Crows+5", "Hire more crows to press enter for you", 2.02728653e12, "crows"),
        Upgrade("Monkeys", "Hire monkeys to press enter for you", 170, "monkeys"),
        Upgrade("Monkeys+1", "Hire more monkeys to press enter for you", 28730, "monkeys"),
        Upgrade("Monkeys+2", "Hire more monkeys to press enter for you", 4869777, "monkeys"),
        Upgrade("Monkeys+3", "Hire more monkeys to press enter for you", 825427265, "monkeys"),
        Upgrade("Monkeys+4", "Hire more monkeys to press enter for you", 1.39909921e11, "monekys"),
        Upgrade("Monkeys+5", "Hire more monkeys to press enter for you", 2.3714731682e13, "monkeys"),
    ]
    
    input("Press enter to get coins!")

    while(True):
        print('\n\n\n\n\n\n')
        before = coins
        coins+=enter + math.floor(time_passed*snails) + math.floor(time_passed*crows) + math.floor(time_passed*monkeys)
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
            coins_gained_snails = math.floor(snails * time_passed_snails)
            time_spent_snails = 0
            if (coins_gained_snails > 0):
                time_spent_snails = coins_gained_snails / snails
                time_passed_snails -= time_spent_snails
            print(f'Snails = +{math.floor(coins_gained_snails)} ({snails} * {math.floor(time_spent_snails)} seconds)')
        if crows > 0:
            coins_gained_crows = math.floor(crows * time_passed_crows)
            time_spent_crows = 0
            if (coins_gained_crows) > 0:
                time_spent_crows = coins_gained_crows / crows
                time_passed_crows -= time_spent_crows
            print(f'Crows = +{math.floor(coins_gained_crows)} ({crows} * {math.floor(time_spent_crows)} seconds)')
        if monkeys > 0:
            coins_gained_monkeys = math.floor(monkeys * time_passed_monkeys)
            time_spent_monkeys = 0
            if (coins_gained_monkeys > 0):
                time_spent_monkeys = coins_gained_monkeys / monkeys
                time_passed_monkeys -= time_spent_monkeys
            print(f'Monkeys = +{math.floor(coins_gained_monkeys)} ({monkeys} * {math.floor(time_spent_monkeys)} seconds)')
        print(f'==========\nCoins: {math.floor(coins)}')

        inp = input()
        
        time_passed = time.time() - last_time
        last_time = time.time()
        if snails > 0:
            time_passed_snails += time_passed
        if crows > 0:
            time_passed_crows += time_passed
        if monkeys > 0:
            time_passed_monkeys += time_passed
        
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
                    case "crows":
                        crows += 0.5
                    case "monkeys":
                        monkeys += 1
            except:
                print("Input does not match an available option")






main()