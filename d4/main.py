class lottery:
    def __init__(self, ticket) -> None:
        self.target = []
        self.numbers = []
        for card in ticket:
            target, numbers = card.strip().split(" | ")
            self.target.append(set(target.strip().split()))
            self.numbers.append(list(numbers.strip().split()))
        self.match_list = self.find_match()
    
    def find_match(self) -> list[str]:
        match_list = []
        for i in range(len(self.target)):
            card_target = self.target[i]
            card_numbers = self.numbers[i]
            number_match = []
            for number in card_numbers:
                if number in card_target:
                    number_match.append(number)
            match_list.append(number_match)
        return match_list
    
    def wrong_count_points(self) -> int:
        points = 0
        for match in self.match_list:
            match_count = len(match)
            if match_count == 0:
                continue
            x = (match_count-1)//3
            a = 2**x
            r = 1/2
            n = x+1
            remainder = (match_count-1)%3
            points += 3*(a*(1-r**n)/(1-r)) + 1*a - (3-remainder)
            
        return points
    
    def count_points(self) -> int:
        total_points = 0
        for match in self.match_list:
            match_count = len(match)
            if match_count == 0:
                continue
            total_points += 2**(match_count-1)
        return(total_points)
    
    def count_cards(self) -> int:
        card_multiply = [1] * len(self.numbers)
        for i, match in enumerate(self.match_list):
            match_number = len(match)
            multiplier = card_multiply[i]
            card_multiply[i+1:i+1+match_number] = [m+1*multiplier for m in card_multiply[i+1:i+1+match_number]]
        return sum(card_multiply)

    
f = open("input.txt", "r")
ticket = []
for line in f:
    ticket.append(line.strip().split(": ")[1])

game = lottery(ticket=ticket)
print(game.count_points())
print(game.count_cards())
