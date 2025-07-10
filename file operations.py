with open('Codingal.txt','w')as file:
    file.write("HI!I am Anutithi Paul.I am a good girl.")
    file.close()
with open('Codingal.txt','r')as file:
    data=file.readlines()
    print("words in this file are..........")
    for line in data:
        word=line.split()
        print(word)
    file.close()
