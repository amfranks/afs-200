import requests

class User():
    def __init__(self, firstName, lastName, emailAddress, username, password, UUID, phone, cell, pictureLarge, pictureThumbnail):
        self.firstName = firstName
        self.lastName = lastName
        self.emailAddress = emailAddress
        self.username = username
        self.password = password
        self.UUID = UUID
        self.phone = phone
        self.cell = cell
        self.pictureLarge = pictureLarge
        self.pictureThumbnail = pictureThumbnail

    ################################################### Define setters.

    def setFirstName(self, firstName):
        self.firstName = firstName

    def setLastName(self, lastName):
        self.lastName = lastName

    def setEmailAddress(self, emailAddress):
        self.emailAddress = emailAddress

    def setUserName(self, userName):
        self.userName = userName

    def setPassword(self, password):
        self.password = password

    def setUUID(self, UUID):
        self.UUIDs = UUID

    def setPhone(self, phone):
        self.phone = phone

    def setCell(self, cell):
        self.cell = cell

    def setPictureLarge(self, pictureLarge):
        self.pictureLarge = pictureLarge

    def setPictureThumbnail(self, pictureThumbnail):
        self.pictureThumbnail = pictureThumbnail

     ################################################### Define getters.

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getEmailAddress(self):
        return self.emailAddress

    def getUserName(self):
        return self.getUserName

    def getPassword(self):
        return self.getPassword

    def getUUID(self):
        return self.getUUID

    def getPhone(self):
        return self.getPhone

    def getCell(self):
        return self.getCell

    def getPictureLarge(self):
        return self.getPictureLarge

    def getPictureThumbnail(self):
        return self.getPictureThumbnail

    # Magic method to print object.
    def __str__(self):
        retStr = self.firstName
        retStr += self.lastName
        retStr += self.emailAddress
        return f"{self.firstName} {self.lastName}, {self.emailAddress}"


class AuthorizedUsers():
    def __init__(self):
        self.authorizedUsers = []

    def addAuthorizedUser(self, authorizedUser):
        self.authorizedUsers.append(authorizedUser)

    def showAuthorizedUsers(self):
        for authorizedUser in self.authorizedUsers:
            print(authorizedUser)

    def searchForAuthorizedUser(self, firstName):
        for authorizedUser in self.authorizedUsers:
            if (authorizedUser.getFirstName().lower() == firstName):
                return authorizedUser
        return None


# Get data from API
def getData():
    URL = "https://randomuser.me/api/?nat=us&results=10"

    try:
        response = requests.get(URL, timeout = 5)
        response.raise_for_status()
        response_JSON = response.json()
        return response_JSON

    # Handle exceptions.
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err) 

myAuthorizedUsers = AuthorizedUsers()   
jsonUserData = getData()

# Loop through all of the users that are returned stored under the key "results".
for currentUser in jsonUserData["results"]:
    firstName = currentUser["name"]["first"]
    lastName = currentUser["name"]["last"]
    emailAddress = currentUser["email"]
    username = currentUser["login"]["username"]
    password = currentUser["login"]["password"]
    uuid = currentUser["login"]["uuid"]
    phone = currentUser["phone"]
    cell = currentUser["cell"]
    pictureLarge = currentUser["picture"]["large"]
    pictureThumbnail = currentUser["picture"]["thumbnail"]

    newUser = User(firstName, lastName, emailAddress, username, password, uuid, phone, cell, pictureLarge, pictureThumbnail)
    myAuthorizedUsers.addAuthorizedUser(newUser)

# Print the list of Users in our AuthorizedUsers, separated by a new line.
myAuthorizedUsers.showAuthorizedUsers()