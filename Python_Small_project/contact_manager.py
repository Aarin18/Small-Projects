'''# for i in range(11,1,-1):
#        print(i)                        #this what for loop is
#        brack 
#        continue 


# list [1,2,3,4,5,6]
# ["apple" , "happy"]

"""Numbers = [1 , 2 , 3 , 4 , 5]
print(Numbers[0])                        # this shows a place that we can write then we get the number or whatever at that place and same we will do with (-) negative number it start with the last one 
print(Numbers[len(Numbers) - 1])         # with len function 
Numbers.append("arin")"""                # if i want to add somthin in my code lately
{ }  this is for a dictionary                                                                    '''

import json


def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    person = {"name": name, "age": age, "email": email}
    return person


def display_people(people):
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])


def delete_contact(people):
    display_people(people)

    while True:
        number = input("Enter a number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number, out of range.")
            else:
                break
        except:
            print("Invalid number")

    people.pop(number - 1)
    print("Person deleted.")


def search(people):
    search_name = input("Search for a name: ").lower()
    results = []

    for person in people:
        name = person["name"]
        if search_name in name.lower():
            results.append(person)

    display_people(results)


print("Hi, welcome to the Contact Managament System.")
print()

with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]

while True:
    print()
    print("Contact list size:", len(people))
    command = input("You can 'Add', 'Delete' or 'Search' and 'Q' for quit: ").lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print("Peron added!")
    elif command == "delete":
        delete_contact(people)
    elif command == "search":
        search(people)
    elif command == "q":
        break
    else:
        print("Invalid command.")

with open("contacts.json", "w") as f:
    json.dump({"contacts": people}, f)
