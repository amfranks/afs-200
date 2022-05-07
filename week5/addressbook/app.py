from flask import Flask, render_template, request
app = Flask(__name__)

import requests
import addressbook

# Get data from API
def getData():
    URL = "https://randomuser.me/api/?nat=us&results=25"

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

users = addressbook.AddressBook() 

@app.route("/")
def home():  
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

        newUser = addressbook.Contact(firstName, lastName, emailAddress, phone, pictureThumbnail)
        users.addAddress(newUser)

    return render_template('index.html', results = users.getAllAddresses())

@app.route("/search", methods=['GET', 'POST'])
def search():
    inputVal = request.form.get('search')

    if request.method == 'POST':
        print(inputVal)
        return render_template('index.html', results = users.findAllMatching(inputVal))
    else:
        return render_template('index.html', results = users.getAllAddresses())

if __name__ == "__main__":
    app.run()