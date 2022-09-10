import os.path
import shutil
import time


def welcomeMessage():
    print("\t........Welcome to the Automatic File Mover........")
    print("\n\nJust Enter the source location(s), destination location(s) and the file types (.mp3, .mp4, etc)")
    print("And the File Mover will take care of the moving :)\n\n\n")



def getInfo():
    info = {
        "sources": [],
        "destinations": [],
        "file_types": []
    }

    print("Enter the source folder paths. Enter \"done\" to move onto the next prompt.")
    while True:
        print()
        given_path = input("Source Folder Path: ")
        if given_path.lower() == "done":
            break
            
        elif (os.path.isdir(given_path)):
            info["sources"].append(given_path)
        
        else:
            print("Oops!! That doesn't look like a valid folder path. Please try again")


    print("\n\nEnter the destination folder paths. Enter \"done\" to move onto the next prompt.")
    while True:
        print()
        given_path = input("Destination Folder Path: ")
        if given_path.lower() == "done":
            break
            
        elif (os.path.isdir(given_path)):
            info["destinations"].append(given_path)
        
        else:
            print("Oops!! That doesn't look like a valid folder path. Please try again")

    print("Enter the file types (with or without '.'). Enter \"done\" to get the moving started!")
    while True:
        print()
        given_type = input("File Type: ")
        if given_type.lower() == "done":
            break
        else:
            info["file_types"].append(given_type)

        return info



def moveFiles(info):

    print("\n\n\nThe file mover is now active and should move your file(s) within 10 seconds")
    print("Press ^C (option + C) to force exit and stop moving!!")

    # For each source folder
    while True:
        for source_folder in info["sources"]:
            # for each file in the source folder
            for file_name in os.listdir(source_folder):
                # for each of the file types
                for file_type in info["file_types"]:
                # if the file is of any of those file types
                    if file_name.endswith(file_type):
                    # then move it to each of the destination folders
                        for destination_folder in info["destinations"]:
                            shutil.copyfile(source_folder+'/'+file_name, destination_folder+'/'+file_name)
                        os.remove(source_folder+'/'+file_name)
        time.sleep(10)
    


def main():
    welcomeMessage()
    desired_info = getInfo()
    moveFiles(desired_info)



if __name__ == "__main__":
    main()