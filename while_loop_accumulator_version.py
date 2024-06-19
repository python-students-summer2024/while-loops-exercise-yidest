def get_starting_number():
    whether_valid=0
    while whether_valid<1:
        num=input("How many bottles of beer on the wall?")
        if num.isdigit()==True:
            if int(num)>=1:
                whether_valid+=1
            else:
                whether_valid=whether_valid
        else:
            whether_valid=whether_valid
    return int(num)

def sing(num):
    while num>1:
        print(str(num)+" bottles of beer on the wall, "+str(num)+" bottles of beer.")
        if num-1>1:
            print("Take one down, pass it around, "+str(num-1)+" bottles of beer on the wall.")
        else:
            print("Take one down, pass it around, "+str(num-1)+" bottle of beer on the wall.")
        print()
        num-=1
    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take it down, pass it around, no more bottles of beer on the wall!")
