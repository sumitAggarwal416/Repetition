""" I, Sumit Aggarwal, student number: 000793607, certify that all work
submitted is my own work, that I have not copied it from any other source. I
also certify that I have not allowed anyone else to copy my work.
"""

a=1
while a>=1:
    num1=int(input("Enter a number between 5 and 15(inclusive): "))
    if num1>=5 and num1<=15:
        num2=int(input("Enter a poistive number: "))
        product= num1*num2
        mod= product%60
        print('a'*mod)
        break
    else:
        print("Error! Please enter a number which is in the specified range!")

# This code does not prints the required sttring until and unless tbe user puts
# in a valid value, no matter how many times you put a wrong value.
