import os

def thats_the_way(path):
    if not os.path.exists(path) or not os.path.isdir(path):
        print("Error: The specified path does not exist or is not a directory.")
        return []

    return [file for file in os.listdir(path) if file.startswith("S")]

path = input("enter directory")
matching_files = thats_the_way(path)

print("Matching files:", matching_files)
