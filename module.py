product=[]
def add():
    pid=int(input("enter product id:"))
    pnm=(input("enter product name:"))
    price=int(input("enter product price:"))
    d1={
        "pid":pid,
        "pname":pnm,
        "pprice":price
    }
    product.append(d1)
def display():
    print("=======================================")
    print("product_ID product_NAME product_PRICE")
    print("=======================================")
    for p1 in product:
        print(p1["pid"],"          ",p1["pname"],"          ",p1["pprice"])
def search():
    pid=int(input("enter PID:"))
    found=0
    for p1 in product:
       if p1["pid"] == pid:
        print("product is found")
        print("=======================================")
        print("product_ID product_NAME product_PRICE")
        print("=======================================")
        print(p1["pid"],"          ",p1["pname"],"          ",p1["pprice"])
        break
    if found == 0:
        print("Not Found")
def updateName():
    pid=int(input("enter PID which name u want to change:"))
    found=0
    for p1 in product:
        if(p1["pid"]==pid):
            found=1
            break
    if(found==1):
        print("product is found")
        pname=input("enter new product name")
        p1["pname"]=pname
        print("=======================================")
        print("product_ID product_NAME product_PRICE")
        print("=======================================") 
        print(p1["pid"],"          ",p1["pname"],"          ",p1["pprice"])
    else:
        print("Not Found")
def deletebyPId():
    pid=int(input("enter pid which name u want to delete"))
    found=0

    for p1 in product:
        if p1["pid"]==pid:
            product.remove(p1)
            found=1
            print("product is deleted successfully")
            break
    if found == 0:
        print("NOt Found")
def sortbyprice():
    if not product:
        print("no product available to sort.")
        return
    product.sort(key=lambda x : x["pprice"])
    print("product sorted by price succesfully!")
    display()
