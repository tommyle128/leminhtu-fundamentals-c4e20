print("Welcome to the super login gateway")

loop = True
login_counter = 0
real_name = "c4e"
real_pass = "codethechange"

while loop:
    if login_name == input("Username: "):
        
        login_pass = input("Pasword: ")
        if login_pass == "codethechange":
            print("Welcome, ",real_name)
            break
        else:
            print("Password is incorrect!")
            login_counter += 1
       
    else:
        print("Username is incorrect!")
        login_counter += 1
    
    if login_counter ==3:
        print ("You failed to log in 3 times, go away!!!")
        loop = False
    
    
            

