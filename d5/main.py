class almanac:
    def __init__(self, file: str, ranged_seeds: bool = False) -> None:
        self.seed = []
        self.location = []
        self.checked = []
        for line in open(file, "r"):
            if line.startswith("seeds:"):
                if ranged_seeds:
                    text = [int(num) for num in line.strip("seeds: ").split()]
                    if len(text) % 2 > 0:
                        raise Warning("seeds not in pairs")
                    for i, num in enumerate(text):
                        if i % 2 > 0:
                            continue
                        else:
                            self.seed.append((num, text[i+1]))
                    self.location = self.seed[:]
                else:
                    self.seed = [int(num) for num in line.strip("seeds: ").split()]
                    self.location = self.seed[:]
            elif "map:" in line or line == "\n":
                self.checked = []
                continue
            else:
                 self.updatelocation(line, ranged_seeds)
    
    def updatelocation(self, text: str, ranged_seeds: bool) -> None:
       # print(text.strip("\n"), self.location)
        new_loc, start, range = [int(num) for num in text.strip("\n").split()]
        if ranged_seeds:
            for i, loc in enumerate(self.location):
                if i in self.checked:
                    continue
                else:
                    overlap_start = max(loc[0], start)
                    overlap_end = min(loc[0]+loc[1]-1, start+range-1)
                    if overlap_start<=overlap_end:
                        self.checked.append(i)
                        if overlap_start != loc[0]:
                            self.location.append((loc[0], start - loc[0]))
                        if overlap_end != (loc[0]+loc[1]-1):
                            self.location.append((start+range, loc[0]+loc[1]-(start+range)))
                        self.location[i] = (new_loc+(overlap_start-start), overlap_end-overlap_start+1)
                        
        else:
            for i, loc in enumerate(self.location):
                if i in self.checked:
                    continue
                if loc >= start and loc<(start+range):
                    #if i == 1 : print(loc, start, start+range)
                    self.location[i] = new_loc + (loc - start)
                    self.checked.append(i)

    def get_loc(self):
        print(self.location)
        return min(self.location)

test = almanac("test.txt", ranged_seeds=True)
print(test.get_loc())
input = almanac("input.txt", ranged_seeds=True)
print(input.get_loc())