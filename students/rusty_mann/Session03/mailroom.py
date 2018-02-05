
donors = [["Allen, Paul", [1000000, 50000, 300000]], 
                    ["Gates, Bill", [5000000, 80000, 700000]], 
                    ["Bezos, Jeff", [30000]], 
                    ["Musk, Elon", [1000000, 30000]], 
                    ["Zuckerberg, Mark",[10000, 50000, 12000, 400000]]]

#def sort_donors():

def make_report(donor):
    donor_sort = sorted(donor, key=lambda don: sum(don[1]), reverse=True)
    #print(donor_sort)
    col_names = ["Donor Name", "| Total Given", "| Num Gifts", "| Average Gift"]
    headers = f'{col_names[0]:20}{col_names[1]:>15}{col_names[2]:^15}{col_names[3]:20}'
    print(" ")
    print(headers)
    print(("_")*65)
    print((" "))
    for n in range(len(donor_sort)):
        columns = f'{(donor_sort[n])[0]:20}{sum((donor_sort[n])[1]):15.2f}{len((donor_sort[n])[1]):^15}{(sum((donor_sort[n])[1])/len((donor_sort[n])[1])):12.2f}'
        print(columns)
    init_prompt()
#make_report(donor_sort)


def donation_amount(donor):
    don_amt = input("Please enter a donation amount: ")
    if don_amt == "quit":
        init_prompt()
    for n in range(len(donors)):
        if (donors[n])[0] == donor:
            (donors[n])[1].append(int(don_amt))
            #return donors
    #print(donors)
    thank_you_email(donor, don_amt)
    init_prompt()
    #print(donors)


def add_donor(new_donor):
    donors.append(new_donor)
    new_donor.append([])


def choose_donor():
    new_don = []
    choose_don = input("Please enter a donor name in the form: Last_name, First_name: ")
    if choose_don == "quit":
        init_prompt()
    for n in range(len(donors)):
        if donors[n][0] == choose_don:
            donation_amount(choose_don)
    else:
        new_don.append(choose_don)
        add_donor(new_don)
    donation_amount(choose_don)


def show_list():
    abc_sort = (sorted(donors, key=lambda donor: donor[0]))
    for n in range(len(abc_sort)):
        print((abc_sort[n])[0])


def thank_you_email(donor, amount):
    print(f"Dear {donor}, thank you for your donation of {amount}. You are a good person")


def work_flow(response):
    valid_response = ["1", "2", "3", "list"]
    while response not in valid_response:
        print("Please choose a valid response: ")
        init_prompt()
    if response == "list":
        show_list()
        init_prompt()
    elif response == "1":
        choose_donor()
    elif response == "2":
        make_report(donors)
    else:
        if response == "3":
            quit()


def init_prompt():
    init_response = input("Would you like to, 1 Send a Thank You, 2 Create a Report, or 3 quit?")
    work_flow(init_response)

init_prompt()
