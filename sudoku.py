def main():
	hardestPuzzle = [[8,0,0,0,0,0,0,0,0],
			 [0,0,3,6,0,0,0,0,0],
			 [0,7,0,0,9,0,2,0,0],
			 [0,5,0,0,0,7,0,0,0],
			 [0,0,0,0,4,5,7,0,0],
			 [0,0,0,1,0,0,0,3,0],
			 [0,0,1,0,0,0,0,6,8],
			 [0,0,8,5,0,0,0,1,0],
			 [0,9,0,0,0,0,4,0,0]]

	p = Puzzle()
	p.__importSimpleMap__(hardestPuzzle)
	p.setNote(5,9,1)
	p.setNote(6,9,1)
	p.setCell(6,9)
	print p.getDetailedMapString()


class Puzzle:
	def __init__(self):
		self.p = self.__generateEmptyPuzzle__()

	def getCell(self,x,y):
		return self.p[y][x-1][0]

	def setCell(self,x,y,cellValue=0):
		if cellValue==0:
			solo = self.__getSoloNote__(x-1,y-1)
			if solo>0 and self.p[y-1][x-1][0]==0:
				cellValue = solo
		self.p[y-1][x-1][0]=cellValue

	def unsetCell(self,x,y):
		self.p[y-1][x-1][0]=0

	def getNotes(self,x,y):
		return self.p[y-1][x-1]
		
	def setNote(self,x,y,note):
		if x>0 and y>0:
			self.p[y-1][x-1][note]=note

	def clearNote(self,x,y,note=0):
		if note==0:
			for n in range(1,len(self.p[y-1][x-1])):
				self.p[y-1][x-1][n] = 0
		else:
			self.p[y-1][x-1][note]=0
	def clearNotes(self,x,y):
		self.clearNote(x,y)

	def getSimpleMap(self):
		sMap = [[0 for x in range(len(self.p))] for y in range(len(self.p[0]))]
		for y in range(len(self.p)):
			for x in range(len(self.p[y])):
				sMap[y][x] = self.p[y][x][0]
		return sMap
	def getSimpleMapString(self):
		#NOTE: baked numbers. needs abstraction.
		m = self.getSimpleMap()
		s = ""
		for y in range(len(m)):
			for x in range(len(m[y])):
				s += str(m[y][x]).replace("0","-") + " "
				if (x+1)%3==0 and x<len(m[y])-1: s += "| "
			if (y+1)%3==0 and y<len(m)-1:
				s+= "\n------+-------+------\n"
			elif (y<len(m)-1):
				s += "\n"
		return s
	def getDetailedMapString(self):
		#NOTE: baked numbers. needs abstraction.
		finalString = "\n"
		divR = (" "*18)+" | "+(" "*15)+" | "+(" "*18) + "\n"
		divBR = ("="*57)+"\n"
		def genCellRowString(y):
			div =   "   "
			div_b = " | "
			r1, r2, r3 = div, div, div
			cell_n = 0
			for cell in self.p[y]:
				if (cell[0]!=0):	#if cell set, print set value
					r1 += "   "
					r2 += "-"+str(cell[0])+"-"
					r3 += "   "
				else:			#else print notes grid
					r1 += ''.join(map(str, cell[1:4 ])).replace("0"," ")
					r2 += ''.join(map(str, cell[4:7 ])).replace("0"," ")
					r3 += ''.join(map(str, cell[7:10])).replace("0"," ")
				cell_n += 1
				if cell_n%3==0 and cell_n<len(cell)-1:
					r1 += div_b; r2 += div_b; r3 += div_b
				else:
					r1 += div; r2 += div; r3 += div
					
			return r1 + "\n" + r2 + "\n" + r3 + "\n"
		for y in range(len(self.p)):
			finalString += genCellRowString(y)
			if (y+1)%3==0 and y<len(self.p)-1: finalString += divBR
			elif y<len(self.p)-1: finalString += divR
		return finalString

	def setAllNotes(self):
		for y in range(len(self.p)):
			for x in range(len(self.p[y])):
				for n in range(len(self.p[y][x])):
					self.p[y][x][n] = n

	def getDebugString(self):
		s = "columns: " + str(len(self.p)) + \
			"\nrows: " + str(len(self.p[0])) + \
			"\nslots: " + str(len(self.p[0][0])) + "\n"
		for y in range(len(self.p)):
			for x in range(len(self.p[y])):
				for n in self.p[y][x]:
					s += str(n)
				s += " "
			s += "\n"
		return s

	def __generateEmptyPuzzle__(self,r=9,c=9,s=10):
		puzzle = [[[0 for n in range(s)] for x in range(c)] for y in range(r)]
		return puzzle

	def __importSimpleMap__(self,sM):
		#NOTE: unsafe assumptions. needs safeguards.
		for y in range(len(sM)):
			for x in range(len(sM[y])):
				self.p[y][x][0] = sM[y][x]

	def __getSoloNote__(self,x,y):
		notes = self.p[y][x]
		numNotes = 0
		soloNote = 0
		for n in notes:
			if n > 0: numNotes += 1
		if numNotes==1:
			for n in notes:
				if n > 0: soloNote = n
		return soloNote

	def __str__(self):
		return self.getSimpleMapString()

def getCommand():
	cmd = input("What next? ")
	return str(cmd)
	

if  __name__ == "__main__":
	main()
