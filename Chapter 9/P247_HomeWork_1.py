#! python3
# FileCopy

import shutil, os

def FileCopy(folder, newfolder):
    folder = os.path.abspath(folder)
    newfolder = os.path.abspath(newfolder)
    count = 0
    for foldername, subfolders, filenames in os.walk(folder):
        print('\nSearching files in %s' % (foldername))
        for filename in filenames:
            if filename.endswith('.pdf') or filename.endswith('.PDF') or filename.endswith('.jpg') or filename.endswith('.JPG'):
                print('Searching Success %s' % (filename))
                count += 1
                basepath  = foldername + '\\' + filename
                shutil.copy(basepath, newfolder)
            elif count == 0:
                print('Searching not')
    print('Copy File Count : %s' %(count))


FileCopy('C:\\Users\\Parkchihoon\\Desktop\\starlex', 'C:\\Users\\Parkchihoon\\Desktop\\test')