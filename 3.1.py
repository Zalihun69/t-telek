main = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
numbers = []
while True:
    number = int(input('Adj meg egy számot a megadott intervallummal'))
    if number in main:
        numbers.append(main)
    else:
        print("Nincs benne az intervallumba")
        print(main)
        break
    
