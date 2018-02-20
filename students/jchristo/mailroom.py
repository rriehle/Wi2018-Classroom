#mailroom program
#program needs to do the following: “Send a Thank You”, “Create a Report” or “quit”
#!/usr/bin/env python3

#for saving files to user desktop
#import pathlib
#pth = "/Users/"/pathlib.Path.home() / "/Desktop/"
#pth = "/Users/Desktop/"

#initial list of donors
donor_db = {'Homer Simpson':[5,10,50],'Marge Simpson':[5,20,100],\
            'Lisa Simpson':[10,30,65],'Bart Simpson':[15,55,500],\
            'Maggie Simpson':[5,70,50]}

#using a varaible for the input seems to cause problems, value is retained throughout script which is not desired
user_prompt = int(input("Please Choose From the Following Options:"\
                        + "\n" + "1 - Send a Thank You" + "\n" + \
                        "2 - Create a Report" + "\n" +"3 - Send Letters to Everyone"\
                        +"\n" +"4 - Quit"))

menu_choice = user_prompt

#might need to change the below to a while loop
def doer(menu_choice):
    if menu_choice == 1:
        get_donor()
        get_donation(donor_name)
        write_note(donor_name,donation)
        #doer(menu_choice_2)
    elif menu_choice ==2:
        create_report()
        #doer(menu_choice_3)
    elif menu_choice == 3:
        send_letters()
        #the below causes a recursion error, max depth reached
        #doer(menu_choice_4)
    else:
        print("Exiting")

#Force lower then apply title caps to avoid errors
def get_donor():
    global donor_name
    donor_name = input("Please Enter the Donor's Full Name:")
    donor_name = donor_name.lower().title()
    if donor_name != "List":
        if donor_name in donor_db.keys():
            print("Existing Donor")
            return donor_name
        elif donor_name not in donor_db.keys():
            donor_db[donor_name] = []
            print("New Donor")
            return donor_name
    elif donor_name == "List":
        print(donor_db.keys())
        donor_name = input("Please Enter the Donor's Full Name:")
        donor_name = donor_name.lower().title()
        if donor_name in donor_db.keys():
            print("Existing Donor")
            return donor_name
        elif donor_name not in donor_db.keys():
            donor_db[donor_name] = []
            print("New Donor")
            return donor_name

def get_donation(donor_name):
    global donation
    donation = input("Please Enter the Donation Amount:")
    donation = int(donation)
    donor_db[donor_name].append(donation)
    #global total_donation
    #total_donation = sum(donor_db[donor_name])
    return donation

def write_note(donor_name,donation):
    print("Thank You {} for Your Generous Donation of: ${}".format(donor_name,donation))
    #global menu_choice_2
    #menu_choice_2 = user_prompt

def create_report():
    global menu_choice_3
    print("Donor Name "+""*4+"| Total Given | "+""*4+"Num of Gifts | "+""*4+"Avg Gift"+ "\n" + "-"*50)
    for k,v in sorted(donor_db.items(),key=lambda i:sum(i[1]),reverse=True):
        #need to figure out how to print avg as float in the code below
        print("{:<} ${:>10} {:>10} ${:>}".format(k,sum(v),len(v),(sum(v)/len(v))))
    #menu_choice_3 = user_prompt

def send_letters():
    global menu_choice_4
    for k,v in donor_db.items():
        file_name = k.replace(" ","_")
        f = (open("{}.txt".format(file_name),"w"))
        f.write("Dear {}, "+ "\n"\
                "Thank you for your very kind donation of {1}."+ "\n" +\
                "It will be put to very good use"+ "\n" +\
                "Sincerely,"+ "\n" + "-The Team".format(k,sum(v)))
    print("Letter Generation Complete")
    menu_choice_4 = user_prompt

doer(menu_choice)
print("this worked")
