'''Helper module to handle simple file I/O.'''

def checkFileExists(filePath):
    '''Check if a path is a file.'''

    from os import path

    return path.isfile(filePath)

def saveData(filePath, data):
    '''Save data as CSV.'''

    from csv import writer

    with open(filePath, 'w', newline = '') as f:
        c = writer(f, delimiter = ',')
        c.writerows(data)
        
def readData(filePath):
    '''Read data from CSV to a list.'''

    from csv import reader

    result = []

    with open(filePath)  as f:
        c = reader(f, delimiter = ',')

        for r in c:
            result.append(r)

    return result
