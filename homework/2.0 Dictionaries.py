'''
1. Read in the files in this zip file to create one dictionary with the English terms as the key and the French, German and Spanish terms as the corresponding values (DO NOT MANUALLY TYPE IN THE KEY/VALUE PAIRS).
2. Based on the dictionary created 
a. Allow the user to enter an English word/phrase and output the corresponding 3 translations. If the user enters a phrase that has no corresponding translation, output a "Translations not found" message.
b. Allow the user to enter a new English word/phrase and the translations for it. Write the new word/phrase and translations to their respective files. The user should be able to search for and see the translations of any new words entered.
'''
print('welcome to the translator')

process = input('Start? Y/N: ').upper()

while process == 'Y':

    french_d = {}
    with open('french.txt', 'r') as french:
        lines = french.readlines()

    for item in range(0, len(lines), 2):
        key = lines[item].strip()
        value = lines[item+1].strip()
        french_d[key] = value

    german_d = {}

    with open('german.txt', 'r') as german: 
        lines = german.readlines()

    for item in range(0, len(lines), 2):
        key = lines[item].strip()
        value = lines[item+1].strip()
        german_d[key] = value


    spanish_d = {}

    with open('spanish.txt', 'r') as spanish:
        lines = spanish.readlines()

    for item in range(0, len(lines), 2):
        key = lines[item].strip()
        value = lines[item+1].strip()
        spanish_d[key] = value


    translator = {}

    for key in french_d.keys():
        translator[key] = french_d[key], german_d[key], spanish_d[key]

    print(translator)

    phrase = input('What phrase are you looking to transalte? ')

    match = False
    for key, value in translator.items():
        if key == phrase:
            value_clean = ', '.join(str(n) for n in value)
            print()
            print('the matching translations are: ')
            print(f'{key}: {value_clean}')
            match = True

    if not match:
        print()
        print('Translations not found')

    choice = input('would you like to enter a new english phrase? Y/N ').upper()

    if choice == 'Y':
            english_phrase = input('what is the english phrase: ')
            french_phrase = input('whats its french translation? ')
            german_phrase = input('whats its german translation? ')
            spanish_phrase = input('whats its spanish translation? ')


            with open('french.txt', 'a') as french:
                french.write(english_phrase + '\n')
                french.write(french_phrase + '\n')

            with open('german.txt','a') as german:
                german.write(english_phrase + '\n')
                german.write(german_phrase + '\n')
        
            with open('spanish.txt','a') as spanish:
                spanish.write(english_phrase + '\n')
                spanish.write(spanish_phrase + '\n')        

            



    else:
        print("thanks bye")
        process = 'N'
