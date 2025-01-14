import random
import string
codeOrDecode=int(input ("Enter 1 to code and enter 0 to decode "))
w=""
nw=""
ns=""
if codeOrDecode==1:
    mess=input("Enter the message which you want to change to secret message : ")
    mess=mess+' '
    for i in mess:
        if i!=' ':
           w=w+i
        else :
            if len(w)>=3:
                 nw=random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+w[1:len(w)]+w[0]+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
            else:
                nw=w.reverse()
            ns=ns+' '+nw
            w=""
            nw=""
    print("The coded form of your message is :",ns)
else:
    message=input("Enter the message which you wants to decode : ")
    message=message+' '
    for i in message:
        if i!=' ':
            w=w+i
        else:
            if len(w)<3:
                nw=w.reverse()
            else:
                nnw=w[3:len(w)-3]
                nw=nnw[len(nnw)-1]+nnw[0:len(nnw)-1]
            ns=ns+' '+nw
            w=""
            nw=''
            nnw=''
    print("The Decoded form of your message is :",ns)