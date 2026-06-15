import os
import matplotlib.pyplot as plt

def format_size(size_bytes):
    """Convert bytes to a human-readable format."""
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    size = float(size_bytes)

    for unit in units:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} PB"


def get_folder_size(folder_path):
    """Recursively calculate folder size."""
    total_size = 0

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                total_size += os.path.getsize(file_path)
            except (PermissionError, FileNotFoundError):
                continue

    return total_size


def analyze_folder(folder_path):
    print(f"\nAnalyzing: {folder_path}\n")

    total_folder_size = get_folder_size(folder_path)

    print("-" * 150)
    print(f"\t\t\t\t\t\t\tTotal Folder Size: {format_size(total_folder_size)}")
    print("-" * 150)

    print("\nFILE\FOLDER\t\tFILE NAME\t\t\t\t\t\tSIZE:\n")
    print("-" * 150)

    try:
       for item in os.listdir(folder_path):

        item_path = os.path.join(folder_path, item)

        if os.path.isdir(item_path):
            size = get_folder_size(item_path)
            print(f"<FOLDER>\t{item:<62} {format_size(size)}")

        elif os.path.isfile(item_path):
            size = os.path.getsize(item_path)
            print(f"<FILE>\t\t{item:<62} {format_size(size)}")
   
    except PermissionError:
        print("Permission denied.")


if __name__ == "__main__":
    folder = input("Enter folder path: ").strip()

    if os.path.exists(folder):
        analyze_folder(folder)
    else:
        print("Folder does not exist.")
    print("-" * 150)
    print("\t\t\t\t\t\t\t THANK YOU")
    print("-" * 150)
#------------------------------------------------------------------------------------------------------------------------------------------------------
#******************************************************************************************************************************************************
    #EXPACTED OUTPUT:-

#c:\Users\sahil\python_intership\project_folder\folder_size_analyzer.py:42: SyntaxWarning: "\F" is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\F"? A raw string is also an option.
#print("\nFILE\FOLDER\t\tFILE NAME\t\t\t\t\t\tSIZE:\n")
#Enter folder path: C:\samsung data

#Analyzing: C:\samsung data

#------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                       Total Folder Size: 3.09 GB
#------------------------------------------------------------------------------------------------------------------------------------------------------

#FILE\FOLDER             FILE NAME                                               SIZE:

#------------------------------------------------------------------------------------------------------------------------------------------------------
#<FOLDER>        app                                                            50.39 MB
#<FOLDER>        audio                                                          21.55 MB
#<FILE>          Bella ciao new remix.mp3                                       387.86 KB
#<FILE>          Best ever ringtone.mp3                                         337.66 KB
#<FOLDER>        Camera                                                         1.76 GB
#<FILE>          DSC_7960.JPG                                                   5.86 MB
#<FILE>          DSC_7961.JPG                                                   6.54 MB
#<FILE>          DSC_7962.JPG                                                   6.00 MB
#<FILE>          DSC_7963.JPG                                                   6.54 MB
#<FILE>          DSC_7966.JPG                                                   6.00 MB
#<FILE>          DSC_7967.JPG                                                   5.75 MB
#<FILE>          DSC_7968.JPG                                                   6.64 MB
#<FILE>          DSC_7969.JPG                                                   6.37 MB
#<FILE>          DSC_7970.JPG                                                   6.07 MB
#<FOLDER>        Facebook                                                       1.96 MB
#<FOLDER>        folder                                                         171.54 KB
#<FOLDER>        image                                                          188.26 MB
#<FOLDER>        Instagram                                                      1.84 MB
#<FILE>          iPhone_6_Plus_Original_Ringtone(256k) (1).mp3                  835.54 KB
#<FILE>          Maa_O_Meri_Maa_WhatsApp_status(256k).mp3                       1.95 MB
#<FILE>          Mera_bhai_tu_.mp3                                              941.29 KB
#<FILE>          Meri maa ke barabar ko.mp3                                     469.91 KB
#<FOLDER>        Mrg video                                                      579.62 MB
#<FOLDER>        Snapchat                                                       68.79 MB
#<FILE>          Soft Romantic.mp3                                              447.05 KB
#<FOLDER>        video                                                          395.52 MB
#------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                         THANK YOU
#------------------------------------------------------------------------------------------------------------------------------------------------------