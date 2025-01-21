class chatbook:
    def __init__(self):
        self.username =""
        self.password = ""
        self.logged = False
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
            self.mypost()
        elif user_input=='4':
            self.writeMessage()
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
                self.logged = True
            else:
                print("you have wrong input")
        self.menu()
    
    def mypost(self):
        if self.logged==True:
            txt = input("Enter your text here")
            print(f"your msg is:-> {txt}")
        else:
            print("Sign in first to post something")
        self.menu()
    
    def writeMessage(self):
        if self.loggedin==True:
            msg = input("Enter your message")
            print(f"your msg is:-> {msg}")
        else:
            print("Sign in second to msg something")
        self.menu()
            
    
obj = chatbook()