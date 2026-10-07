class Gratitudes:
    def __init__(self):
        self.gratitudes = []

    def add(self, gratitude):  # add *args
        self.gratitudes.append(gratitude)
#       for gratitude in args:
#           self.gratitude.append(gratitude)

    def format(self):
        formatted = "Be grateful for: "
        formatted += ", ".join(self.gratitudes)
        return formatted
