import subprocess
import sys

# This python file simply compiles and runs an input file, cutting down on the time it takes to use the commandline.

def compile_java(java_file):
    print("Compiling and running file: "+java_file)
    cmd = "javac " + java_file
    proc = subprocess.Popen(cmd, shell=True)
    proc.wait()

def run_java(java_file):
    cmd = "java " + java_file
    proc = subprocess.Popen(cmd, shell=True)
    proc.wait()

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
