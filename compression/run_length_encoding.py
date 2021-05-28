# example: aaaaaabbbcccccdeeebbbb
from itertools import chain

string = str(input('Insert your screen:'))
counter = 0
new_pairs = {}
previous_character = ''
lt_char_num = []
tuple_char_num = []

for character in string:
    if character == previous_character or previous_character == '' :
        counter = counter+1
    else:
        tuple_char_num = (previous_character, counter)
        lt_char_num.append(tuple_char_num)
        counter = 1
    previous_character = character

tuple_char_num = (previous_character, counter)
lt_char_num.append(tuple_char_num)
joined_str = ','.join(map(str, chain.from_iterable(lt_char_num)))
print(joined_str)