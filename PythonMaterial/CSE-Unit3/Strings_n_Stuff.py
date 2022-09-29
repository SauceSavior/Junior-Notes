"""
Data Types-
Primitive-
Boolean, intiger, etc.
Non-Primitive- String, Array, etc.
"""
#convert string use str()
age = str(15)
age = '15'
age = "15"

email="charity.baylor@evsck12.com"
#use substrings to get a portion of the string
username=email[0:email.index("@")]
domain=email[15:26]
firstname=email[0:7]
lastname=email[8:14]
print(username, domain, firstname, lastname)



number="123456"
print(number[:3])
print(2+2)
print("2"+"2")
print(2*3)
print("2"*3)
print(2*3)
print(2**3)
print("2"**3)
print("123"+"456"+str(789))

#quick trick to clear print(\n"*50)