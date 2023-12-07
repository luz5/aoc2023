class cube:
    def __init__(self, red: int, blue: int, green: int) -> None:
        self.red = red
        self.blue = blue
        self.green = green

    def check_max(self, game: str) -> dict:
        rounds = game.strip().split("; ")
        max_cube = {"green": 0,
                    "blue": 0,
                    "red": 0
                    }
        for round in rounds:
            cubes = round.strip().split(", ")
            for cube in cubes:
                number, color = cube.split()
                if int(number) > max_cube[color]:
                    max_cube[color] = int(number)
        return max_cube
    
    def if_doable(self, max_cube: dict) -> bool:
        result = True
        for cube in max_cube:
            actual_cube = getattr(self, cube, None)
            if actual_cube and actual_cube < max_cube[cube]:
                result = False
        return result
    
    def get_power(self, all_game: str) -> int:
        sum = 0
        f = open(all_game, "r")
        for line in f:
            power = 1
            gamenum, gameinfo = line.split(": ")
            gameint = int(gamenum.split()[1])
            for numberofcubes in self.check_max(gameinfo).values():
                power *= numberofcubes
            sum += power
        return sum
    
    def sum_of_game(self, all_game: str) -> int:
        sum = 0
        f = open(all_game, "r")
        for line in f:
            gamenum, gameinfo = line.split(": ")
            gameint = int(gamenum.split()[1])
            if self.if_doable(self.check_max(gameinfo)):
                sum += gameint
        return sum

game = cube(red=12, green=13, blue=14)
print(game.sum_of_game("input.txt"))
print(game.get_power("input.txt"))