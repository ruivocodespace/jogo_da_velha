tab = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def check_imp(tab2, simbol, int_user): 

    if int_user >= 0 and int_user < 9:
        if tab2[int_user] == " ":
            tab2[int_user] = simbol
        return True  
    return False