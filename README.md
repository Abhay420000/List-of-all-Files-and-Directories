# List-of-all-Files-and-Directories
This helps us to find all the names of folders or files (With Path) inside a path.
This is done by using stack and recursion.

It also gives a dictionary with Key = Folder_Name, Values =[file1,file2,file3,...] it is optional you can use it if you want.

You can even modify it if you want a file of a particular type using if condition.


How to run?(In CLI)

Syntax:
python <path_> <store/print> <with full path/not with full path>

path = ./ for current or ../ for previous directory or full path(eg.D:/Python/Projects/)
Note:While in Full Path you must add '/' at last otherwise it will not work eg.D:/Python/Projects/

store/print = Give 's' for store or 'p' for print
You can store or print output as you wish if you want to store it will make a output file named (output.txt)

with full path/not with full path = Pass 'wp' for full path or 'nwp' for only names

Example:

python main.py C:\Windows\System32\ s wp (In Windows)

python main.py 'C:\Windows\System32\' 'p' 'wp' (In Linux)
