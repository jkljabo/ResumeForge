class SectionWeights:
    def __init__(self):
        self.weights = {
            "experience": 5,
            "projects": 3,
            "skills": 2,
            "certifications": 1,
        }

    def get(self, section):
        return self.weights.get(section, 1)

    def add(self, section, weight):
        self.weights[section] = weight