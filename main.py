import os
import subprocess
import re


def clean_flutter(folder):
    prev_dir = os.getcwd() # my current directory 
    dir=folder # same current directory
    items=os.listdir(dir) # All file and folders inside it
    for item in items: # for each file and folder 
        if os.path.isfile(os.path.join(dir, item)): # is it a file?
            item_path = os.path.join(dir, item) 
            if item_path.__contains__("pubspec.yaml"): # if file is it pubspec.yaml?
                flutter_folder=re.sub("/[a-zA-Z]*pubspec.yaml","",item_path)
                os.chdir(flutter_folder) # go to the dir
                res=subprocess.run(["/home/user/software/flutter/bin/flutter","clean"],)
                print(res) # response of the clean
                os.chdir(prev_dir) # move to the previous dir
        elif os.path.isdir(os.path.join(dir, item)):
            clean_flutter(os.path.join(dir, item))
        else:
            pass


def clean_rust_builds(folder):
    prev_dir = os.getcwd() # my current directory 
    dir=folder # same current directory
    items=os.listdir(dir) # All file and folders inside it
    for item in items: # for each file and folder 
        if os.path.isfile(os.path.join(dir, item)): # is it a file?
            item_path = os.path.join(dir, item) 
            if item_path.__contains__("Cargo.toml"): # if file is it Cargo.toml?
                flutter_folder=re.sub("/[a-zA-Z]*Cargo.toml","",item_path)
                os.chdir(flutter_folder) # go to the dir
                res=subprocess.run(["/home/user/.cargo/bin/cargo","clean"],)
                print(res) # response of the clean
                os.chdir(prev_dir) # move to the previous dir
        elif os.path.isdir(os.path.join(dir, item)):
            clean_rust_builds(os.path.join(dir, item))
        else:
            pass

def clean_node_modules(folder):
    dir=folder # same current directory
    items=os.listdir(dir) # All file and folders inside it
    for item in items: # for each file and folder 
        if os.path.isfile(os.path.join(dir, item)): # is it a file?
            pass
        elif os.path.isdir(os.path.join(dir, item)):
            new_folder=os.path.join(dir, item)
            if new_folder.__contains__("node_modules"):
                node_modules=new_folder
                res=subprocess.run(["rm","-rf",node_modules])
                print(res)
            else:
                clean_node_modules(os.path.join(dir, item))
        else:
            pass

def getFileSizesUnderThisFolder(folder):
    dir=folder
    items=os.listdir(dir)
    for item in items:
        if os.path.isfile(os.path.join(dir, item)):
            item_path = os.path.join(dir, item)
            size = os.path.getsize(item_path)/(1024**2)
            # print(size<40)
            if size>40:
                print(dir,item)
            # print(item, f"is a file : {size} megabytes")
        # Check if the item is a directory
        elif os.path.isdir(os.path.join(dir, item)):
            getFileSizesUnderThisFolder(os.path.join(dir, item))
            # print(item, "is a directory")
        else:
            print(item, "is neither a file nor a directory")

# getFileSizesUnderThisFolder(".")




clean_flutter("/home/user/Desktop/Programming/")
clean_node_modules("/home/user/Desktop/Programming/")
clean_rust_builds("/home/user/Desktop/Programming/")




def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
            print(total_size/(1024**2))
    return total_size

# Example usage
folder_path = "/home/user/Desktop/Programming/"
size_in_mb = get_folder_size(folder_path)/(1024**2)

print("Size of folder '{}': {} MB".format(folder_path, size_in_mb))
