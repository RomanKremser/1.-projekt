# projekt_1.py: první projekt do Engeto Online Python Akademie
# author: Ŕoman Kremser
# email: rkremser@seznam.cz
# discord: chimera #+9734


# Slovník uživatelů a jejich hesel
USERS = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

# texty pro analýzu
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the IBM Almaden Research Center, we 
present research results in a wide range 
of areas, from nanotechnology to cloud 
computing. Our team comprises researchers 
in computer science, mathematics, physics, 
chemistry, materials science, and 
electrical engineering, all dedicated to 
advancing the state of the art in their 
respective fields.''',

'''The term "data science" has appeared 
relatively recently to specifically designate 
a set of principles and techniques to extract 
knowledge from data. In many cases, though, 
the term is used interchangeably with 
"machine learning," so we will use them 
interchangeably in this book. Of course, 
there are subtle differences between the two.''']

# ověření přihlašovacích údajů
# ověření přihlašovacích údajů
username = input('Username: ')
password = input('Password: ')
authenticated = False

if username in USERS and USERS[username] == password:
    authenticated = True

if not authenticated:
    print('Invalid username or password. Terminating the program..')
    exit()


# pozdrav uživatele a výběr textu
print('-' * 40)
print(f'Welcome to the app, {username}')
print(f'We have {len(TEXTS)} texts to be analyzed.')
print('-' * 40)
text_choice = input('Enter a number between 1 and 3 to select: ')
if not text_choice.isdigit() or int(text_choice) not in range(1, len(TEXTS) + 1):
    print('Invalid input or text number.')
    exit()

# analýza textu
text = TEXTS[int(text_choice) - 1]
words = text.split()
titlecase_words = [word for word in words if word.istitle()]
uppercase_words = [word for word in words if word.isupper()]
lowercase_words = [word for word in words if word.islower()]
numeric_strings = [word for word in words if word.isnumeric()]
numeric_sum = sum([int(word) for word in numeric_strings])

# četnost délek slov v textu
word_lengths = [len(word.strip(',.')) for word in words]
word_freq = {length: word_lengths.count(length) for length in set(word_lengths)}

# výstup
print('-' * 40)
print(f'There are {len(words)} words in the selected text.')
print(f'There are {len(titlecase_words)} titlecase words.')
print(f'There are {len(uppercase_words)} uppercase words.')
print(f'There are {len(lowercase_words)} lowercase words.')
print(f'There are {len(numeric_strings)} numeric strings.')
print(f'The sum of all the numbers {numeric_sum}')
print('-' * 40)
print('LEN|  OCCURRENCES  |NR.')
print('-' * 40)
for length in sorted(word_freq.keys()):
    print(f'{length:3}|{"*" * word_freq[length]} {word_freq[length]}')