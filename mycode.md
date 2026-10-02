# print ("Welcome to the Contact Book CLI")

contacts=[]

def add_contact(name,phone,email) :
    print("Enter contact details : ")
    name=input(print("Enter name : "))
    phone =int (input (print ("Enter phone number: ")))
    email=input(print("Enter email : "))

    for contact in contacts :
        contact {
        "name" : "name"
        "phone" : "phone"
        "email" : "email"
        }
        contacts.append()

## Attempt 2 - add_contact()

Mistake:
I passed name, phone, and email as function parameters even though the function should collect user input itself.

Lesson:
A function should have a clear responsibility. add_contact() should create a contact by taking input, creating a dictionary, and storing it.

Mistake:
I initially used a loop while creating a contact.

Lesson:
Loops are needed when working with existing contacts (search/update/delete), not when creating a new contact.


## Attempt 3 - add_contact completed

Mistakes fixed:
- Removed unnecessary function parameters.
- Removed incorrect loop while creating a contact.
- Correctly created dictionary and appended it into contacts list.

Learning:
A contact is represented as a dictionary.
Multiple contacts are stored inside a list.

## Attempt 4 - Understanding loops

Mistake:
I thought view_contacts() needed a loop for searching.

Lesson:
Loops are used for iteration (going through all items). Searching requires conditions to find a specific item.

Mistake:
I thought dictionary values could be accessed using dot notation like contact.name.

Lesson:
Dictionaries use keys:
contact["name"]

Dot notation is used with objects/classes.



def view_contacts() :
    for contact in contacts :
        # print(["name"] : ["phone"])
        print(["name"])
        print(["phone"])

 ## Attempt 5 - view_contacts()

Mistake:
I wrote print(["name"]) instead of accessing the dictionary key.

Lesson:
When working with dictionaries, values are accessed using:
dictionary["key"]

Example:
contact["name"]

Mistake:
I confused iteration with receiving input.

Lesson:
view_contacts() does not receive individual contacts. It receives/uses the contacts collection and iterates through each record.

def view_contacts() :
    user=0
    print("Heres the complete list of contacts ")
    for contact in contacts :
        
        user+=user
        print(f"Usser : {user}")
        print("Name :  ",contact["name"])
        print("Phone : " ,contact["phone"])
        print("Email : ", contact["email"])
view_contacts()

## Attempt 6 - view_contacts improvements

Mistake:
Used user += user instead of user += 1.

Lesson:
+= means add the right side value to the existing variable.
For counting, we increase by 1.

Mistake:
Variable name "user" was confusing because it represented contact number.

Lesson:
Good variable names make code easier to understand and maintain.

## Attempt 7 - Search Contact Logic

Learning:
Searching requires two things:
1. Loop to check every item.
2. Condition to compare the required value.

Pattern:
for item in collection:
    if condition:
        do something

Important:
A loop only repeats. The if statement makes decisions.

def search_Contact():
    found=False
    iname=input("Enter the contact's name : ")
    for contact in contacts :
        if iname==contact["name"]:
            found=True
            print("Contact Found :  ")
            print(contact)
        else:
            if found==False:
             print("Contact not found ")
search_Contact()


## Attempt 8 - Search Contact

Mistake:
I placed "Contact not found" inside the loop.

Lesson:
A search is only unsuccessful after checking the entire collection.

Correct pattern:
Loop through all items first.
After the loop, decide if something was found.

Mistake:
Used search_Contact instead of search_contact.

Lesson:
Python naming convention uses lowercase snake_case for functions.

## Attempt 8 - Search Logic Deep Understanding

Concept:
A normal if/else inside a loop checks one item at a time.

Mistake:
Using else inside the loop for "not found".

Lesson:
A search can only fail after checking the complete collection.
A flag variable like found = False stores the final state.

Pattern:

found = False

loop:
    if match:
        found = True

after loop:
    if not found:
        item does not exist

        Important:

if/else:
Makes decisions for one condition.

for loop:
Repeats work for every item.

A loop does not stop when it reaches else.
The else executes only for the current iteration.

Search failure can only be decided after checking every item.

## Attempt 9 - break

Learning:
break exits the entire loop immediately.

Used when the required item is found and continuing the loop is unnecessary.

Difference:
continue = skip current iteration
break = stop the whole loop