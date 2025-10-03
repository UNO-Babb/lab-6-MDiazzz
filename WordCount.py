#WordCount.py
#Name: Michelle Diaz  
#Date: 10/2/25
#Assignment: WordCount

def main():
  textFile = open("gettysberg.txt", 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0 

  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1
      letterCount += len(w) 
 
 #print(line)
  print("Lines:", lineCount)
  print("Words:", wordCount)
  print("Letter:", letterCount)
  

if __name__ == '__main__':
  main()
