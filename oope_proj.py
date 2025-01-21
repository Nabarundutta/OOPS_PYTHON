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
                           press 5 to exit""")
        if user_input=='1' :
            pass
        elif user_input=='2':
            pass
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        else:
            exit()       
            
obj = chatbook()