notes = int(input("Enter how many dollars you have"))
notes1 = (notes//100,)
notes2 = ((notes%100)//50)
notes3 = ((notes%100)%50)//10
print(notes1, " hundred dollar bills \n", notes2, "fifty dollar bills \n", notes3, "ten dollar bills")