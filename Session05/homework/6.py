map = {
    "size_x": 6,
    "size_y": 6
}

player = {
    "x": 1,
    "y": 1
}

boxes = [
    {"x": 0, "y": 2},
    {"x": 1, "y": 2},
    {"x": 2, "y": 2},
    {"x": 3, "y": 2}
]

destinations = [
    {"x":0,"y":3},
    {"x":0,"y":5},
    {"x":1,"y":4},
    {"x":3,"y":5},
]

obstacles = [
    {'x' : 1, 'y' : 3},
    {'x' : 4, 'y' : 5}
]

old_box = {}
old_player = {}

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
            
            obs_is_here = False
            for obs in obstacles:
                if x == obs["x"] and y == obs["y"]:
                    obs_is_here = True

            if player_is_here:
                print("P ", end="")
            elif box_is_here:
                print("B ", end="")
            elif dest_is_here:
                print("D ", end="")
            elif obs_is_here:
                print("O ", end="")

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
    
    

    move = input("What is your next move? W/A/S/D or (Undo - Z)").upper()
    dx = 0
    dy = 0

    if move == "W":
        dy = -1
    elif move == "S":
        dy = 1
    elif move == "A":
        dx = -1
    elif move == "D":
        dx = 1
    elif move =="Z":
        player["x"] = old_player["x"]
        player["y"] = old_player["y"]
        box["x"] = old_box["x"]
        box["y"] = old_box["y"]

    else:
        playing = False

    old_player["x"] = player["x"]
    old_player["y"] = player["y"]
    old_box["x"] = box["x"]
    old_box["y"] = box["y"]
    
    if 0<= player["x"] + dx < map["size_x"] and 0<= player["y"] + dy < map["size_y"]:
        player["x"] += dx
        player["y"] += dy
    
    for box in boxes:
        if player["x"] == box["x"] and player["y"] == box["y"]:
            # Player can’t push box out of map
            if 0<= box["x"] + dx < map["size_x"] and 0<= box["y"] + dy < map["size_y"]:
                box["x"] += dx
                box["y"] += dy
            else:
                player["x"] -= dx
                player["y"] -= dy
    
    

    
            
            
        
            
                    
            
                        
                            

    

    
   
    
        
            

    
        
        
 





