c = True
ct = 0

while c:
    c = int(input('Enter a card:'))

    if  c > 0 and c < 7:
        ct = ct + 1
        print (ct)
        print ("low card")

    elif c >= 7 and c < 10:
        ct = ct + 0
        print(ct)
        print("neutral card")

    elif c >= 10 and c < 12:
        ct = ct - 1
        print (ct)
        print("high card")


    if c == 0:
       c = False

print("\nrunning count: ",  ct)


#true count

n = float(input("enter # of decks :"))
truecount = n/ct
print("truecount =",truecount)
if truecount > 0.6:
    print("good count")
else: print("bad count")
#BJ cardcounter prototype 1.0

