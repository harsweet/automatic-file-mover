import os.path


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


    print("Enter the source folder paths. Enter \"done\" to move onto the next prompt.")
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



def main():
    welcomeMessage()
    getInfo()



if __name__ == "__main__":
    main()