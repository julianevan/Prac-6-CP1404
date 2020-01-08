class Guitar:
    year = 0
    cost = 0

    def __init__(self,name,year,cost):
        """defining constructor __init__ with instances name, year, cost"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """for string formatting"""
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        """for age of guitar"""
        return 2019 - self.year

    def is_vintage(self):
        """Determining if a guitar is vintage or not"""
        return self.get_age() >= 50
