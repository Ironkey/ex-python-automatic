#! python3
# Filedelet

import send2trash, os

def BigFileDelet(folder):
    Biglist = []
    folder = os.path.abspath(folder)

    for foldername, subfoldernames, filenames in os.walk(folder):
        print('Searching in %s' % (foldername))

        if int(os.path.getsize(foldername)) >= 1000000000:
            print('%s size %s. Big Folder' % (foldername, os.path.getsize(foldername)))
            Biglist.append(foldername)

        for filename in filenames:
            filepath = foldername + '\\' + filename
            if int(os.path.getsize(filepath)) >= 1000000000:
                print('%s size %s. Big File.' % (filename, os.path.getsize(filepath)))
                Biglist.append(filepath)

    print('Biger List : ' + str(Biglist))
    for delist in Biglist:
        send2trash.send2trash(delist)
    print('File All Del')


BigFileDelet(r'C:\Users\Parkchihoon\Desktop\test')