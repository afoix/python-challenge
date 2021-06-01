# test letters a,6,b,3,c,5,d,1,e,3,b,4
string = str(input("Give me your sequence with coma:"))
string = string.replace(',', '')
number = 0
letter = ''
list_of_letters = []
string_same_letter = ''

for character in string:
    if not character.isdigit():
        letter = character
    else:
        number = int(character)
        string_same_letter = letter * number
        list_of_letters.append(string_same_letter)

print(''.join(list_of_letters))