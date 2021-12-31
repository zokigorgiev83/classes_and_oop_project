class School:
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_numberOfStudents(self):
        return self.numberOfStudents

    def set_numberOfStudents(self, new_num_of_students):
        self.numberOfStudents = new_num_of_students

    def __repr__(self):
        return "A {} school named {} with {} students.".format(
            self.level, self.name, self.numberOfStudents
        )


class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, "primary", numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def get_pickupPolicy(self):
        return self.pickupPolicy

    def __repr__(self):
        superClass_repr = super().__repr__()
        return superClass_repr + "The pickup policy is '{}'.".format(self.pickupPolicy)


class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, "high", numberOfStudents)
        self.sportsTeams = sportsTeams

    def get_sportsTeams(self):
        return ", ".join(self.sportsTeams[:-1]) + ", and " + self.sportsTeams[-1]

    def __repr__(self):
        superClass_repr = super().__repr__()
        return (
            superClass_repr
            + " The active sports teams in the school are the following: {}.".format(
                ", ".join(self.sportsTeams[:-1]) + ", and " + self.sportsTeams[-1]
            )
        )


class MiddleSchool(School):
    def __init__(self, name, numberOfStudents):
        super().__init__(name, "middle", numberOfStudents)
