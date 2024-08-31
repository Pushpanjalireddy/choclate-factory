def add_chocolates(chocolates):
    name=input("enter the name of the cholate")
    amount=int(input("enter the amount"))
    stock=int(input("enter the stock"))
    chocolates={'name':name,'amount':amount,'stock':stock}
    chocolates.append(chocolate)
    return chocolates
def remove_chocolates(chocolates):
    name=input("enter the name of chocolates")
    for chocolate in chocolates[ : ]:
        if chocolate['name']==name:
            chocolates.remove(chocolate)
    return chocolates

def update_amount(chocolates):
    name=input("enter the name of chocolate")
    amount=int(input("enter the amount"))
    for chocolate in chocolates:
        if chocolate["name"]==name:
            chocolate["amount"]=amount
    return chocolates
def update_stock(chocolates):
    name=input("enter the name of chocolate")
    stock=int(input("enter the amount"))
    for chocolate in chocolates:
        if chocolate["name"]==name:
            chocolate["stock"]=stock
    return chocolates