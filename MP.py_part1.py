#Author: Lahiru Lekamge
#Date: 14th November 2022

#Project: Progamming CW1

Pass = 0
Defer = 0
Fail = 0
Total = 0
Another_set = 'Y'
Progress = 0
Trailer = 0
Retriever = 0
Excluded = 0
Flag_credit = False
Flag_defer = False
Flag_fail = False
Outcome_total = 0

while Another_set == 'Y':
    while Flag_credit == False:
        try:
            Pass = int(input("please enter your credit at pass : "))
            Flag_credit = True
            if Pass not in range(0,121,20):
                print('out of range')
                Flag_credit = False
        except ValueError:
            print('Integer Required')
            Flag_credit = False

    while Flag_defer == False:
        try:
            Defer = int(input("please enter ypur credits at defer : "))
            Flag_defer = True
            if Pass not in range(0,121,20):
                print('out of range')
                Flag_defer = False
        except ValueError:
            print('Integer Required')
            Flag_defer = False

    while Flag_fail == False:
        try:
            Fail = int(input("please enter your credits at fail: "))
            Flag_fail = True
            if Pass not in range(0,121,20):
                print('out of range')
                Flag_fail = False
        except ValueError:
            print('Integer Required')
            Flag_fail = False

    Total = Pass + Defer + Fail

    if Total != 120:
        print('Total incorrect')
    else:
        if Pass == 120:
            print("Progress")
            Progress = Progress + 1

        elif Pass == 100:
            print("Progress (module trailer)")
            Trailer = Trailer + 1

        elif Pass == 80:
            print("Do not Progress - module retriever")
            Retriever = Retriever + 1

        elif Pass == 60:
            print("Do not Progress - module retriever")
            Retriever = Retriever + 1

        elif Pass == 40:
            if Fail == 80:
                print("Excluded")
                Excluded = Excluded + 1
            else:
                print("Do not Progress - module retriever")
                Retriever = Retriever + 1

        elif Pass == 20:
            if Defer >= 40:
                print("Do not Progress - module retriv=ever")
                Retriever = Retriever + 1
            else:
                print("Excluded")
                Excluded = Excluded + 1

        else:
            if Pass == 0:
                if Defer >= 60:
                    print("Do not Progress - module retriever")
                    Retriever = Retriever + 1
                else:
                    print("Excluded")
                    Excluded = Excluded + 1

    Flag_credit = False
    Flag_defer = False
    Flag_fail = False

    print()

    print("Would you like to enter another set of data?")
    Another_set = input("Enter 'Y' for yes or 'Q' to quit and iew results : ")

    print()


print("Horizontal Histogram")

print("progress ",Progress," : ",Progress*"*")
print("Trailer ",Trailer," : ",Trailer*"*")
print("Retriever ",Retriever," : ",Retriever*"*")
print("Excluded ",Excluded," : ",Excluded*"*")

print()


Outcome_total = Progress + Trailer + Retriever + Excluded
print(Outcome_total,"Outcomes in total.")



                      

            

    







                
            


