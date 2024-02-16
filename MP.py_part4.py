#Author: Lahiru Lekamge
#Date: 14th November 2022

#Project: Progamming CW1

Pass = 0
Defer = 0
Fail = 0
Progress = 0
Trailer = 0
Retriever = 0
Exclude = 0

d = {}

response = 'Y'

while response == 'Y':

    while True:
        id_num = input("Please enter your id number:")
        try:
            Pass = int(input("Please enter your credits at pass:"))
            if Pass in range(0,140,20):
                Defer = int(input("Please enter your credits at defer:"))
                if Defer in range(0,140,20):
                    Fail = int(input("please enter your credits at fail:"))
                    if Fail in range(0,140,20):
                        if (Pass + Defer + Fail) !=120:
                            print("Total incorrect")
                            continue
                        
                    else:
                        print("Out of range")
                else:
                    print("Out of range")
            else:
                 print("Out of range")
                    
        except ValueError:
            print("Value error")
            continue
        break
    if Pass == 120:
        Credit= ("Progress")

    elif Pass== 100 and Defer == 20 or Pass == 100 and Fail == 20:
        Credit= ("Progress(module trailer)")

    elif Pass in range(60,100,20) or Defer in range(40,100,20) or Fail in range(40,80,20):
        Credit= ("Do not progress - module retriever")

    elif Fail in range(80,121,20):
         Credit= ("Exclude")
    d[id_num] = {}
    d[id_num] = Credit,Pass,Defer,Fail
      

    response = input("Would you like to enter another set of data?" )
    while response.upper() != "Y" and response.upper() != "Q":
     response = input("Would you like to enter another set of data?" )
print(d)
        
   
     
            



       



            
                            
                    
                                     
