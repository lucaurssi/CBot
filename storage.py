

def token_magic():
    try:
        f = open("token.env", "r")
        token = f.read()
        f.close()
        return token 
    except:
        token = input(f' please insert your discord token: ')
        f = open("token.env", "w")
        f.write(token)
        f.close()
        return token
        

def privilege():
    try:
        f = open("privilege.env", "r")
        aux = f.read()
        f.close()
        entitled_list = []
        for i in aux.split(','):
            entitled_list.append(i)
   
        return entitled_list 
        
    except:
        entitled_list = input(f'privilege.env not found, please insert your discord name:')
        f = open("privilege.env", "w")
        f.write(entitled_list)
        f.close()
        return entitled_list

def privilege_add(name, p_list):
    if name in p_list:
        return p_list
    
    p_list.append(name)
    
    f = open("privilege.env", 'a')
    f.write(',' + name)
    f.close()
    
    return p_list
    
    
def privilege_remove(name, p_list):
    if name not in p_list:
        return p_list
    
    p_list.remove(name)
    aux = p_list
    
    f = open("privilege.env", "w") # erase the file and prepare to re-write it
    f.write(p_list[0]) # write first member of the list
    p_list.pop(0)
    
    for i in p_list: # write the rest of the members
        f.write(',')
        f.write(i)
    f.close()
    
    return aux
   
    