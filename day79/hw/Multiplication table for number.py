def multi_table(number):
    string = ""   
    for i in range(1 , 11):
        string += str(i) + " * " + str(number) + " = " + str(i * number) + "\n"       
    return string[:-1]