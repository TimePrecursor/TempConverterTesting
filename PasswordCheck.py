class functionclass:
    # def    __init__(self):
    #     pass

    def passwordstep(self,pos,passw):
        with open("Logins2.txt") as file:
            lines = file.readlines()
            x = lines[pos].split("|")
            print(x[3])
            if int(x[3]) == int(passw):
                return True
            else:
                return False
