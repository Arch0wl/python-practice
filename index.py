from turtle import backward


failed_subjects="exercise-bacics"

msg='welcome to Python 101: Strings'


# From the string "welcome to Python 101: Strings", extract text and create/ 
# print a new string that says "1 welcome Ring to Tyler"
# every first letter should be capitalize



msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:10]+' '+'Tyler'
print(msg1)
print(msg1.title())



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

