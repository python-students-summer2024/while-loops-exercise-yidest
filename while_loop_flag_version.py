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
    keep_going=True
    while keep_going:
        if num==1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
            keep_going=False
        elif num==2:
            print("2 bottles of beer on the wall, 2 bottles of beer.")
            print("Take one down, pass it around, 1 bottle of beer on the wall.")
            print()
        else:
            print(str(num)+" bottles of beer on the wall, "+str(num)+" bottles of beer.")
            print("Take one down, pass it around, "+str(num-1)+" bottles of beer on the wall.")
            print()
        num-=1
    