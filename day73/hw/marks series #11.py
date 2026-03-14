def replace_exclamation(st):
    vowel = "aeiouAEIOU"
    string = ""
    

    
    for i in st:
        if i in vowel:
            string += "!"
        else:
            string += i
    
    return string
            