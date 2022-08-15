from itertools import count


failed_subjects="5"

msg = 'Welcome to it\'s Python 101: Strings'

print(msg, msg)
print(msg.upper())

print(msg.lower())
print(msg.capitalize()) #Welcome capitalize
print(msg.title()) #all words capitalize


print(len(msg)) #to find the lenght
print(msg.count('Python')) #to find the # of 'Python'
print(msg.count('n')) #to find the # of 'n'

# slicing
print(msg[6]) 

# slicing
print(msg[29]) 

# slicing
print(msg[29 : ]) # : everything after 29

# slicing with endpoint
print(msg[12 : 33]) # : everything after 12 takes up to 33

# slicing with endpoint
print(msg[ : 30]) # : everything started from 0 up to 30