#!/usr/bin/env python3

"""

    Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
    Display the dictionary.
    Delete the entry for “cake”.
    Display the dictionary.
    Add an entry for “fruit” with “Mango” and display the dictionary.
        Display the dictionary keys.
        Display the dictionary values.
        Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
        Display whether or not “Mango” is a value in the dictionary (i.e. True).


"""

a_dict={"name":"Chris",
        "city":"Seattle",
        "cake":"Chocolate"}



def print_dict():
    """Output a dict"""

    print('[+] Printing out current dictionary: ')
    for k, v in a_dict.items():
        print(k, v)



print('[+] output the initial dictionary for display')
print_dict()

print('[+] remove some cake')
a_dict.pop('cake')

print_dict()

print('[+] add some fruit')
a_dict.update({'fruit':'mango'})

print_dict()

print('[+] show the keys')

for i in a_dict.keys():
    print(i)

print('[+] show the values')
for i in a_dict.values():
    print(i)


def are_you_in_dict(key, z_dict):
    """just to if key in z_zdict in the check"""
    if key in z_dict:
        return True
    else:
        return False

def are_you_true(b_value):
    """Print a message based on true / false of value"""

    if b_value == True:
        print('    [*] True: You must have my key!')

    if b_value == False:
        print('    [*]: False: Key does not exist')

'''example of checking boolean return in a function / don't do this in real life'''

print('[+] Does X exist in pair')
are_you_true(are_you_in_dict('name', a_dict))
print('[+] X does not exist in pair')
are_you_true(are_you_in_dict('frog', a_dict))


'''Simpler code examples here'''
print("[+] A simple use case to get true/false values")
print('name' in a_dict)
print('frog' in a_dict)


print('##################################################################')
print('[*] Dictionary 2 (sets) / working with sets')

"""

a_dict={"name":"Chris",
        "city":"Seattle",
        "cake":"Chocolate"}


Dictionaries 2

    Using the dictionary from item 1: Make a dictionary using the same
    keys but with the number of ‘t’s in each value as the value (consider upper and lower case?).

Sets

    Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
    Display the sets.
    Display if s3 is a subset of s2 (False)
    and if s4 is a subset of s2 (True).

Sets 2

    Create a set with the letters in ‘Python’ and add ‘i’ to the set.
    Create a frozenset with the letters in ‘marathon’.
    display the union and intersection of the two sets.
"""

t_set = set(['t','T'])

print('[-] set union/insec testing')
print(len(set.intersection(set("SeattleT"),t_set)))

a2_dict={"name": len(set.intersection(set(a_dict['city']),t_set)),
        "city": len(set.intersection(set(a_dict['city']),t_set)),
        "cake": len(set(set(a_dict['city']),t_set))
        }

for k, v in a2_dict.items():
    print(k, v)

print(a_dict['city'])
# print(set.intersection(set([a_dict['city']]),t_set)
print(len(set.intersection(set(a_dict['city']),t_set)))

#print(len(set.intersection(set(a_dict['city']),t_set)) - 1)

# a3_dict={"name": len(set.intersection(set(a_dict['city']),t_set)),
#         "city": 2,
#         "cake": 1}



#
