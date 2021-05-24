# -*- coding: utf-8 -*-
"""
Created on Sat May  1 18:26:28 2021

@author: abhay

version: 0.0.1

"""

import os,argparse

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

Note:Uncomment KeepRec if you want to use.
'''

def stackUpdate(dirr,operation):
    '''
    Its going to update here when required
    Its required when we have to go back or forward
    in a directory(path).
    
    Note:Whenever do stackUpdate always do buildUpdate
    '''
    global stack
    if operation == 'a':
        stack.append(dirr)
    elif operation == 'p' and len(stack) != 0:
        stack.pop()

def buildPath():
    '''
    This is going to build path for us using stack.
    
    Note:Whenever do stackUpdate always do buildUpdate
    
    '''
    global stack,ipath,path
    ipath = path
    if len(stack) > 0:
        for i in range(0,len(stack)):
            ipath = ipath + stack[i] + '/'
    else:
        ipath = path


def keepRec():#Not required (Optional)
    '''
    Used to keep record of each and every files in a directory.
    It must be called to do so.
    A dictionary with key = Folder name, values =[file1,file2,file3]
    
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
        dirc = path
    unordereddat[dirc] = files

def datas():
    '''
    This function is going to do our actual work of listing
    files and directories order wise.
    
    '''
    
    global ps,wp,f
    
    buildPath()
    #keepRec()
    
    with os.scandir(ipath) as ent:
        for i in ent:
            
            #listing all files
            if os.path.isfile(ipath+i.name):
                if ps == "p" and wp == "wp":
                    print(ipath+i.name+'\n')
                elif ps == "p" and wp == "nwp":
                    print(len(stack)*'\t'+'-'+i.name)
                elif ps == "s" and wp == "wp":
                    f.write(ipath+i.name+'\n')
                elif ps == "s" and wp == "nwp":
                    f.write(len(stack)*'\t'+'-'+i.name)
            
            #listing directorie and going inside it
            elif os.path.isdir(ipath+i.name):
                if ps == "p" and wp == "wp":
                    print(ipath+i.name+'\n')
                elif ps == "p" and wp == "nwp":
                    print(len(stack)*'\t'+'-'+i.name)
                elif ps == "s" and wp == "wp":
                    f.write(ipath+i.name+'\n')
                elif ps == "s" and wp == "nwp":
                    f.write(len(stack)*'\t'+'-'+i.name)
                
                stackUpdate(i.name,'a')
                buildPath()
                #keepRec()
                datas()
                stackUpdate(ipath, 'p')
                buildPath()
                
parser = argparse.ArgumentParser()
parser.add_argument("Path", help = "Enter Main Path (path of directory inside which you want list)")
parser.add_argument("Print_Store", help = "Print or Store Output", choices = ["p","s"])
parser.add_argument("With_Without_Path", help = "What you want output with full path  or without path(Only Name) ?", choices = ["wp","nwp"])

args = parser.parse_args()

path = args.Path
ps = args.Print_Store
wp = args.With_Without_Path

if ps == "s":
    f = open('Output.txt','w')
else:
    print('\n')

datas()

f.close()

#print(unordereddat)#Gives a dictionary with key = Folder name, values =[file1,file2,file3]
#Note: Uncomment keepRec above in code frist