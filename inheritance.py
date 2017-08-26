
class Race():

    def get_race(self):
        return " extension "

    def get_racial_ability(self):
        return self.racial_ability



class Khajit(Race):

    race = "khajit"
    racial_ability = "night sight"
    occupation = "thief"

    def get_race(self):
        super().get_race()
        return self.race + super().get_race()

    def get_occupation(self):
        return self.occupation


class Nord(Race):

    race = "nord"
    racial_ability = "war cry"
    occupation = "warrior"

    @property
    def get_race(self):
        return self.race + super().get_race() + "of skyrim"

    @property
    def get_occupation(self):
        return self.occupation


class Karjo(Khajit):

    occupation = "guard"

    # extend
    def get_race(self):
        return super().get_race

    #override
    def get_occupation(self):
        return self.occupation


class Miraak(Nord):

    occupation = "sorcerer"

    def get_race(self):
        return "immortal " + super().get_race

    def get_occupation(self):
        return self.occupation
