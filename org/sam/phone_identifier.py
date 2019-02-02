


def abc():
    print ("hello")
    
def is_phone(ph):
    
    l = len(ph)
    
    
    if (l == 10): 
        if (ph.isdigit()):
           
            p_first = ph[0]
            p = int(p_first)
        
            if (p == 7 or p == 8 or p == 9):
                print("the phone number is valid")
                print("yes")
            else:
                print("this is not a valid number")
        else:
            print("no, there is a character")
        
    else:
        print("no, there aren't 10 digits")


     
def is_phone_1(ph):
    
    l = len(ph)    
    
    if (l == 10): 
        if (ph.isdigit()):
           
            p_first = ph[0]
            p = int(p_first)
        
            if (p == 7 or p == 8 or p == 9):
                print("the phone number is valid")
                print("yes")
                return True
            else:
                print("this is not a valid number")
                return False
        else:
            print("no, there is a character")
            return False
        
    else:
        print("no, there aren't 10 digits")
        return False

def is_phone_2(ph):
    
    l = len(ph)   
    
    if (l != 10):
        return False
    
    if not (ph.isdigit()):
        return False
       
    p_first = ph[0]
    p = int(p_first)

    if (p == 7 or p == 8 or p == 9):
        #print("the phone number is valid")
        
        return True
    
    #print("this is not a valid number")
    return False
    


if __name__ == "__main__":
    #abc()
    
    #is_phone('1896540318')
    
    phone_or_not = is_phone_2('1896540318')
    print(phone_or_not)
    