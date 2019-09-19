def copy_file(source_file,destinstion_file):
    #open source file
    source_file = open(source_file)
    #open destination file 
    destinstion_file = open (destinstion_file,'w')
    #read soure file contents
    source_file_read = source_file.read()
    #Write source file in destination file
    destinstion_file.write(source_file_read)
    print("Coping Done Enjoy")
if __name__ == "__main__":
    #name of source file 
    source_file = input("Enter source file location > ")
    #name of destination file 
    destinstion_file = input("Enter destination file location >")
    #call copy function 
    copy_file(source_file,destinstion_file)