
import os
import re


class FileWalker():
        """ holds the files for a given folder """
        def __init__(self, name="Example Folder", pathToFolder="./"):
                try:
                        os.stat(pathToFolder)
                except OSError:
                        print "Folder doesn't exist"
                        raise

                self.regexp = re.compile(r'.*\.(git|svn).*', re.IGNORECASE)
                self.path = pathToFolder
                self.name = name
                self.files = [] # list of files
                self.__fetchAllFiles()

        def getFiles(self):
                return self.files

        def __fetchAllFiles(self):
                for dirpath, dnames, fnames in os.walk(self.path):
                        for f in fnames:
                                pathToFile = os.path.join(dirpath, f)
                                
                                if not self.regexp.match(pathToFile):
                                        self.files.append(pathToFile)

        def __str__(self):
                returnStr =  "Folder: %s\n" % (self.name)
                returnStr += " Files: %d\n"  % len(self.files)
                returnStr += " Path : %s \n" % self.path
                return returnStr
