import pandas as pd
import numpy as np

grosery = pd.read_csv("/Users/afoix/dango-git/python-challenges/green-grosery/greengrocer-sales-data.csv")

# What the total profit was for the week
grosery['Cost'] = grosery['Units bought'] * grosery['Purchase unit price']
grosery['Gain'] = grosery['Units sold'] * grosery['Sale unit price']
grosery['Total Gain'] = grosery['Gain'] - grosery['Cost']

total = grosery['Total Gain'].sum()

print("This is the total gain she made: ", total, end='\n\n')

# The names of the three kinds of item that generated the biggest profits,
# along with how much profit that was.
# They should be sorted so that the biggest profit is first,
# then the second biggest, then the third biggest.

Three_largest = grosery.nlargest(3, 'Total Gain')

print('These are the three kinds of item that generated the biggest gains')
print(pd.DataFrame(Three_largest), end='\n\n')

# The names of the three kinds of item that generated the biggest losses,
# along with how much loss that was.
# They should be sorted so that the biggest loss is first,
# then the second biggest, then the third biggest.

Three_lower = grosery.nsmallest(3, 'Total Gain')

print('These are the three kinds of item that generated the biggest losses')
print(pd.DataFrame(Three_lower))


