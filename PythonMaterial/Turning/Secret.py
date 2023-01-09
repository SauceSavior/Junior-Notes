

import random
from cryptography.fernet import Fernet
global d
x=input("y/n")
if x=="y":
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(b"welcome to geeksforgeeks")
    print(token)
    d = f.decrypt(token)
else:  
    print(d)