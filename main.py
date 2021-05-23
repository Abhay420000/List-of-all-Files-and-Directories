# -*- coding: utf-8 -*-
"""
Created on Sat May  1 18:26:28 2021

@author: abhay
"""

import os

stack = []
'''
Stack is Used as a directory(folder/path) pointer due to its property of LIFO
It's last element is current directory Current Directory
'''

ipath = ''
'''
This is the path made every time when we move from
directory to directory
Maked by using Stack
'''

unordereddat = {}
'''
Data added when a directory is found
eg.{'MYDIR':[file1,dir2,file2],'dir2':[file5,file6]}
Not a main part for this project.
This is just for fun.
'''

def stackUpdate(dirr,operation):
    '''
    Its going to update here when required
    Its required when we have to go back or forward
    in a directory(path)
    Note:Whenever do stackUpdate always do buildUpdate
    '''
    global stack
    if operation == 'a':
        stack.append(dirr)
    elif operation == 'p' and len(stack) != 0:
        stack.pop()

def buildPath():
    '''
    This is going to build path for us using stack
    Returns
    Note:Whenever do stackUpdate always do buildUpdate
    -------
    None.

    '''
    global stack,ipath
    ipath = ''
    if len(stack) > 0:
        for i in range(0,len(stack)):
            ipath = ipath + stack[i] + '/'
    else:
        ipath = './'


def keepRec():#Not required (Optional)
    '''
    Used to keep record of each and every files in a directory.
    It must be called to do so.
    A dictionary with key = Folder name, values =[file1,file2,file3]
    
    Returns
    -------
    None.

    '''
    global unordereddat,ipath,stack
    files = []
    with os.scandir(ipath) as ent:
        for i in ent:
            files.append(i.name)
    
    try:
        dirc = stack[-1]
    except:
        #for the frist time
        dirc = './'
    unordereddat[dirc] = files

def datas(flag = 2):
    '''
    This function is going to do our actual work of listing
    files and directories order wise.
    
    '''
    
    if flag == 1:
        f = open('Output.txt','w')
    else:
        print('\n')
    
    buildPath()
    #keepRec()
    
    with os.scandir(ipath) as ent:
        for i in ent:
            
            #listing all files
            if os.path.isfile(ipath+i.name):
                
                if flag == 1:
                    f.write(len(stack)*'\t'+'-'+i.name)
                else:
                    print(len(stack)*'\t'+'-'+i.name)
            
            #listing directorie and going inside it
            elif os.path.isdir(ipath+i.name):
                if flag == 1:
                    f.write(len(stack)*'\t'+'-'+i.name)
                else:
                    print(len(stack)*'\t'+i.name)
                stackUpdate(i.name,'a')
                buildPath()
                #keepRec()
                datas()
                stackUpdate(ipath, 'p')
                buildPath()
                


while True:
    
    print('What Do you want?')
    print('\t1.Make a File')
    print('\t2.Print On Screen\n')
    
    try:
        s = int(input("Enter Option:"))
        if s > 2:
            print('Invalid Option!\n')
    except ValueError:
        print("Please Enter Only Numbers\n")
        continue
    
    if s == 1:
        datas(s)
    else:
        datas()
    
    print('\n')
    
    break

#print(unordereddat)#Gives a dictionary with key = Folder name, values =[file1,file2,file3]
#Note: Uncomment keepRec above in code frist