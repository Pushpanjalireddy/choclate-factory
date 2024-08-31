def buy(chocolates):
    name=input("enter the name of chocolate")
    quantity=int(input("enter the quantity"))
    amount=0
    for chocolate in chocolates:
        if chocolates["name"]==name:
            if quantity<=chocolate["stock"]:
                amount=quantity*chocolate["amount"]
                chocolate["stock"]-=quantity
            else:
                print("out of sctock")
    return chocolates,amount
