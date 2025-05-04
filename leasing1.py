from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["leasing_db"]
collection = db["listings"]

def menu():
    print(" Rental System")
    print("1. Add New Listing")
    print("2. View All Listings")
    print("3. Exit")

def add():
    print("Please enter the listing details:")
    data = {
        "Title": input("Title: "),
        "Description": input("Description: "),
        "Rent": input("Rent: "),
        "Address": input("Address: "),
        "Number of Rooms": input("Number of Rooms: "),
        "Contact Info": input("Contact Info: ")
    }
    collection.insert_one(data)
    print(" Listing added successfully.")

def show():
    print("All Listings ")
    listings = list(collection.find())
    if not listings:
        print("No listings found.")
        return
    for i, item in (listings, 1):
        print(f"Listing {i}")
        print(f"Title: {item.get('Title')}")
        print(f"Description: {item.get('Description')}")
        print(f"Rent: {item.get('Rent')}")
        print(f"Address: {item.get('Address')}")
        print(f"Number of Rooms: {item.get('Number of Rooms')}")
        print(f"Contact Info: {item.get('Contact Info')}")

while True:
    menu()
    choice = input("Select an option (1 or2 or3): ")
    if choice == "1":
        add()
    elif choice == "2":
        show()
    elif choice == "3":
        print(" Exiting. Goodbye!")
        break
    else:
        print("Please try again.")
