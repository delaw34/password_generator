#password generator application
#user enters numbers of paasword required
#user enters lenght of password required


import random
uppercase = "ABCEDEFGHIJKLIMNOP"
lowercase = "abcdfeghijklomopq"
numbers = "1234567890"
symbols = "$%^^&*()$#@!"

all_seq = uppercase + lowercase + numbers + symbols

def password_gen():
    while 1:
        password_lenght = int(input("enter your lenght of password required here:  "))
        numbers_of_password = int(input("enter numbers of password required here:  "))
        for x in range(numbers_of_password):
            mypassword = ""
            for x in range(password_lenght):
                password_random = random.choice(all_seq)
                mypassword = password_random + mypassword
            print("this is the password you generated", mypassword) 
   
    
password_gen()