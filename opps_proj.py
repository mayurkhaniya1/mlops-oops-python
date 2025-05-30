# oops to project create

class chatbook:
    def __init__(self):
        self.username=""
        self.password = ""
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""welcome to chatbook !! how would you like to proceed
                           1. press 1 to sigup
                           2 press 2 to signin
                           3 press 3 to rite a post
                           4 press 4 to message a friend
                           5 press 5 to other key to exit""")
        
        if user_input == "1":
            self.sigup()

        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else : 
            exit()

    def sigup(self):
        email = input("Enter your email here -> ")
        passwordd = input("Enter your password here -> ")
        self.username = email
        self.password = passwordd                
        print("you heve signed up successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == "" and self.password == "":
            print("please sinup first by pressing 1 in the mail menu")
        else:
            uname = input("Enter your email/username here -> ")
            pws = input("Enter your password here -> ")
            if self.username == uname and self.password == pws:
                print("you have signed in successfully !!")
                self.loggedin = True
            else:
                print("please input correct creadintials..")

        print("\n")
        self.menu()
# object create
obj = chatbook()
