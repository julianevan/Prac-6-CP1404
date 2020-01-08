class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        """defining constructor __init__ with instances such as name, typing, reflection and year"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """defining function is_dynamic"""
        return self.typing

    def get_name(self):
        """defining function get_name"""
        return self.name

    def __str__(self):
        """for string formatting"""
        return "{}, {} Typing, Reflection={}, first appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)
