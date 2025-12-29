

words = ["gega" , "rezi" ,"dachi" , "Goga" , "monkey"]
i = 0
while i < len(words):
    if words[i] == words[i].lower():
       words[i] = words[i].upper()
       i += 1
    else: 
        words.pop(i)

print(words)
        
        






