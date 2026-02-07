#positional or required
def calcGST(price,buyerState,sellerState):
    print("price=",price,buyerState,sellerState)
    if buyerState==sellerState:
        print("SGCT and CGST equally")
    else:
        print("IGST")
calcGST(10000,"MH","WB")
calcGST(10000,"MH","MH")

calcGST(price=100,sellerState="MH",buyerState="BH")
def calcGSTSameState(price=100,buyerState="MH",sellerState="MH"):
    print("price=",price,buyerState,sellerState)
    if buyerState==sellerState:
        print("SGCT and CGST equally")
    else:
        print("IGST")
calcGSTSameState() 

def sayHello(name,language="English"):
    print("hello",language,name)
sayHello("Navin")


