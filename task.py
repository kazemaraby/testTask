contractString = """enter contract type,
1-fixed term contract,
2-An unlimited contract period ,
 """
reasonString = """ 

The reason for ending the labor relationship ,
1-The termination of the contract or the agreement of the two parties to terminate the contract,
2-Termination of the contract from the employer,
3-Termination of the contract from the employer in one of the cases mentioned in Article 80,
4-Leaving work as a result of a forced force,
5-The worker terminates the employment contract within six months from the date of marriage or months from the date of delivery,
6-Leaving the worker to work in one of the cases mentioned in Article 81,
7-Termination of the contract by the worker or the worker leaving work in cases other than those mentioned in Article 81,
"""


while True:
    try:
        contractType=int(input(contractString))
    except ValueError:
        
        continue
    else:
        if(contractType >2):
            continue
        else:
            break

if(contractType ==2):
    reasonString +="""8-The worker resigns """

while True:
    try:
        reason=int(input(reasonString))
    except ValueError:
        continue
    else:
        if(reason >8):
            continue
        else:
            break
        


while True:
    try:
        salary =int(input("enter  your salary :"))
    except ValueError:
        continue
    else:
        break
        

while True:
    try:
        lengthofservice=int(input("enter your Length of service (years) :"))
    except ValueError:
        continue
    else:
        break 


while True:

    numberofmonth =input("number of month (optional) :")
    if not numberofmonth:
        break
    else:
        try:
            numberofmonth =int(numberofmonth)
        except ValueError:
            continue
        else:
            break    
    
            
while True:

    numberofdays = input("number of days (optional) :")
    if not numberofdays:
        break
    else:
        try:
            numberofdays =int(numberofdays)
        except ValueError:
            continue
        else:
            break     




if(type(numberofmonth) ==int):
    
    lengthofservice += (numberofmonth /12)
    

if(type(numberofdays) ==int ):
    
    lengthofservice += (numberofdays /365)

total = 0

if((reason == 1) or (reason == 2) or (reason == 4) or (reason == 5) or reason==6):
    
    if lengthofservice <=5:
        total =.5*salary*lengthofservice
        
    else:
        rest = lengthofservice -5
        total = (.5*5*salary ) +(rest *salary)



elif(reason ==3 or reason==7):
    total=0

elif(reason==8):
    if(lengthofservice <2):
        total =0
    elif (lengthofservice <=5 and lengthofservice >=2):
        total =(1/3) *(.5*salary*lengthofservice)
    elif ((lengthofservice >=5) and (lengthofservice < 10) ):
        rest = lengthofservice -5
        total = (2/3)*((.5*5*salary ) +(rest *salary))
    else:
         rest = lengthofservice -5
         total = (.5*5*salary ) +(rest *salary)


print("total = {}".format(total))
        


