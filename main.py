import os

# DETECTING BINOD IN EVERY FILE THAT COMES IN THIS FUNCTION:
def isBinod(filename):
    """ Detecting of Checking BINOD is Every File in this Directory! """
    with open(filename, 'r') as fp:
        file_data = fp.read()
    # CHecking every case for binod string
    if 'binod' in file_data.lower():
        return True
    else:
        return False

if __name__ == '__main__':
    print(('\n'*2) + ('\t'*3) + 'BINOD DETECTOR' + ('\n'*2))
    directory = os.listdir()
    binodNum = 0

    for file in directory:
        if file.endswith('txt') or file.endswith('csv'):
            print(f'Detecting BINOD in {file}')
            boolVal = isBinod(file)
            if boolVal:
                print(f'Binod Found in {file}\n')
                binodNum += 1
            else:
                print(f'Binod Not Found in {file}\n')

    print(f'BINOD DETECTOR USING PYTHON 3.6.5')
    print(f'Binod Found in this {binodNum} files!!!')