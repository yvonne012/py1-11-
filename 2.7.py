scores = ['chris', 83, 'david', 96, 'bill', 92, 'amy', 59, 'james', 77]

#print(5*2)
#print(len(scores))

# name
for i in range(0, len(scores), 2):
    print(scores[i])
    
# score
for i in range(0, len(scores), 2):
    print(scores[i+1])
