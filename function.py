def countWordsFromFile():
      fileName = input("Enter the file name: ")
      count = 0
      file = open(fileName, "r")

      for line in file:
        words = line.split()
        count = count+len(words)
      print("No. of words: ")
      print(count)

countWordsFromFile()      
            
        
        
       