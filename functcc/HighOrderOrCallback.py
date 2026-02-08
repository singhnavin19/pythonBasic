def addPriceAndCalulateGSt(navin,*prices):
    sum=0
    for i in prices:
        sum+=i
    navin(sum)
def gstCalculate(price):
    print("Gst calculated on ",price," is 20 %")
varGstCalculate=gstCalculate
addPriceAndCalulateGSt(varGstCalculate,10,20,30)
