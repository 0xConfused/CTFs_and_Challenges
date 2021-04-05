def main():
    
    print("start:")
    password = [42]*32
    
    for c in range(len(password)):
        password[c] = chr(password[c])
        print(password[c], end="")
    print()
        
    buffer = "jU5t_a_sna_3lpm12g94c_u_4_m7ra41"

    for i in range(31,16,-2):
        password[i] = buffer[i]
        
    test(password)

    for i in range(30,15,-2):
        password[i] = buffer[46-i]
        
    test(password)
        
    for i in range(15,7,-1):
        password[i] = buffer[23-i]
        
    test(password)
        
    for i in range(7,-1,-1):
        password[i] = buffer[i]
        
    for c in range(len(password)):
        print(password[c], end="")
    print()
        
    test(password)
    createfile(password)
    
    print("end")
    
def test(password):
    for c in range(len(password)):
        print(password[c],end="")
    print()

def createfile(password):
    file1 = open("picoCTFvaultdoor3.txt","a")
    str1=""
    for s in range(len(password)):
        str1 += password[s]
    file1.write(str1)
    file1.close() 
    
    
if __name__=="__main__":
    main()
    
