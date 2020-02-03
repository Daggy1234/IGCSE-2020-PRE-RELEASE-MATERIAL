
    
x = ["Hatchback","Saloon   ","Estate   "]
y = [535000,495000,625000]
a = ["Set of Luxury Seats   ","Satellite navigation  ","Parking sensors       ","Bluetooth Connectivity","Sound system          "]
b = [45000, 5500, 10000, 350, 1000]
c = []
total = 0
print("-------------------------")
print("Sno|   Model   | prices |")
print("-------------------------")
while True:
    for k in range(0,3):
        print(" {} | {} | {} |".format(k+1,x[k],y[k]))
        print("-------------------------")
        k+=1
    m = int(input("Enter serial number of car model selected: "))
    if (m <0) or (m>3):
        print("PLEASE ENTER VALID SERIAL NUMBER FOR MODEL")
        break
    else:
        total += y[m-1]
        print("-"*38)
        print("|Sno|     Optional Extra     | Price |")
        print("-"*38)
        for i in range(0,5):
            if (b[i]>100) and (b[i]<1000):
                q= 2
            elif (b[i]>=1000) and (b[i]<10000):
                q = 1
            else:
                q = 0
            print("| {} | {} | {}{} |".format(i+1,a[i],b[i],q*" "))
            print("-"*38)
            i+=1
        while True:
            w = int(input("ENTER serial number of add on, enter 0 to exit: "))
            if w == 0:
                break
            elif (w<1)or(w>5):
                print("ENTER CORRECT SERIAL NUMBER FOR ADD-ON")
            else:
                c.append(w-1)
        print("MODEL: {}".format(x[m-1]))
        for j in range(0,len(c)):
            addon = b[c[j]]
            print("ADD-ON: {}".format(a[c[j]]))
            j+=1
        total += addon
        print("final amount is {}".format(total))
        
        while True:
            y  = str(input("Do you want a trade in y/n:"))
            if (y == "N") or (y == "n"):
                print("final amount is {}".format(total))
                trade = 0
                break
            elif (y == "Y") or (y == "y"):
                trade = int(input("EPMLOYEE ENTER TRADE IN VALUE: "))
                print("final amount is {}".format(total-trade))
                break
            else:
                print("ENTER y/n")
        
        final = float(total-trade)
        backprice = round(float(final *.99),2)
        fp = final-addon
        
        print('''
1.PAYMENT FULL AMOUNT
No of payments:1
Monthly amount: NA''')
        if fp<backprice:
            print('''
1.PRICE WITH FREE ADD-ON: {}
2.PRICE WITH CASHBACK: {}
DEALS: '''.format(fp,backprice))
        else:
            print('''
1.PRICE WITH CASHBACK: {}
21.PRICE WITH FREE ADD-ON: {}
'''.format(backprice,fp))
        
                  


        print('''
2.PAYMENT 4 years
No of payments:36
Cashback = NA
Monthly amount: {}
Final Amount: {}'''.format(round(final/36,2),final))
        syearprice = round(float(final *1.05),2)
        print('''
3.PAYMENT 7 years
No of payments:84
Cashback = NA
Monthly amount: {}
Final Amount: {}'''.format(round(syearprice/84,2),syearprice))

        break
        
              
        
                
                     
        


#19,20,15,22,12
# use while loop to enter upgrades and append to list c
