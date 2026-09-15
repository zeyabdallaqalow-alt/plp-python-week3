count = 1
total = 0

# BUG: The while statement was missing a colon, so I added it.
while count < 5:
    total = total + count
    count = count + 1

print("Sum of 1 to 5 is: " + total)
