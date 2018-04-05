#!/usr/bin/python

# This Tool For Brute Force Attack On Locked Zip Files
# By : Oseid Aldary
## I LOVE PYTHON(^-^)

## LIT'S STARTED !!

#First Import libraries ##

from sys import argv
from time import sleep as se
import datetime
import zipfile


## Show Time ##

now = datetime.datetime.now()
hour = now.hour
min = now.minute
sec = now.second
timenow = "{}:{}:{}".format(hour,min,sec)

####

# Usage msg

if len(argv) !=3:

	print("""

JoKeR11=> We Are Arab :)

 ******** **   **            **     **   ** 
//////** /**  **            ****   /**  ** 
     **  /** **   ******   **//**  /** **  
    **   /****   //**//*  **  //** /****   
   **    /**/**   /** /  **********/**/**  
  **     /**//**  /**   /**//////**/**//** 
 ********/** //**/***   /**     /**/** //** 
//////// //   // ///    //      // //   // 

[#] Usage: python ZKrAK.py <Zip File Locked> <WordList>""")
	exit(1)


filename = argv[1]
if filename[-4:] !=".zip":
	print("\n[!] Error This File[{}] Is Not A ZIP File !!".format(filename))
	exit(1)
passw = argv[2]
try:
   fileopen = open(passw, "r")
except:
	print("\n[!] Error The WordList File Not Found !!\n[*] Check Your File Location")
	exit(1)


zfile = zipfile.ZipFile(filename)
passwlist = open(passw,"r").readlines()

loop = 1
print("""
===============> ZipCracker <=================

[$] Start At    :> {}
[>] ZipFile     :> {}
[>] Wordlist    :> {}

[^] Checking.......

""".format(timenow,filename,passw))
se(1)
for password in passwlist:
	password = password.strip()
	try:
	   zfile.extractall(pwd=password)
	   print("[+] Trying Password[{}] : {} ==> Yes".format(loop,password))
	   print("\n[#] Password Found: {}".format(password))
	   print("[$] ShutDown At: {}".format(timenow))
	   break
	except:
	   print("[-] Trying Password[{}] : {} ==> No".format(loop,password))
	   loop +=1
	   se(0.10)

else:
	print("\n[@] Sorry I Can't Found Password In This Wordlist! :(\n[*] Try Other Wordlist :)")
	exit(1)


##############################################################
##################### 		     #########################
#####################   END OF TOOL  #########################
#####################                #########################
##############################################################
#This Tool by Oseid Aldary
#Have a nice day :)
#GoodBye
