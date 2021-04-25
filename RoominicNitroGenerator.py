import random, string
from requests import Session
from colorama import Fore, init

init(convert=True)

print('██████╗░░█████╗░░█████╗░███╗░░░███╗██╗███╗░░██╗██╗░█████╗░')
print('██╔══██╗██╔══██╗██╔══██╗████╗░████║██║████╗░██║██║██╔══██╗')
print('██████╔╝██║░░██║██║░░██║██╔████╔██║██║██╔██╗██║██║██║░░╚═╝')
print('██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║██║██║╚████║██║██║░░██╗')
print('██║░░██║╚█████╔╝╚█████╔╝██║░╚═╝░██║██║██║░╚███║██║╚█████╔╝')
print('╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░╚════╝░')
print('%show many codes you want to generate?%s ' % (Fore.CYAN, Fore.WHITE), end='')
amount = int(input())
for i in range(amount):
    code = "https://discord.gift/%s" % (('').join(random.choices(string.ascii_letters + string.digits, k=16)))
    print('Code: %s' % (code))
    with open('nitro codes.txt', 'a') as f:
        f.write('%s\n' % (code))
print('here is your code enjoy! now you can close this window ')