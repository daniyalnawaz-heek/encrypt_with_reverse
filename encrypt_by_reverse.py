
message=str(input("Enter the text"))
 
#cipher text is stored in this variable
translated = '' 

#for loop for iteration
i = len(message) - 1

while i >= 0:
   translated = translated + message[i]
   i = i - 1
   
   
print("The cipher text is : ", translated)