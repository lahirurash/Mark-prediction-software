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

Progress_list = []
Module_trailer_list = []
Module_retriever_list = []
Exclude_list = []

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
    if Total !=120:
        print("out of range! ")
    else:
       if Pass == 120:
           print("Progress")
           Progress = Progress + 1
           Progress_list.append(Pass)
           Progress_list.append(Defer)
           Progress_list.append(Fail)

       elif Pass == 100:
           print("Progress (module trailer)")
           Trailer = Trailer + 1
           Progress = Progress + 1
           Module_trailer_list.append(Pass)
           Module_trailer_list.append(Defer)
           Module_trailer_list.append(Fail)

       elif Pass == 80:
           print("Module retriever")
           Retriever = Retriever + 1
           Module_retriever_list.append(Pass)
           Module_retriever_list.append(Defer)
           Module_retriever_list.append(Fail)

       elif Pass == 60:
           print("Module retriever")
           Retriever = Retriever + 1
           Module_retriever_list.append(Pass)
           Module_retriever_list.append(Defer)
           Module_retriever_list.append(Fail)

       elif Pass == 40:
            if Fail == 80:
                print("Exclude")
                Excluded = Excluded + 1
                Exclude_list.append(Pass)
                Exclude_list.append(Defer)
                Exclude_list.append(Fail)
            else:
                print("Modulr retriever")
                Retriever = Retriever + 1
                MOdule_retriever_list.append(Pass)
                MOdule_retriever_list.append(Defer)
                MOdule_retriever_list.append(Fail)
       elif Pass == 20:
            if Defer >= 40:
                print("Module retriever")
                Retriever = Retriever + 1
                Module_retriever_list.append(Pass)
                Module_retriever_list.append(Defer)
                Module_retriever_list.append(Fail)
            else:
                print("Exclude")
                Excluded = Excluded + 1
                Exclude_list.append(Pass)
                Exclude_list.append(Defer)
                Exclude_list.append(Fail)


       else:
            if Pass == 0:
                if Defer >= 60:
                    print("Module retriever")
                    Retriever = Retriever + 1
                    MOdule_retriever_list.append(Pass)
                    MOdule_retriever_list.append(Defer)
                    MOdule_retriever_list.append(Fail)
                else:
                    print("Exclude")
                    Excluded = Excluded + 1
                    Exclude_list.append(Pass)
                    Exclude_list.append(Defer)
                    Exclude_list.append(Fail)


    Flag_credit = False
    Flag_defer = False
    Flag_fail = False

    print()


    print("Would you like to enter another set of data?")
    Another_set = input("Enter 'Y' for yes or 'Q' to quit and view results : ")


    print()


# Display progress

p_length = int(len(Progress_list) / 3)

a = 0

for i in range(p_length):
    print("Progress - ",Progress_list[a],",",Progress_list[a+1],",",Progress_list[a+2])
    
    a = a + 3

# Display module trailer

mt_length = int(len(Module_trailer_list) / 3)

b = 0

for i in range(mt_length):
    print("Progress (Module trailer) - ",Module_trailer_list[b],",",Module_trailer_list[b+1],",",Module_trailer_list[b+2])
    b = b + 3

# Display module retriever

mr_length = int(len(Module_retriever_list) / 3)

c = 0

for i in range(mr_length):
    print("Module retriever - ",Module_retriever_list[c],",",Module_retriever_list[c+1],",",Module_retriever_list[c+2])
    c = c + 3

# Display Exclude

e_length = int(len(Exclude_list) / 3)

d = 0

for i in range(e_length):
    print("Exclude - ",Exclude_list[d],",",Exclude_list[d+1],",",Exclude_list[d+2])
    d = d + 3
    


    

    
        
        
 

  

