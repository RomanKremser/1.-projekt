# projekt_1.py: první projekt do Engeto Online Python Akademie
# author: Ŕoman Kremser
# email: rkremser@seznam.cz
# discord: chimera #+9734
users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

TEXTS = [
    '''Situated about 10 miles west of Kemmerer, 
    Fossil Butte is a ruggedly impressive 
    topographic feature that rises sharply 
    some 1000 feet above Twin Creek Valley 
    to an elevation of more than 7500 feet 
    above sea level. The butte is located just 
    north of US 30N and the Union Pacific Railroad, 
    which traverse the valley.''',

    '''At the base of the butte, 
    the greenish sandstone and shale slope 
    downward into beds of rich fossil-bearing 
    rocks. Represented in these rocks are 
    numerous species of fossil plants and animals 
    from a time period called the Eocene.''',

    '''Fossil Butte National Monument preserves 
    the best paleontological record of Eocene 
    aquatic communities in North America and 
    possibly the world. Fossils preserved 
    in limestone include plants and animals 
    of the freshwater lake that covered the 
    area approximately 50 million years ago 
    as well as fish, insects, reptiles, birds 
    and mammals that lived in and around the lake.'''
]

# pozdrav uzivatele a pozvi ho k prihlaseni
username = input("username:")
password = input("password:")

if users.get(username) != password:
    print("Incorrect username or password, terminating the program..")
else:
    print(f"----------------------------------------\nWelcome to the app, {username}\We have 3 texts to be analyzed.\n----------------------------------------")

    # uzivatel si zvoli text k analyzovani
    text_index = input("Enter a number btw. 1 and 3 to select: ")
    if not text_index.isdigit() or int(text_index) not in [1, 2, 3]:
        print("Invalid input, terminating the program..")
    else:
        selected_text = TEXTS[int(text_index) - 1]
        words = selected_text.split()
        word_lengths = [len(word.strip(".,!?:")) for word in words]
        titlecase_words = [word for word in words if word.istitle()]
        uppercase_words = [word for word in words if word.isupper()]
        lowercase_words = [word for word in words if word.islower()]
        numeric_strings = [word for word in words if word.isnumeric()]
        numeric_values = [int(word) for word in words if word.isnumeric()]

        print(f"----------------------------------------\nThere are {len(words)} words in the selected text.\nThere are {len(titlecase_words)} titlecase words.\nThere are {len(uppercase_words)} uppercase words.\nThere are {len(lowercase_words)} lowercase words.\nThere are {len(numeric_strings)} numeric strings.\nThe sum of all the numbers {sum(numeric_values)}\n----------------------------------------")

        # vytvor sloupcovy graf
        word_length_count = {}
        for length in word_lengths:
            if length not in word_length_count:
                word_length_count[length] = 1
            else:
                word_length_count[length] += 1

        print("LEN|  OCCURENCES  |NR.")
        print("-" * 30)

       

for length, count in sorted(word_length_count.items()):
            stars = "*" * count
            print(f"{length:3}")