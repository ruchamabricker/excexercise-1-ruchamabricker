import os

def thats_the_way(path):
    if not os.path.exists(path) or not os.path.isdir(path):
        print("Error: The specified path does not exist or is not a directory.")
        return []

    return [file for file in os.listdir(path) if file.startswith("S")]

if __name__ == "__main__":
    path = input("Enter directory: ")
    matching_files = thats_the_way(path)
    print("Matching files:", matching_files)