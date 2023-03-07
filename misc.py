import os
from datetime import timedelta, date

# Main file path
filePath = './bin/log/'

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
def saveToFile(line, YM_input=None):
    try:
        # if YM_input==None:
        #     # File path config
        #     thisMonth = date.today().strftime('%B')
        #     thisYear = date.today().strftime('%Y')
        #     filePath = './bin/log/' + str(thisYear)
        #     if not os.path.exists(filePath): os.makedirs(filePath)
        #     filePath = filePath + '/' + str(thisMonth) + '.txt'
        # else:
        #     filePath = './bin/log/' + YM_input + '.txt'
        
        # File path config
        thisMonth = date.today().strftime('%B')
        thisYear = date.today().strftime('%Y')
        filePath = './bin/log/' + str(thisYear)
        if not os.path.exists(filePath): os.makedirs(filePath)
        filePath = filePath + '/' + str(thisMonth) + '.txt'
    
        # Checking formatting
        if line[0]=='' or line[1]=='' or line[2]=='' or isNumber(line[3]):
            print('Unable to save file')
            return
        line[3] = str(line[3]).replace(',', '.')
        
        # Checking if file exists
        if not os.path.exists(filePath): 
            with open(filePath, 'w') as f:
                print(1)
                f.write('Type,Place,Title,Amount\n')

        # Checking if file has heading
        with open(filePath, 'r') as f:
            if f.readline() == 'Type,Place,Title,Amount\n':
                hasHeading = True
            else:
                hasHeading = False

        with open(filePath, 'a', encoding='utf-8') as f:
            if hasHeading:
                f.write(','.join(line) + '\n')
            else:
                f.write('Type,Place,Title,Amount\n')
                f.write(','.join(line) + '\n')   
    except:
        print('Error occured while saving the file')