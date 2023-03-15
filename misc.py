import os
from datetime import timedelta, date

# Main file path
filePath = './bin/log/'

def returnTotals(FP):
    totalExp = 0.00
    totalInc = 0.00
    logs = []
    with open(FP, 'r', encoding='utf-8') as file:
        for line in file.readlines(): logs.append(line.strip('\n'))
    elements = [i.split(',') for i in logs]

    for el in elements:
        if el[0] == 'inc': 
            totalInc += float(el[3])
            totalInc = round(totalInc, 2)
        elif el[0] == 'exp': 
            totalExp += float(el[3])
            totalExp = round(totalExp, 2)

    totalBal = totalInc - totalExp
    return [str(totalExp), str(totalInc), str(totalBal)]

def getYearArr(FP):
    return [os.listdir(FP)[i] for i in range(len(os.listdir(FP)))]
def getMonthArr(FP):
    return [os.listdir(FP)[i] for i in range(len(os.listdir(FP)))]

# Function checking if provided number is float
def isNumber(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
# Create files depending on current year and month
def createFiles():
    thisYear = date.today().year
    filePath = './bin/log/' + str(thisYear)
    if not os.path.exists(filePath):
        os.makedirs(filePath)
    today = date.today()
    lastDayMonth = (date(today.year, today.month, 1) + timedelta(days=32) - timedelta(days=1)).day
    for day in range(1, lastDayMonth + 1):
        current_date = date(today.year, today.month, day)
        file_name = current_date.strftime('%B') + '.txt'
        fp = os.path.join(filePath, file_name)
        
        # Check if file for the current month already exists
        if not os.path.exists(fp):
            with open(fp, 'w') as file:
                file.write('Type,Place,Title,Amount\n')

# Function Saving to file
def saveToFile(line, FP):
    try:
        # Checking formatting
        line[3] = str(line[3]).replace(',', '.')
        if line[0]=='' or line[1]=='' or line[2]=='' or not isNumber(line[3]):
            print('Unable to save file')
            return
        
        # Checking if file exists
        if not os.path.exists(FP): 
            with open(FP, 'w') as f:
                f.write('Type,Place,Title,Amount\n')

        # Checking if file has heading
        with open(FP, 'r') as f:
            if f.readline() == 'Type,Place,Title,Amount\n':
                hasHeading = True
            else:
                hasHeading = False

        with open(FP, 'a', encoding='utf-8') as f:
            if hasHeading:
                f.write(','.join(line) + '\n')
            else:
                f.write('Type,Place,Title,Amount\n')
                f.write(','.join(line) + '\n')   

    except:
        print('Error occured while saving the file')