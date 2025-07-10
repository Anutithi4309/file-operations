new_file=open('New_file.txt','x')
new_file.close()
import os
print("if my file exist or not..........")
if os.path.exists('my_file.txt'):
    os.remove('my_file.txt')
else:
    print("file does not exist")
my_file=open('my_file.txt','w')
my_file.write("I am Anutithi paul..")
my_file.close()
os.remove('Codingal.txt')
os.rmdir('Folder')