import hashlib

flag = 0
counter = 0

pass_hash = raw_input("Enter MD5 hash or SHA1 hash")

wordlist = raw_input("Enter Your Password file name :")

try:
    pass_file = open(wordlist, "r")
except:
    print("No File Found:")
    quit()

for word in pass_file:

    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()
    counter = 0

    if digest == pass_hash:
        print("PASSWORD CRACKED!!!!!")
        print("password Found")
        print("Password is " + word)
        flag=1
        break

    if flag == 0:
        print("password not found!!")
