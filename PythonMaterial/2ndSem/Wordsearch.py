dictionary = ["BINARY", "COMPUTER SCIENCE", "DECIMAL", "HEXADECIMAL", "JUPYTER", "MATPLOTLIB", "NOTEBOOK", "OCTAL", "PANDAS", "POWERSHELL"]
n = len(dictionary)
M = 15
B = 15

def isWord(Str):
    # Linearly search all words
    for i in range(n):
        if (Str == dictionary[i]):
            return True
    return False
def findWordsUtil(boggle, visited, i, j, Str):
	# Mark current cell as visited and
	# append current character to str
	visited[i][j] = True
	Str = Str + boggle[i][j]
	
	# If str is present in dictionary,
	# then print it
	if (isWord(Str)):
		print(Str)
	
	# Traverse 8 adjacent cells of boggle[i,j]
	row = i - 1
	while row <= i + 1 and row < M:
		col = j - 1
		while col <= j + 1 and col < B:
			if (row >= 0 and col >= 0 and not visited[row][col]):
				findWordsUtil(boggle, visited, row, col, Str)
			col+=1
		row+=1
	
	# Erase current character from string and
	# mark visited of current cell as false
	Str = "" + Str[-1]
	visited[i][j] = False

def findWords(boggle):
   
    # Mark all characters as not visited
    visited = [[False for i in range(B)] for j in range(M)]
     
    # Initialize current string
    Str = ""
     
    # Consider every character and look for all words
    # starting with this character
    for i in range(M):
      for j in range(B):
        findWordsUtil(boggle, visited, i, j, Str)
 
# Driver Code
boggle=[['M','A','T','P','L','O','T','L','I','B','O','G','T','R','C'],
        ['Z','Q','O','E','M','I','X','U','G','R','K','C','T','O','I'],
        ['B','I','N','A','R','Y','H','U','C','O','N','X','M','A','H'],
        ['U','P','S','E','S','O','Z','P','O','P','J','P','Z','F','K'],
        ['R','R','O','L','S','O','P','B','M','A','U','Q','O','X','L'],
        ['S','S','V','W','K','O','E','E','F','T','P','N','L','R','A'],
        ['H','A','L','H','E','T','C','L','E','B','Y','A','S','W','M'],
        ['P','H','D','O','O','R','G','R','Q','E','T','R','F','F','I'],
        ['G','D','F','N','Y','Q','S','B','B','C','E','C','S','A','C'],
        ['U','M','C','O','A','C','D','H','O','S','R','V','M','W','E'],
        ['H','T','A','L','I','P','L','W','E','T','M','L','U','W','D'],
        ['M','O','M','E','G','Q','K','H','M','L','O','U','H','O','A'],
        ['U','G','N','O','L','G','Y','X','U','M','L','M','G','S','X'],
        ['F','C','J','E','J','X','H','A','T','A','B','S','A','C','E'],
        ['E','I','U','H','N','Z','P','L','A','M','I','C','E','D','H']]
 
print("Following words of", "dictionary are present")
findWords(boggle)

