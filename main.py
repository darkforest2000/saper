import random
import os

class Cell:

	def __init__(self, around_mines, mine):
		self.around_mines = around_mines
		self.mine = mine
		self.fl_open = False

class GamePole:
	pole  = []

	def __init__(self, M, N):
		self.M = M
		self.N = N
		self.all_cells = [i for i in range(1, self.N**2+1)]
		self.m_indxes = random.sample(self.all_cells, self.M)
		#self.around_mines = 0

		self.matrix = [[j for j in range(i, i+self.N)] for i in range(1, self.N**2+1, self.N)]
		#print(self.matrix)
		self.compleate_dict = dict([(k,v) for k, v in enumerate([0 for i in range(self.N**2)], 1)])
		#for i in self.matrix:
		#print(sorted(self.m_indxes))
		for i in range(self.N):
			for j in range(self.N):
				try:
					if i == 0 or j == 0:
						self.save_value = 0
					self.all_must_be_true = [j>-1, i>-1, j-1>=-1, i-1>=-1]
					#or self.matrix[i][j] - self.N in self.m_indxes
					#print(self.all_must_be_true)
					#if bomba: continue
					#print(f"n:{self.matrix[i][j]} b:{self.m_indxes}")
					if self.matrix[i][j] in self.m_indxes:
						#self.compleate_dict[self.matrix[i][j]] = 'b'
						continue
				except Exception as e:
					pass
				try:
					if self.matrix[i][j-1 if j > 0 else 'q'] in self.m_indxes and all(self.all_must_be_true): #and self.matrix[i][j-1]:
						self.compleate_dict[self.matrix[i][j]] += 1
				except Exception as e:
					pass
				try:
					if self.matrix[i][j+1] in self.m_indxes and all(self.all_must_be_true):
						self.compleate_dict[self.matrix[i][j]] += 1
				except Exception as e:
					pass
				try:
					if self.matrix[i-1 if i > 0 else 'q'][j] in self.m_indxes and all(self.all_must_be_true):
						self.compleate_dict[self.matrix[i][j]] += 1
				except Exception as e:
					pass
				try:
					if self.matrix[i+1][j] in self.m_indxes and all(self.all_must_be_true):
						self.compleate_dict[self.matrix[i][j]] += 1
				except Exception as e:
					pass
				try:
					if self.matrix[i+1][j+1] in self.m_indxes and all(self.all_must_be_true):
						self.compleate_dict[self.matrix[i][j]] += 1
				except Exception as e:
					pass
				try:
					if self.matrix[i+1][j-1 if j > 0 else 'q'] in self.m_indxes and all(self.all_must_be_true):
						self.compleate_dict[self.matrix[i][j]] += 1
				except Exception as e:
					pass
				try:
					if self.matrix[i-1 if i > 0 else 'q'][j+1] in self.m_indxes and all(self.all_must_be_true):
						self.compleate_dict[self.matrix[i][j]] += 1
				except Exception as e:
					pass
				try:
					if self.matrix[i-1 if i > 0 else 0][j-1] in self.m_indxes and all(self.all_must_be_true):
						self.compleate_dict[self.matrix[i][j]] += 1
				except Exception as e:
					pass

		for i in range(1, N*N+1):
			self.pole.append(Cell(self.compleate_dict[i], [i in self.m_indxes][0]))

	def show(self):
		for i in range(1, self.N**2+1, self.N):
			for j in range(i, i+self.N):
				#print('b' if self.pole[j-1].mine is True else self.pole[j-1].around_mines if self.pole[j-1].around_mines > 0 else '#', end=' ')
				print('#' if self.pole[j-1].fl_open is False else self.pole[j-1].around_mines if self.pole[j-1].around_mines > 0 else 'b' if self.pole[j-1].mine is True else ' ', end=' ')
			print()
		


N = int(input(f"Введите размер поля: "))
M = int(input(f"Введите количество мин: "))
GM = GamePole(M, N)
#print(GM.pole[0].mine)
#print(sorted(GM.m_indxes))
GM.show()
user_input = -1
while user_input not in GM.m_indxes:
	user_input = int(input(f"Введите номер клетки до {GM.N**2}: "))
	GM.pole[user_input-1].fl_open = True
	os.system('cls')
	#print(sorted(GM.m_indxes))
	GM.show()
