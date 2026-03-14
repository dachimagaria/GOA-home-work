def reverse(st):
    st = st.split()
    string = ""

    for i in st[::-1]:
        string += i + " "

    return string[:-1]
        
    