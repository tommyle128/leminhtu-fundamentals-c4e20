map = {
    "size_x": 5,
    "size_y": 5
}

player = {
    "x": 3,
    "y": 4
}

boxes = [
    {"x": 1, "y": 1},
    {"x": 2, "y": 2},
    {"x": 3, "y": 3},
]

destinations = [
    {"x": 2, "y": 1},
    {"x": 3, "y": 2},
    {"x": 4, "y": 3},
]


playing = True
while playing:

    # print map
    for y in range (map["size_y"]):
        for x in range (map["size_x"]):
            box_is_here = False
            for box in boxes:
                if y == box["y"] and x == box["x"]:
                    box_is_here = True

            player_is_here = False                 
            if y == player["y"] and x == player["x"]:
                player_is_here = True       
        
            dest_is_here = False
            for dest in destinations:                      
                if y == dest["y"] and x == dest["x"]:
                    dest_is_here = True
                
            if player_is_here:
                print("P ", end="")
            elif box_is_here:
                print("B ", end="")
            elif dest_is_here:
                print("D ", end="")
                           
            else:   
                print("- ", end ="")
        print()
    # End of print map
    ##### check win
    win = True
    for box in boxes:
        if box not in destinations:
            win = False
    
    if win:
        print("You win!!!")
        break
    ######
    
    dx = 0
    dy = 0

    move = input("Your move: ").upper()
    if move == "W":
        dy = -1
    elif move == "S":
        dy = 1
    elif move == "A":
        dx = -1
    elif move == "D":
        dx = 1
    else:
        playing = False
    
    if 0<= player["x"] + dx < map["size_x"] and 0<= player["y"] + dy < map["size_y"]:
        player["x"] += dx
        player["y"] += dy
    
    for box in boxes:
        if player["x"] == box["x"] and player["y"] == box["y"]:
            box["x"] += dx
            box["y"] += dy
    
   
            

    
        
        
 





