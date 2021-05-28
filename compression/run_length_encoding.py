

# **What I want you to do, part 1**:
# Write a program which RLE encodes an input string.
# I want to type in something like `aaaaaabbbcccccdeeebbbb` ,
# and the program should print out `a,6,b,3,c,5,d,1,e,3,b,4`
# It should work for any input that is at least 1 character long.

# I want to take the first character and compare with the follow characters until it's a different character
# I want to save in a variable (counter) how many time the character is the same
# stop when character is different

# Code to use
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
print(lt_char_num)