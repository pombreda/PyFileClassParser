# Python based File Scanner
The main goal is to develop a file parser that will be configurable when it comes to 
different filetypes. Once could add a new file class and configure a number of regular expressions.
The main idea was to create a configurable file parser that could scan source folders and provides a versatile statistics for a certain amount of file classes. The usual question was:
 * How much source code does this project contain?
 * How much scripting code does the project contain?

## How to use it
 * In order to scan several folders for files 

 ```Python
 from FileWalker import FileWalker
 ``

# Classes

## FileClass
* simply stores the files which belong to a certain file class
* internal data:
 * name (string)
 * files (list)
 * statistics (FileStatistics)

## FileWalker
 * Holds all the files for a folder
 * Always initiated using a existing folder (relative or absolute)

## Session
 * Stores the results for a folder that in turn could contain several file classes

## FileStatistics
 * Object stores the following informatione
   * maxSize - biggest file attached
   * avgSize - average size of all attached files
   * minSize - smallest file
   * sumSize - total amount of bytes stored in files
   * numFiles - number of files found in that folder