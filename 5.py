CNP=str(input("CNPul persoanei: "))
if len(CNP) == 13:
    i=0
    while(i !=(CNP)) and (ord(CNP[i]) in range(48.59)):
        i += 1
    if i == len(CNP):
        print("CNPul a fost scris corect")
    else:
        print("CNPul a fost scris gresit")
else:
    print("CNPul a fost scris resit")
    
    