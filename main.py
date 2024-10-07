# Activity-1----------------------------------------------------------------
# with open ("codingal.txt","w") as file:
#     file.write("Hello, world!")
# file.close()

# with open("codingal.txt","r") as file:
#     data=file.readlines()
#     print("Words will be printed:")
#     for line in data:
#         word=line.split()
#         print(word)
# file.close()



# Activity-2----------------------------------------------------------------
# import os
# try:
#     new_file=open("newfile.txt","x")
#     new_file.close()
#     print("newfile.txt created successfully")
# except FileExistsError:
#     print("File already exists")
    
# print("Checking if file is existing or not")
# if os.path.exists("newfile.txt"):
#     os.remove("newfile.txt")
#     print("file removed successfully")
# else:
#     print("file does not exist")
    
# if os.path.exists("xyz"):
#     os.rmdir("xyz")
#     print("Directory removed successfully")
# else:
#     print("Directory does not exist")



 #Activity-3----------------------------------------------------------------
# with open ("codingal.txt") as fp:
#      data1= fp.read()
# with open("xyz.txt") as fp:
#     data2= fp.read()
    
# data1+="\n"
# data1+=data2 
# print("Merging two files")
# with open ("Mergedfile.txt","w") as fp:
#     fp.write(data1)



#Activity-4----------------------------------------------------------------------
outputFile=open("updatedFile.txt","w")
inputFile=open("new.txt","r")
linesSeenSoFar=set()
print("Eliminating dublicate lines")
for line in inputFile:
    if line not in linesSeenSoFar:
        outputFile.write(line)
        linesSeenSoFar.add(line)
inputFile.close()
outputFile.close()