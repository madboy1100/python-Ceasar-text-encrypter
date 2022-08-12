
text=input("welcome to encrypting program Enter plain text: ")
text=text.upper()
y=input("please enter your key : ")
x= input("If you want \"Ceasar Cipher\" enter 1 if you want \"Multiplicative Cipher\" enter 2 : ")


shift =int(y) # key

x=int(x)

encryption = ""
#Raveshe Ceasar Cipher
if(x==1):
    for c in text:

     if c.isupper():
        c_unicode = ord(c)
        c_index = ord(c) - ord("A")
        new_index = (c_index + shift) % 26
        new_unicode = new_index + ord("A")
        new_character = chr(new_unicode)
        encryption = encryption + new_character
    print("Plain text:",text)

    print("Encrypted text:",encryption)

#raveshe Affine Cipher
if(x==2):
    shift2=int(input("please Enter your 2nd key for Affine Cipher : "))
    for c in text:

     if c.isupper():
        c_unicode = ord(c)
        c_index = ord(c) - ord("A")
        new_index = (c_index*shift2 + shift) % 26
        new_unicode = new_index + ord("A")
        new_character = chr(new_unicode)
        encryption = encryption + new_character
    print("Plain text:",text)

    print("Encrypted text:",encryption)
   # gathered and written by seyed hadi eshaghpour
   # i also take a look and help from StackOverFlow and my friend



