with open('compare.txt', 'r') as file:
    condition = file.read().splitlines()

mylist = ['a', 'ham', 'classification', 'there', 'dog', 'cheese']
mylist.sort(key=len, reverse=True)
print(mylist)