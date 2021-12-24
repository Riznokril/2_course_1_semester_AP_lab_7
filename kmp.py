class KMP:
    
    def __init__(self, text, pattern):
        self.results = []
        self.pattern = pattern
        self.text = text

    def find_sufix_massive(self):
        sufix_massive = [0] * len(self.pattern)
        j = 0
        i = 1
        while i < len(self.pattern):
            if self.pattern[i] == self.pattern[j]:
                sufix_massive[i] = j + 1
                i += 1
                j += 1
            else:
                if j != 0:
                    j = sufix_massive[j - 1]
                else:
                    sufix_massive[i] = 0
                    i += 1
        return sufix_massive

    def kmp(self):
        sufix_massive = self.find_sufix_massive()
        i = j = 0
        while i < len(self.text) and j < len(self.pattern):
            if self.text[i] == self.pattern[j]:
                i += 1
                j += 1
                if j == len(self.pattern):
                    self.results.append(i - j)
                    j = sufix_massive[j - 1]
            else:
                if j != 0:
                    j = sufix_massive[j - 1]
                else:
                    i += 1
        return self.results