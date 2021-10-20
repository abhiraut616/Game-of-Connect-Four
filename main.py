#Function for drawing playing board
def drawBoard():
    for i in range(r):
        for j in range(c+1):
            for k in occupy_places:
                if i == k[0] and j == k[1]:
                    print("|", k[2], sep="", end="")
                    break
            else:
                print("|", end=" ")
        print()

#Function to check specified number of pieces of player1 or player2 connected vertically
def checkVertically():
    # Player 1:
    c_lis = []
    r_lis = []
    for e in range(0, len(occupy_places), 2):
        c_lis.append(occupy_places[e][1])

    for c in c_lis:
        if c_lis.count(c) >= p:
            for s in range(0, len(occupy_places), 2):
                if occupy_places[s][1] == c:
                    r_lis.append(occupy_places[s][0])
            break

    if len(r_lis) >= p:
        lis = sorted(r_lis)
        m = max(lis)
        for e in range(len(lis)):
            if m-e in lis:
                continue
            else:
                break
        else:
            return 1

    # Player 2:
    c_lis = []
    r_lis = []
    for e in range(1, len(occupy_places), 2):
        c_lis.append(occupy_places[e][1])

    for c in c_lis:
        if c_lis.count(c) >= p:
            for s in range(1, len(occupy_places), 2):
                if occupy_places[s][1] == c:
                    r_lis.append(occupy_places[s][0])
            break

    if len(r_lis) >= p:
        lis = sorted(r_lis)
        m = max(lis)
        for e in range(len(lis)):
            if m-e in lis:
                continue
            else:
                break
        else:
            return 2

#Function to check specified number of pieces of player1 or player2 connected Horizontally
def checkHorizontally():
    # Player 1:
    c_lis = []
    r_lis = []
    for e in range(0, len(occupy_places), 2):
        r_lis.append(occupy_places[e][0])

    for r in r_lis:
        if r_lis.count(r) >= p:
            for s in range(0, len(occupy_places), 2):
                if occupy_places[s][0] == r:
                    c_lis.append(occupy_places[s][1])
            break

    if len(c_lis) >= p:
        lis = sorted(c_lis)
        m = max(lis)
        for e in range(len(lis)):
            if m-e in lis:
                continue
            else:
                break
        else:
            return 1

    # Player 2:
    c_lis = []
    r_lis = []
    for e in range(1, len(occupy_places), 2):
        r_lis.append(occupy_places[e][0])

    for r in r_lis:
        if r_lis.count(r) >= p:
            for s in range(1, len(occupy_places), 2):
                if occupy_places[s][0] == r:
                    c_lis.append(occupy_places[s][1])
            break

    if len(c_lis) >= p:
        lis = sorted(c_lis)
        m = max(lis)
        for e in range(len(lis)):
            if m-e in lis:
                continue
            else:
                break
        else:
            return 2

#Function to check specified number of pieces of player1 or player2 connected Diagonally
def checkDiagonally():
    # Player 1:
    count = 0
    r_lis = []
    c_lis = []
    for s in range(0, len(occupy_places), 2):
        r_lis.append(occupy_places[s][0])
        c_lis.append(occupy_places[s][1])

    r_max = max(r_lis)
    c_max = max(c_lis)
    for e in range(len(r_lis)):
        if r_max-e in r_lis and c_max-e in c_lis:
            count += 1
    if count >= p:
        return 1

    # Player 2:
    count = 0
    r_lis = []
    c_lis = []
    for s in range(1, len(occupy_places), 2):
        r_lis.append(occupy_places[s][0])
        c_lis.append(occupy_places[s][1])

    r_max = max(r_lis)
    c_max = max(c_lis)
    for e in range(len(r_lis)):
        if r_max-e in r_lis and c_max-e in c_lis:
            count += 1
    if count >= p:
        return 2

#Function to check pieces connected vertically or horizontally or diagonally
def checkResult():
    res=checkVertically()
    if res == 1:
        print("Player 1 Win")
        return 1
    if res==2:
        print("Player 2 Win")
        return 1
    
    res=checkHorizontally()
    if res == 1:
        print("Player 1 Win")
        return 1
    if res==2:
        print("Player 2 Win")
        return 1

    res=checkDiagonally()
    if res == 1:
        print("Player 1 Win")
        return 1
    if res==2:
        print("Player 2 Win")
        return 1
    return 0

    
#Function to get the row,column,pieces,player 1 color and player 2 color values
def initial():    
    r=int(input("Enter row: "))
    c=int(input("Enter column: "))
    p=int(input("Enter piece: "))
    while(True):
        if p<=0:
            print("You cannot have ",p," pieces to connect.")
            p=int(input("Please enter a positive, non-zero integer for the number of pieces to connect: "))
        else:
            break
    p1_color=input("\nPlayer one, do you want red or yellw (r or y)?" )
    if p1_color=='r':
        p2_color='y'
    else:
        p2_color='r'
    return [r,c,p,p1_color,p2_color]
    


#Starting point of program
occupy_places=[]     #This list contains the account of already occupied places of playing board 
occupy_rows_per_col={}   #This dictionary contains account of every column filled rows
play=0
r,c,p,p1_color,p2_color=initial()
drawBoard()

while(True):
    #Player 1:
    column=int(input("\nPlayer 1, what column do you want to put your piece? "))-1
    if column in occupy_rows_per_col:
        for e in range(r-1,-1,-1):
            if  e not in occupy_rows_per_col[column]:
                occupy_rows_per_col[column].append(e)
                occupy_places.append((e,column,p1_color))
                break
    else:
        occupy_rows_per_col[column]=[r-1]
        occupy_places.append((r-1,column,p1_color))
    drawBoard()

    if play>=p:
         if checkResult():
            if int(input("\nDo you want to play again (0-no, 1-yes)? ")):
                play=0
                occupy_places.clear()
                occupy_rows_per_col.clear()
                r,c,p,p1_color,p2_color=initial()
                drawBoard()
                continue
            else:
                break


    # Player 2:
    column=int(input("\nPlayer 2, what column do you want to put your piece? "))-1
    if column in occupy_rows_per_col:
        for e in range(r-1,-1,-1):
            if  e not in occupy_rows_per_col[column]:
                occupy_rows_per_col[column].append(e)
                occupy_places.append((e,column,p2_color))
                break
    else:
        occupy_rows_per_col[column]=[r-1]
        occupy_places.append((r-1,column,p2_color))
    drawBoard()
    play+=1
    if play>=p:
         if checkResult():
            if int(input("\nDo you want to play again (0-no, 1-yes)? ")):
                play=0
                occupy_places.clear()
                occupy_rows_per_col.clear()
                r,c,p,p1_color,p2_color=initial()
                drawBoard()
            else:
                break

    
    
   
        
    
        
        



