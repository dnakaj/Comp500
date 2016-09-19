import subprocess
import sys
import os

# This python file simply compiles and runs an input file, cutting down on the time it takes to use the commandline.

def compile_java(java_file):
    print("Compiling and running file: "+java_file)
    cmd = "javac " + java_file
    proc = subprocess.Popen("exec "+cmd, shell=True)
    # output = proc.communicate()[0]
    # if(proc.returncode != 0):
        # print("There was an error while compiling the file!")
        # sys.exit()
    proc.wait()
def run_java(java_file):
    cmd = "java " + java_file
    proc = subprocess.Popen(cmd, shell=True)
    proc.wait()

directory = input("Set your directory (leave blank to use the current one): ")

if(directory == ""):
    print("Using directory '"+os.getcwd()+"'")
    directory = os.getcwd()
else:
    print("Using directory '"+os.getcwd()+"/"+directory+"'")
    os.chdir(os.getcwd()+"/"+directory)

while(1 == 1):
    java_file = input("Filename: ")

    compile_java(java_file+".java")
    run_java(java_file)

    validAnswer = False

    while not(validAnswer):
        continueProgram = input("Quit program? (Y/N) ")
        # If the user enters "y", quit the program
        if(continueProgram.lower() == "y"):
            sys.exit()
        # Else if the user enters "n", continue
        elif(continueProgram.lower() == "n"):
            validAnswer = True
        # Else, repeat prompt
        else:
            print("Invalid answer!")
