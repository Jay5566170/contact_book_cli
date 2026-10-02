# print ("Welcome to the Contact Book CLI")

contacts=[]

def add_contact() :
    print("Enter contact details : ")
    name=input("Enter name : ")
    phone =input ("Enter phone number: ")
    email=input("Enter email : ")


    contact = {
        "name" : name,
        "phone" : phone,
         "email" : email
        }
    contacts.append(contact)
    print("Contact Added Successfully")
add_contact()
print(contacts)


def view_contacts() :
    Contact=0
    print("Heres the complete list of contacts ")
    for contact in contacts :
        
        Contact+=1
        print(f"Contact : {Contact}")
        print("Name :  ",contact["name"])
        print("Phone : " ,contact["phone"])
        print("Email : ", contact["email"])
view_contacts()


def search_contact():
    found=False
    iname=input("Enter the contact's name : ")
    for contact in contacts :
        if iname==contact["name"]:
            found=True
            print("Contact Found :  ")
            print(contact)
       
    if not found:
             print("Contact not found ")
search_contact()