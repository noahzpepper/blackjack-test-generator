"""
Blackjack Test Generator

Generates blackjack basic strategy tests.

Creates two files in the working directory, the test file and answers file.
Each file contains a list of blackjack strategy questions and corresponding legend.
The answers file fills in the blanks with the correct basic strategy answers.

Args:
	--size: number of questions to generate (default 48)
	--versions: comma separated list of versions (default A)

Examples:
	
	(default usage)
	$ python3 blackjack_test_generator.py
	  Wrote test to test_A.txt
	  Wrote answer key to test_A_answers.txt

	(write multiple tests)
	$ python3 blackjack_test_generator.py --version=A,B
	  Wrote test to test_A.txt
	  Wrote answer key to test_A_answers.txt
  	  Wrote test to test_B.txt
	  Wrote answer key to test_B_answers.txt
"""
import random
import argparse

HEADER_TEXT_FORMAT = "Blackjack Basic Strategy Test\t\t\t\tName: {:_^25}\nVersion {}\n\n"
INSTRUCTIONS_TEXT = "Fill in the blanks with the corresponding basic strategy play.\n\n"
LEGEND_TEXT = 	"Legend:\nHit: H\t\tStand: S\t\tSplit: P\nDouble if allowed, otherwise hit: Dh\n" + \
				"Double if allowed, otherwise stand: Ds\nSurrender if allowed, otherwise hit: Rh\n" + \
				"Surrender if allowed, otherwise stand: Rs\nSurrender if allowed, otherwise split: Rp"

basic_strategy = {
	# Hard hands
	"8": ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],
	"9": ["H", "Dh", "Dh", "Dh", "Dh", "H", "H", "H", "H", "H"],
	"10": ["Dh", "Dh", "Dh", "Dh", "Dh", "Dh", "Dh", "Dh", "H", "H"],
	"11": ["Dh", "Dh", "Dh", "Dh", "Dh", "Dh", "Dh", "Dh", "Dh", "Dh"],
	"12": ["H", "H", "S", "S", "S", "H", "H", "H", "H", "H"],
	"13": ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
	"14": ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
	"15": ["S", "S", "S", "S", "S", "H", "H", "H", "Rh", "Rh"],
	"16": ["S", "S", "S", "S", "S", "H", "H", "Rh", "Rh", "Rh"],
	"17": ["S", "S", "S", "S", "S", "S", "S", "S", "S", "Rs"],
	"18": ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
	# Soft hands
	"A,2": ["H", "H", "H", "Dh", "Dh", "H", "H", "H", "H", "H"],
	"A,3": ["H", "H", "H", "Dh", "Dh", "H", "H", "H", "H", "H"],
	"A,4": ["H", "H", "Dh", "Dh", "Dh", "H", "H", "H", "H", "H"],
	"A,5": ["H", "H", "Dh", "Dh", "Dh", "H", "H", "H", "H", "H"],
	"A,6": ["H", "Dh", "Dh", "Dh", "Dh", "H", "H", "H", "H", "H"],
	"A,7": ["Ds", "Ds", "Ds", "Ds", "Ds", "S", "S", "H", "H", "H"],
	"A,8": ["S", "S", "S", "S", "Ds", "S", "S", "S", "S", "S"],
	"A,9": ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
	# Split hands
	"2,2": ["P", "P", "P", "P", "P", "P", "H", "H", "H", "H"],
	"3,3": ["P", "P", "P", "P", "P", "P", "H", "H", "H", "H"],
	"4,4": ["H", "H", "H", "P", "P", "H", "H", "H", "H", "H"],
	"5,5": ["Dh", "Dh", "Dh", "Dh", "Dh", "Dh", "Dh", "Dh", "H", "H"],
	"6,6": ["P", "P", "P", "P", "P", "H", "H", "H", "H", "H"],
	"7,7": ["P", "P", "P", "P", "P", "P", "H", "H", "H", "H"],
	"8,8": ["P", "P", "P", "P", "P", "P", "P", "P", "P", "Rp"],
	"9,9": ["P", "P", "P", "P", "P", "S", "P", "P", "S", "S"],
	"10,10": ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
	"A,A": ["P", "P", "P", "P", "P", "P", "P", "P", "P", "P"],
}
"""
A dictionary for the basic strategy chart.
The keys are the player hands.
The values are the optimal play against dealer [2, 3, 4, 5, 6, 7, 8, 9, 10, A].

Rules: 4-8 decks H17 DAS
Source: https://wizardofodds.com/games/blackjack/strategy/4-decks/
"""

def generate_questions(num):
	"""
	Generate questions from the basic strategy chart.

	Args:
		num: the int number of questions to generate

	Returns:
		A list of tuples, where each tuple represents a blackjack question.
		The tuples are unique and in random order.
		Example:
			[("12 vs 2": "H"), ("2,2 vs 6": "P"), ("A,7 vs 8": "S")]

	"""
	db = []
	for hand, strategies in basic_strategy.items():
		for i, answer in enumerate(strategies):
			upcard = "A" if i+2 == 11 else i+2
			prompt = "{0} vs {1}".format(hand, upcard)
			db.append((prompt, answer))
	return random.sample(db, num)

def write_test(filename, version, questions, write_answers):
	"""
	Writes the given questions to a file.

	Args:
		filename: a str name for the file to write
		version: a str version name to be used in the test header 
		questions: a list of tuples, where each tuple represents a blackjack question.
			Example:
				[("12 vs 2": "H"), ("2,2 vs 6": "P"), ("A,7 vs 8": "S")]
		write_answers: a bool of whether to write answers
	"""
	with open(filename, "w+") as out:
		out.write(HEADER_TEXT_FORMAT.format("Answers" if write_answers else "", version))
		out.write(INSTRUCTIONS_TEXT)
		for i, question in enumerate(questions):
			prompt = "{0}:".format(question[0])
			answer = question[1] if write_answers else ""
			spacing = "\n\n" if i % 3 == 2 or i == len(questions)-1 else "\t\t"
			out.write("{0:13}{1:_^7}{2}".format(prompt, answer, spacing))
		out.write(LEGEND_TEXT)
	print("Wrote {0} to {1}".format("answer key" if write_answers else "test", filename))

def main():
	"""Run the program."""
	parser = argparse.ArgumentParser()
	parser.add_argument("--size", help="number of questions to generate (default 48)", type=int, default=48)
	parser.add_argument("--versions", help="comma separated list of version names (default A)", type=str, default="A")
	args = parser.parse_args()

	for version in args.versions.split(","):
		questions = generate_questions(args.size)
		write_test("test_{}.txt".format(version), version, questions, False)
		write_test("test_{}_answers.txt".format(version), version, questions, True)

if __name__ == "__main__":
	main()
