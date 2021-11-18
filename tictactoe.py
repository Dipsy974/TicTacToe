grid = ["","","","","","","","",""]
turn = 0
victory = False



while (turn != 9 and victory == False):


    play = int(input("Quelle case voulez-vous jouer ?"))
    while(grid[play] == "x" or grid[play] == "o"):
         play = int(input("Case déjà prise, quelle case voulez-vous jouer ?"))


    if(turn%2 == 0):
        grid[play] = "o"
    else:
        grid[play] = "x"

    for i in range(3):
        for j in range(3):
            if(grid[3*i + j] == "x"):
                print("X", end=" ")
            elif(grid[3*i + j] == "o"):
                print("O", end=" ")
            else:
                print(" ", end=" ")
        print("")

    for i in range(3):
        if(grid[i] == grid[i+3] == grid[i+6] == "x"):
            victory = True
            print("Joueur 1 a gagné.")
        elif(grid[i] == grid[i+3] == grid[i+6] == "o"):
            victory = True
            print("Joueur 2 a gagné.")

 
        

    turn += 1 