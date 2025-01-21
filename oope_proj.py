class chatbook:
    def __init__(self):
        self.username =""
        self.password = ""
        self.loggedin = False
        self.menu()
    def menu(self):
        user_input = input("""Welcome to chat book whill you like to procedd
                           press 1 to sign up
                           press 2 to sign in
                           press 3 to write a post
                           press 4 to message a friend
                           press 5 to exit
                           \n""")
        if user_input=='1' :
            self.signup()
        elif user_input=='2':
            self.signin()
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        else:
            exit()       
    
    def signup(self):
        username = input("Enter your email adress : ")
        password = input("Enter your password : ")
        self.username = username
        self.password = password
        print("You have successfully signed up")
        self.menu()
        
    def signin(self):
        if self.username=='' and self.password=='':
            print("you have to sign up first \n")
        else:
            uname = input("Enter your username : ")
            pwd = input("Enter your password : ")
            if self.username==uname and self.password==pwd:
                print("you have successfully signed \n")
                self.loggedin() = True
            else:
                print("you have wrong input")
        self.menu()
    
obj = chatbook()