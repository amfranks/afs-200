class Contact():
    def __init__(self, firstName, lastName, emailAddress, phoneNumber, digitalPhoto):
        self.firstName = firstName
        self.lastName = lastName
        self.emailAddress = emailAddress
        self.phoneNumber = phoneNumber
        self.digitalPhoto = digitalPhoto

    ################################################### Define getters.

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getEmail(self):
        return self.emailAddress

    def getPhone(self):
        return self.phoneNumber

    def getPhoto(self):
        return self.digitalPhoto

    # Magic methods to print object.
    def __str__(self):
        return f"{self.firstName} {self.lastName}, {self.emailAddress}"
    def __repr__(self):
        return f"{self.firstName} {self.lastName}, {self.emailAddress}"

        
class AddressBook():
    def __init__(self):
        self.addresses = []
        
    def addAddress(self,address):
        self.addresses.append(address)
        
    def getAllAddresses(self):
        return self.addresses
    
    def findAllMatching(self,searchStr):
        results = []
        for address in self.addresses:
            
            if address.getFirstName().lower().startswith(searchStr.lower()) or address.getLastName().lower().startswith(searchStr.lower()):
                results.append(address)
                
        return results