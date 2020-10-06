largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == 'done' : break
    try:
        inum = int(num)
    except:
        print('Invalid input')
        continue
    for num in [input]:
        if smallest is None:
            smallest = inum
        elif inum < smallest:
            smallest = inum
    for num in [input]:
        if largest is None:
            largest = inum
        elif inum > largest:
            largest = inum

print('Maximum is',largest)
print('Minimim is',smallest)
