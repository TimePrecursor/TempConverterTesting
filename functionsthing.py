class functionclass:
    def    __init__(self):
        pass

    def passwordstep(self,user,pos,passw):
        with open("Logins2.txt") as file:
            line = file.readline(pos)
            print(user)
            if str(line[3]) == passw:
                return True
