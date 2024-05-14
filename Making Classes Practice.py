#Anoushka Saha
#Making Classes Practice
#May 13th, 2024
#Day 17 Practice

#Making a class

class User:
    #Initialize starting values for attribute, which is called everytime a new object is created from this class
    #Name of parameter is same as attribute usually
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    #Method
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "anoushka")
user_2 = User("002", "anaya")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)