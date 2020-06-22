class Person:
    def __init__(self, first, last, mob_num, email):
        self.firstName = first
        self.lastName = last
        self.id = mob_num
        self.email = email
        self.friends = []
        # if access == "customer":
        #     self.previ = "customer"
        # elif access == "staff":
        #     self.previ = "admin"


    def add_friend(self, friend):
        if len(self.friends) < 10 and len(friend.friends) < 10:
            self.friends.append(friend) # p1 is addimg p2 in his friends list
            friend.friends.append(self) # p2 is adding p1 in his friends list

    def getCustomerList(self):
        '''
        @name   : getCustomerList
        @param1 : NA
        @desc   : this is previleged method, only consumable to staff/admin
        @return : None
        '''
        #since we do not store information in DB, admin previleged guys cannot able to retrieve data which stands in iterpreter.
        pass

    def getFriends(self):
        print (len(self.friends))
        for i in self.friends:
            print (i)


p1 = Person("David", "Wolber", "922-43-9873", "wolber@usfca.edu")
p2 = Person("Bob", "Jones", "902-38-9973", "jones@usfca.edu")
p3 = Person("admin", "admin", "123", "admin.gmail.com")

print(p1)

print(p2)

p1.add_friend(p2)



print (p1.firstName)
print (list(p1.friends))
print(p1.friends[0].firstName)

print (p1.getFriends())
