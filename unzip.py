from zipfile import ZipFile
with ZipFile('Assign3.zip', 'r') as zipObj:
    zipObj.extractall()

# with ZipFile('sampleDir.zip', 'r') as zipObj:
#    zipObj.extractall()
