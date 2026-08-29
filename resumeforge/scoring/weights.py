class WeightTable:
    def __init__(self):
        self.weights = {}

    def add(self, keyword, weight):
        self.weights[keyword.lower()] = weight

    def get(self, keyword):
        return self.weights.get(keyword.lower(), 1)