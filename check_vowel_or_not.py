#python program - check vowel or not

ch = input("enter any character: ")
ch1=str.upper(ch)
if(ch1=='A' or ch1=='E' or ch1=='I' or ch1=='O' or ch1=='U'):
    print(ch, "is a vowel.")
else:
    print(ch, "is not a vowel.")
    
print("End of the program")    
