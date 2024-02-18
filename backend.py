import dice
import math
import numpy as np
# import packages

import matplotlib.pyplot as plt

def roller(roll):
    return (dice.roll(roll))
x = True

while x:
    print("please enter a dice roll or type 0 to exit")
    decision = input()
    if(decision == "0"):
        x = False
    else:
        #determine how to advantage vs disadvantage dataset
        data = [int(i) for i in dice.roll(decision)]
        poopData = [int(i) for i in dice.roll(decision)]

        sortedData = (data.sort())
        
        print(*data)
        print("The mean(True) value is " + str((sum(data) / len(data))))
        print("The mean(Ceil) value is " + str(math.ceil(sum(data) / len(data))))
        print("The mean(Floor) value is " + str(math.floor(sum(data) / len(data))))
        print("please specify plot type, standard hist with 1 variable (1), hist with 2 variables, hexbin with 2 variables")
        choice = input()
        if(choice == "1"):
            plt.hist(data,  density=True, color='b', edgecolor = "black")
            plt.show()
        elif(choice == "2"):
            # Creating a stacked histogram
            plt.hist([data, poopData], bins=30, stacked=True, color=['cyan', 'Purple'], edgecolor='black')
                # Adding labels and title
            plt.xlabel('Die Rolls')
            plt.ylabel('Frequency')
            plt.title('Advantage vs Disadvantage')
            # Adding legend
            plt.legend(['Advantage', 'Disadvantage'])
            plt.show()
        elif(choice == "3"):            
            plt.hexbin(data, poopData, gridsize=30, cmap="Blues", edgecolors= "black")
            # Adding labels and title
            plt.title('2D Histogram (Hexbin Plot)')
            # Adding colorbar
            plt.colorbar()
            plt.show()
        
        
       



