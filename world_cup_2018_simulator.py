import itertools

# Functions

# the fixture function finds the result of the two teams
def Fixture(team1, team2, draws_allowed)
    r = rand()
    team1.points +=

# the groupstage function resolves all the fixtures within a group stage and stores the results inside the team class
def GroupStage(team_names_in_group)


    match_fixtures = itertools.combinations(team_names_in_group,2)
    for team1, team2 in match_fixtures
        Fixture(team1, team2, draws_allowed=True)


# the Finals function resolves the knock out stages of the finals
def Finals(group_winners)
    Fixture(T1, T2, draws_allowed=False)

# define Team class
class Team:
    def __init__(self, team, rank, group):
        self.team = team
        self.rank = rank
        self.group = group
        self.fixtures = []
        self.points = 0
        self.result = []
        self.goal_difference = []

# input data
# team name, FIFA rank, group ID
# 'England', 8, 'E'

# load csv
data = load....

# for each row in csv, make an instance of the Team class.
teams_list = [Team(team, rank, group) for team, rank, group in data]

# isolate the teams by the group they appear in
teams_in_group = itertools.groupby(teams_list, lambda x: x.GroupId)

group_winners = GroupStage(teams_in_group)

winner = Finals(group_winners)


