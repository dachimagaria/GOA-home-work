def to_csv_text(array):
    string = ""
    
    for list in array:
        for i in list:
            string += str(i) + ","
        string = string[:-1]
        string += "\n"
                
    return string[:-1]
                