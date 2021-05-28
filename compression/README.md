# Challenge 3: Compression algorithm
Here’s challenge #3.

When I was first learning programming on PC, writing games in DOS, I’d often need to work with image files. This was back before JPG and PNG… back then it was BMP or PCX. An interesting thing about PCX was that it supported compression, making the image files much smaller. The compression technique it used was called ‘run-length encoding.’
Suppose you’ve got a bunch of characters like this: `aaaaaabbbcccccdeeebbbb`. 
Run-length encoding compresses it that to: `[('a', 6), ('b', 3), ('c', 5), ('d', 1), ('e', 3), ('b', 4)]`. 
Each entry in the list tells you a character and how many times it was repeated. If there’s not a lot of repeated characters in the input the RLE might actually make a result which is bigger than the input, instead of smaller, but for inputs with a lot of repeated characters it can save a lot. Art for old DOS games often had a lot of big blocks of repeated pixels so RLE was pretty efficient :)

**What I want you to do, part 1**: Write a program which RLE encodes an input string. I want to type in something like `aaaaaabbbcccccdeeebbbb` , and the program should print out `a,6,b,3,c,5,d,1,e,3,b,4`
It should work for any input that is at least 1 character long.

**What I want you to do, part 2**: Write a program which RLE decodes the output from the first program. I want to give it something like `a,6,b,3,c,5,d,1,e,3,b,4`  as an input, and it should give me `aaaaaabbbcccccdeeebbbb`  as an output.