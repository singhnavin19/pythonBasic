#1. setdeafault

d1={10:"Ten",20:"Twenty",30:"Thirty"}
print(d1)
print(d1.setdefault(50,"fifty"))
print(d1)
print(d1.setdefault(50,"sixty"))


#2. update method
print("#2. update method start here")

d2={1:"One",2:"Two",3:"Three"}
d2.update({10:"Ten"})
print(d2)
d2.update({10:"Tin"})
print(d2)
print("#2. update method end here")

#[]
print("#2. [] start here")
d3={1:"One",10:"Ten"}
d3[1]="Onee"
print(d3)
d3[20]="Twenty"
print(d3)
print("#2. [] end here")
