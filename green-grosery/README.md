# Green grosery
I'm attaching a CSV file that contains data for one week of sales from my local greengrocer's shop. 

For all the different fruits and vegetables that she sells, the CSV file tells you:
* How many she bought from the suppliers that week
* What price she paid for each one
* How many of the things she bought that she actually sold
* What price she charged her customers for each one.

So for example, `Apple,30,2.37,16,3.24` means that she bought 30 apples from her supplier at £2.37 each (costing her a total of 30 x £2.37 = £71.10), then sold 16 of them at £3.24 (making a total of £51.84), so her overall profit on apples that week was -£19.26.

**What I want you to do is**: write a program which prints out a report from this data. The report should say:
* What the total profit was for the week
* The names of the three kinds of item that generated the biggest profits, along with how much profit that was. They should be sorted so that the biggest profit is first, then the second biggest, then the third biggest.
* The names of the three kinds of item that generated the biggest losses, along with how much loss that was. They should be sorted so that the biggest loss is first, then the second biggest, then the third biggest.