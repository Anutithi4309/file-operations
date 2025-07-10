outputFile=open('updated file.txt','w')
inputFile=open('repeated.txt','r')
lines_seens_so_far=set()
print("eliminating duplicate lines")
for line in inputFile:
    if line not in lines_seens_so_far:
        outputFile.write(line)
        lines_seens_so_far.add(line)
inputFile.close()
outputFile.close()