# Python based File Scanner
The main goal is to develop a file parser that will be configurable when it comes to 
different filetypes. Once could add a new file class and configure a number of regular expressions.

## FileClass
* simply stores the files which belong to a certain file class
* internal data:
 * name (string)
 * files (list)
 * statistics (FileStatistics)