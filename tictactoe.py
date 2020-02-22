import random


class Player:
	def __init__(self, sign):
		self.sign = sign

	def move(self, moves, sign):
		print('Your move, please choose a field.')
		player_move = input()
		while player_move not in moves or moves[player_move] != '_':
			print('Something is wrong, you may want to check your move')
			print('Your move, please choose a field.')
			player_move = input()
		moves.pop(player_move)
		moves[player_move] = str(sign)


class Computer(Player):
	def __init__(self, sign):
		super().__init__(sign)

	def move(self, moves, sign_own, sign_op):
		abc = ''
		for key, value in moves.items():
			efg = value
			if abc == efg and value == '_':
				player_move = key
				moves.pop(player_move)
				moves[player_move] = str(sign_own)
				break
			else:
				choice = random.choice(list(moves.keys()))
				while moves[choice] == 'x' or moves[choice] == 'o':
					choice = random.choice(list(moves.keys()))
				moves.pop(choice)
				moves[choice] = str(sign_own)
				break


class Board:
	def __init__(self):
		self.moves = {
			'top_left': '_',
			'top_mid': '_',
			'top_right': '_',
			'mid_left': '_',
			'mid_mid': '_',
			'mid_right': '_',
			'bot_left': '_',
			'bot_mid': '_',
			'bot_right': '_'}

	def action(self, player_move, sign):
		self.moves.pop(player_move)
		self.moves[player_move] = str(sign)

	def winning_board(self, player, sign):
		return ((self.moves['top_left'] == self.moves['top_mid'] == self.moves['top_right'] == str(sign)) or
				(self.moves['mid_left'] == self.moves['mid_mid'] == self.moves['mid_right'] == str(sign)) or
				(self.moves['bot_left'] == self.moves['bot_mid'] == self.moves['bot_right'] == str(sign)) or
				(self.moves['top_left'] == self.moves['mid_mid'] == self.moves['bot_right'] == str(sign)) or
				(self.moves['bot_left'] == self.moves['mid_mid'] == self.moves['top_right'] == str(sign)) or
				(self.moves['top_left'] == self.moves['mid_left'] == self.moves['bot_left'] == str(sign)) or
				(self.moves['top_mid'] == self.moves['mid_mid'] == self.moves['bot_mid'] == str(sign)) or
				(self.moves['top_right'] == self.moves['mid_right'] == self.moves['bot_right'] == str(sign)))

	def advice(self):
		while True:
			print('Do you want me to remind you the name of each field?')
			answer = input().capitalize()
			if answer == 'Yes':
				print(
					'In order to choose where you want put an X please type in the name of field as per below legend:')
				print('top_left|top_mid|top_right')
				print('mid_left|mid_mid|mid_right')
				print('bot_left|bot_mid|bot_right')
				break
			elif answer == 'No':
				break
			else:
				print('I do not understand, please repeat...')

	def print_board(self):
		print(self.moves['top_left'], '|', self.moves['top_mid'], '|', self.moves['top_right'])
		print(self.moves['mid_left'], '|', self.moves['mid_mid'], '|', self.moves['mid_right'])
		print(self.moves['bot_left'], '|', self.moves['bot_mid'], '|', self.moves['bot_right'])

	def starting_board(self):
		print('In order to choose where you want put your marker please type in the name of field as per below legend:')
		print('top_left|top_mid|top_right')
		print('mid_left|mid_mid|mid_right')
		print('bot_left|bot_mid|bot_right')


class Game():
	def __init__(self):
		pass

	def round_log(self, x, moves):
		print(f'Round {x}!')
		f = open(f"board_round_{x}.txt", "w")
		f.write(str(moves))
		f.close()

	def choose_gametype(self):
		global playerA, playerB
		if random.randrange(0, 2) == 0:
			playerA_sign = 'x'
			playerB_sign = 'o'
		else:
			playerA_sign = 'o'
			playerB_sign = 'x'
		while True:
			print('Do you want to play?')
			answer = input().capitalize()
			if answer == 'Yes':
				print('With a friend?')
				answer2 = answer = input().capitalize()
				if answer2 == 'Yes':
					playerA = Player(playerA_sign)
					playerB = Player(playerB_sign)
					break
				elif answer == 'No':
					playerA = Player(playerA_sign)
					playerB = Computer(playerB_sign)
					break
				else:
					print('I do not understand, please repeat...')
			elif answer == 'No':
				playerA = Computer(playerA_sign)
				playerB = Computer(playerB_sign)
				break
			else:
				print('I do not understand, please repeat...')

	def run(self):
		self.choose_gametype()
		b = Board()
		b.starting_board()
		x = 0
		while x < 10:
			if b.winning_board(playerB, playerB.sign):
				print('Player B wins!')
				break
			elif '_' not in b.moves.values():
				print('TIE!')
				break
			if isinstance(playerA, Computer) and isinstance(playerB, Computer):
				self.round_log(x, b.moves)
				b.print_board()
				playerA.move(b.moves, playerA.sign, playerB.sign)
				print('Player A move!')
				b.print_board()
				if b.winning_board(playerA, playerA.sign):
					print('Player A wins!')
					break
				elif '_' not in b.moves.values():
					print('TIE!')
					break
				playerB.move(b.moves, playerB.sign, playerA.sign)
				print('Player B move!')
			elif isinstance(playerA, Player) and isinstance(playerB, Computer):
				self.round_log(x, b.moves)
				b.print_board()
				b.advice()
				playerA.move(b.moves, playerA.sign)
				print('Player A move!')
				b.print_board()
				if b.winning_board(playerA, playerA.sign):
					print('Player A wins!')
					break
				elif '_' not in b.moves.values():
					print('TIE!')
					break
				playerB.move(b.moves, playerB.sign, playerB.sign)
				print('Player B move!')
			else:
				self.round_log(x, b.moves)
				b.print_board()
				b.advice()
				playerA.move(b.moves, playerA.sign)
				print('Player A move!')
				b.print_board()
				if b.winning_board(playerA, playerA.sign):
					print('Player A wins!')
					break
				elif '_' not in b.moves.values():
					print('TIE!')
					break
				b.advice()
				playerB.move(b.moves, playerB.sign)
				print('Player B move!')
			x += 1
			continue


game = Game()

game.run()
