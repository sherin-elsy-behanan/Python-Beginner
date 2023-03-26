#basic print
print("Hello World")   #either single or double quote for defining a string

#print something that is stored in a variable
#1
new = "Sherin"       #new is a string variable
print(new)

#2
new = "Sherin"
print("new") #error since a variable in quotes treated as string to print

#3 concationation of string and content of variables
string1= "Hi"
string2= "Hello"
print("Entered string is" + string1 + string2)

#input from user
n= input("Enter the age")
print("Age = "+age)

#knowing datatype 
mark = 7.4
print(type(mark))    #out will be class>> <datatype>

#Assigning boolean value
Is_girl = False     #capital f also capital t for true

#multiple line sting
print('''
Hi, this is sherin from CEC
''')                            #tripple quote is used

#string intentation,range and printing
string = 'Hai Everybody'
print(string[1])  #will print the character 'H' only
print(string[-1]  #will print last character only
print(string[ : ] #used to copy the full string
print(string[1:4] #print the frst intended letter 'a' to 4th indexed letter excluding the 4th one

#formated string
result=f'{frist} [{second}] is a coder'   #{} refrence to a hole can be added as a value of the variable
print(result)

#length of a string
string= "sherin"
print(len(string))  #length of the string will be returned

#methods(special purpose) upper(),lower(),titile(),find(),replace(),in()
string= "Jilebi is sweet"
print(string.upper())                    #out will be JILEBI
print(string.find('i'))                  #out will be index of "i"(frist 'i' is comsidered)
print(string.find('S'))                  #out will be -1
print(string.find("is"))                 #out will be starting index of the word "is"
print(string.replace('sweet','bitter'))  #out will be "Jilebi is bitter"
print('Jilebi' in string)                #out will be 'True' ie, Jilebi is present 
