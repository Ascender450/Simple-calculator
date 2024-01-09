print("What do you pick 1=+ 2=* 3=/ 4=-")
pick = int(input("Enter one of the options: "))
first_num = int(input("enter a number  "))
sec_num = int(input("enter a number  "))


if pick == 1:
    print(first_num + sec_num)

elif pick == 2:
    print(first_num * sec_num)

elif pick == 3:
    print(first_num / sec_num)

elif pick == 4:
    print(first_num - sec_num) 