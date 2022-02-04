
class User:
    def __init__(self,email):
        self.email = email
    def sign_in(self):
        print("lodgged in")


class wizard(User):
    def __init__(self,name,power,email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"attackin with the power of {self.power}")

class archer(User):
     def __init__(self,name,num_arrows,email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

     def attack(self):
        print(f"attacking with the power of {self.num_arrows}") 

     def run(self):
         print('ran really fast')

     def check_arrows(self):
         print(f'{self.num_arrows} remaining')

# class hybrid(wizard,archer):
#     def __init__(self,name,power,arrows):
#         archer.__init__(self,name,arrows)
#         wizard.__init__(self,name,power)

# hb1 = hybrid('kunle',50,100,)
# print(hb1.name())


wiz1=wizard("tolu",50,"micheal_olafioye@yahoo.com")
arch1=archer("samson",100,"samson@gmail.com")   
# wiz1.attack()
# arch1.attack()
    
        
def player_attack(xter):
    xter.attack()

player_attack(wiz1)
player_attack(arch1)

print(wiz1.email)
print(arch1.email)

