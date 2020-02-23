import csv
import sys
import random

class Person:
    matches = []
    second_matches = []
    excluded = []

    def __init__(self, name, family):
        self.name = name
        self.family = family
        self.excluded = []
        self.exclude(self)
        self.matches = []
        self.second_matches = []

    def exclude(self, to_exclude):
        self.excluded.append(to_exclude)

    def is_excluded(self, person):
        return (person in self.excluded)

    def match(self, person):
        self.matches.append(person)
        self.exclude(person)

    def second_match(self, person):
        self.second_matches.append(person)
        self.exclude(person)

    def to_csv(self):
        str_out = self.name
        for i in range(len(self.matches)):
            str_out += ","
            if self.second_matches[i] == None:
                str_out += self.matches[i].name
            else:
                str_out += self.matches[i].name + " + " + self.second_matches[i].name
        str_out += "\n"
        return str_out

def load_team(name):
    with open(name, "r") as csvfile:
        team = []
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            team.append(Person(row[0], row[1]))
    return team

def exclude_families(team):
    for member in team:
        for match in team:
            if match != member and match.family == member.family:
                member.exclude(match)

def pair_team(team):
    if len(team) % 2 == 1:
        pair_odd_team(team)
    else:
        pair_even_team(team)

def pair_odd_team(team):
    idx = 0
    while idx < len(team):
        if idx == 0:
            if team[0].is_excluded(team[1]) or team[0].is_excluded(team[2]) or team[1].is_excluded(team[2]):
                random.shuffle(team)
                idx = 0
            else:
                idx += 3
        else:
            if team[idx].is_excluded(team[idx+1]):
                random.shuffle(team)
                idx = 0
            else:
                idx += 2

    team[0].match(team[1])
    team[1].match(team[0])
    team[0].second_match(team[2])
    team[1].second_match(team[2])
    team[2].match(team[0])
    team[2].second_match(team[1])
    for i in range(3, len(team), 2):
        team[i].match(team[i+1])
        team[i+1].match(team[i])
        team[i].second_match(None)
        team[i+1].second_match(None)
    return True

def pair_even_team(team):
    idx = 0
    while idx < len(team):
       if team[idx].is_excluded(team[idx+1]):
           random.shuffle(team)
           idx = 0
       else:
           idx += 2

    for i in range(0, len(team)):
        team[i].match(team[i+1])
        team[i+1].match(team[i])
        team[i].second_match(None)
        team[i+1].second_match(None)
    return True

def write_pairings(team, name, num_weeks):
    with open(name, 'w+') as csvfile:
        for i in range(num_weeks):
            csvfile.write(",Week {0}".format(num_weeks))
        for member in team:
            csvfile.write(member.to_csv())

if __name__ == "__main__":
    assert len(sys.argv) == 4
    team = load_team(sys.argv[1])
    exclude_families(team)
    for i in range(int(sys.argv[3])):
        print("Pairing {0}th week...".format(i))
        pair_team(team)
    write_pairings(team, sys.argv[2], int(sys.argv[3]))
