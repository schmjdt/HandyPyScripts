
def getSheetFromDrive(workbookName):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    # use creds to create a client to interact with the Google Drive API
    scope = ['https://www.googleapis.com/auth/drive.readonly']
    creds = ServiceAccountCredentials.from_json_keyfile_name('data/credentials.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    sheet = client.open(workbookName).sheet1

    return sheet

def getValuesFromSheet(sheetObj):
    '''Gets all values from a sheet and returns a list of lists.'''

    # Extract and print all of the values
    result = sheetObj.get_all_values()
    
    return result


def columnNum(col):
    from math import pow

    result = 0

    l = len(col)
    i = 0

    while l > 0:
        base = ord(col[i]) - 64
        result += pow(26, l - 1) * base

        l -= 1
        i += 1

    return int(result)

def getRowColData(data, startR, startC, lenR, lenC):

    if type(startC) == str:
        startC = columnNum(startC) 

    info = {'name': data[startR - 1][startC - 1], 'data': {}}

    for i in range(startR, startR + lenR):
        rK = data[i][startC - 1]
        info['data'].update({rK: {}})
        for ii in range(startC, startC + lenC):
            cK = data[startR - 1][ii]
            v = data[i][ii]
            info['data'][rK].update({cK: v})

    return info

def viewData(data):
    # print('Raw data:', data)
    #
    # print()
    # for d in data:
    #     print(d)
    
    advantageData = getRowColData(data, 5, 'B', 3, 4)

    print(advantageData)

    assert advantageData['data']['d2']['o3'] == '-1'
    assert advantageData['data']['d3']['o2'] == '-2'
    
    mishapData = getRowColData(data, 12, 'B', 3, 2)

    print(mishapData)

    assert mishapData['data']['4']['p1'] == 'nothing'
    assert mishapData['data']['2-3']['p2'] == 'bar'

def main():
    import pyFile

    _DATA_FILE = 'data/data.csv'

    if not pyFile.checkFileExists(_DATA_FILE):
        s = getSheetFromDrive('ExampleData')
        data = getValuesFromSheet(s)

        pyFile.saveData(_DATA_FILE, data)
    else:
        data = pyFile.readData(_DATA_FILE)
    
    viewData(data)


if __name__ == "__main__":
    main()