def is_isogram(string):
    if string == "":
        return True
    
    str2 = "" 
    
    for i in string.lower():
        if i not in str2:
            str2 += i
    
    if str2 == string.lower():
        return True
    else:
        return False
        