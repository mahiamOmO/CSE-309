def greet_user(name):
    print("'Hi{name}!")
    print("welcome to academy")

print("start")
print("john")
print("finish")

#case 1
def greet_user(f_name,l_name):
    print(f'Hi{f_name}{l_name}!')
    print("welcome to academy")

#case 2
print("start")
greet_user("john", "perry")
print("finish")

#case 3
class Greet:
    def greet_user(self,name):
        print(f'Hi{name}!')
        print("welcome to academy")

wish = Greet()
print("start")
wish.greet_user("john")
wish.greet_user("perry")
print("finish")
        