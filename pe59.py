# #pe59.py
# XOR decryption
# Problem 59
# Published on 19 December 2003 at 06:00 pm [Server Time]
# Each character on a computer is assigned a unique code and the 
#preferred standard is ASCII (American Standard Code for Information 
#Interchange). For example, uppercase A = 65, asterisk (*) = 42, and 
#lowercase k = 107.

# A modern encryption method is to take a text file, convert the bytes 
#to ASCII, then XOR each byte with a given value, taken from a secret 
#key. The advantage with the XOR function is that using the same 
#encryption key on the cipher text, restores the plain text; for example, 
#65 XOR 42 = 107, then 107 XOR 42 = 65.

# For unbreakable encryption, the key is the same length as the plain text 
#message, and the key is made up of random bytes. The user would keep 
#the encrypted message and the encryption key in different locations, 
#and without both "halves", it is impossible to decrypt the message.

# Unfortunately, this method is impractical for most users, so the 
#modified method is to use a password as a key. If the password is 
#shorter than the message, which is likely, the key is repeated 
#cyclically throughout the message. The balance for this method is 
#using a sufficiently long password key for security, but short enough 
#to be memorable.

# Your task has been made easy, as the encryption key consists of three 
#lower case characters. Using p059_cipher.txt (right click and 'Save 
#Link/Target As...'), a file containing the encrypted ASCII codes, and the 
#knowledge that the plain text must contain common English words, 
#decrypt the message and find the sum of the ASCII values in the 
#original text.

#testing:
#65 XOR 42 = 107, then 107 XOR 42 = 65.
#print(65^42,'should be 107;',107^42,'should be 65')
#print(65^42,'should be 107;',107^42,'should be 65')
#print('122^65',122^65)

#Thoughts:  Could do frequency analysis of every third character, identify 
#probable " " and "e".  But just as well here to exhaustively try every
#key and look for common word(s) like "the"
def main():

    f = open('p059_cipher.txt', 'r')

    content = f.read()
    f.close()
    c=content.split(',')

    for i in range(len(c)):
        c[i]=int(c[i])
        #print(chr(c[i]))
    #print(ord('a'),ord('z'))
    #Note that ord('a') is 97, and ord('z') is 122.

    for k1 in range(97,123,1):
        for k2 in range(97,123,1):
            for k3 in range(97,123,1):
                m3=0
                d=[0]*len(c)
                for i in range(len(c)):
                    if(m3==0):
                        d[i]=c[i]^k1
                        if(d[i]not in (list(range(30,123,1)))):
                            break
                    elif(m3==1):
                        d[i]=c[i]^k2
                        if(d[i]not in (list(range(30,123,1)))):
                            break
                    elif(m3==2):
                        d[i]=c[i]^k3
                        if(d[i]not in (list(range(30,123,1)))):
                            break
                    m3=(m3+1)%3
                ds=""
                for i in range(len(d)):
                    ds=ds+chr(d[i])

                if('the' in ds and ds[-1]!=chr(0)):
                    print('key:',k1,k2,k3,'message:',ds)


    #by inspection, we find that the key is 101 120 112,
    #so, we decrypt using that key, then sum the ascii values
    m3=0
    k1=101
    k2=120
    k3=112
    d=[0]*len(c)
    for i in range(len(c)):
        if(m3==0):
            d[i]=c[i]^k1
        elif(m3==1):
            d[i]=c[i]^k2
        elif(m3==2):
            d[i]=c[i]^k3
        m3=(m3+1)%3
    print('The sum of the decrypted ascii values is:',sum(d))



def testing():    
    for k1 in range(0,128,1):
        print(k1,chr(k1))
    x=['t','h','e']
    s='the barking dog'
    print('the' in s)
#testing()
main()
