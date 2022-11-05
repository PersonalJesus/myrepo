
inputfile  = "../user_name.txt"
outputfile = "../my_passwords.txt"

password_to_look_for = "mypass"

myfile = open(inputfile, mode='r', encoding='latin_1')           # doesn't open file, just create link for opening
myfile2 = open(outputfile, mode='a', encoding='latin_1')         # mode w purge data in file

for num, line in enumerate(myfile, 1):                           # enumerate lines by the numbers
    if password_to_look_for in line:
        print("Line N: " + str(num) + " : " + line.strip())
        myfile2.write("Found password: " + line)

myfile.close()
myfile2.close()
