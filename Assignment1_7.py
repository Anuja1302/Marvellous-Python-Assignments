def new():
    Number=(int(input("Enter Number \n")))
    if Number%5 == 0:
        return True
    else:
        return False

ans=new()
print(ans)