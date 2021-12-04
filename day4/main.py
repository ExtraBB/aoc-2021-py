lines = open("day4/input").read().strip().split("\n\n")

# Parse input numbers
nums = lines[0].split(",")

# Parse bingo cards
class Card:
    def __init__(self, rows, cols):
        self.rows, self.cols = rows, cols

def parseCard(card):
    rows = [row.split() for row in card.split("\n")]
    cols = [[row[i] for row in rows] for i in range(len(rows[0]))]
    return Card(rows, cols)

cards = [parseCard(card) for card in lines[1:]]

# mark and try to finish line
def tryFinishLine(line, num):
    finished = False
    if num in line:
        line.remove(num)
        finished = len(line) == 0
    return finished

# mark a number on a card
def tryFinishCard(card, num):
    finished = False
    for row in card.rows:
        finished |= tryFinishLine(row, num)
    for col in card.cols:
        finished |= tryFinishLine(col, num)
    return finished

# calculate result for a winning card
def calculateResult(card, num):
    return sum([sum(map(int, row)) for row in card.rows]) * int(num)

def part1(nums, cards):
    for num in nums:
        for card in cards:
            if tryFinishCard(card, num):
                return calculateResult(card, num)

def part2(nums, cards):
    for num in nums:
        for card in [*cards]:
            if tryFinishCard(card, num):
                cards.remove(card)
                if len(cards) == 0:
                    return calculateResult(card, num)

print(part1(nums, cards))
print(part2(nums, cards))