print(" /t 9th Marksheet ")
num  =int(input('Enter value Marks Maths     :'))
num1 =int(input('Enter value Marks Urdu      :'))
num2 =int(input('Enter value Marks English   :'))
num3 =int(input('Enter value Marks Physics   :'))
num4 =int(input('Enter value Marks Chemistry :'))
num5 =int(input('Enter value Marks Sindhi    :'))
num6 =num+num1+num2+num3+num4+num5
num7 =int(num6/550*100)
print(num7)
print()
print("Subject        Marks         ObtainedMarks           percentage %")
print()
print ("Maths          100          "+ str(num) +"                       "              +str(num/100*100)  + '%') 
print ("Urdu           100          "+ str(num1)+"                       "              +str(num1/100*100) + '%') 
print ("English        100          "+ str(num2)+"                       "              +str(num2/100*100) + '%')  
print ("Physics        100          "+ str(num3)+"                       "              +str(num3/100*100) + '%')   
print ("Chemistry      100          "+ str(num4)+"                       "              +str(num4/100*100) + '%')  
print ("Sindhi          50          "+ str(num5)+"                       "              +str(num5/100*100) + '%')  
print ("_________________________________________________________________")
print ("Total Marks    550          "+ str(num6)                  )
print ("_________________________________________________________________")
print ("Total percentage :"+str(round(num7,2))+ " %" )
if(num7 >= 85 & num7 <= 100):
    print("Grade = A")
elif(num7 >= 65):    
    print("Grade = B")
elif(num7 >= 50):    
    print("Grade = C")
elif(num7 >= 40):    
    print("Grade = D")
else:   
    print("Grade = F")  





