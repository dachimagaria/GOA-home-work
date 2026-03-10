def well(x):
    count = x.count('good')
    if count == 0:
        return "Fail!"
    elif count <= 2:
        return "Publish!"
    else:  
        return "I smell a series!"
    
