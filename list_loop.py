# Loop into the items of loop and print them

days_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

for days in days_list:
    print(days)

length = len(days_list)

for num in range(0, length, 1):
    value = days_list[num]
    print(value)