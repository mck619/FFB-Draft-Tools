import csv
import os
from prettytable import PrettyTable

def main():

    while True:
        team = raw_input("Which team's data would you like: ")
        position = raw_input("What position are you concerned about: ")
        print_team_data(team,position)


def print_team_data(team, position):

    team_info = []
    get_schedule(team, team_info)
    get_FPA_rankings(team, team_info, position)
    t = PrettyTable(['WEEK','OPPONENT','POINTS AGAINST RANKING'])
    week = 1
    for item in team_info:
        try:
            FPAR = item['FPAR']
        except:
            FPAR = 'BYE'
        t.add_row([week,item['VS'],FPAR])
        week += 1
    print t
    print_team_depth(team)

def get_schedule(team, team_info):


    c = open(os.getcwd()+'\\raw_data\\nfl-2015-schedule.csv', 'rb')

    cs = csv.reader(c)

    for row in cs:
        if team in row[6]:
            team_info.append({'VS':'BYE'})
        elif row[0] == team:
            team_info.append({'VS':row[1]})
        elif row[1] == '@'+team:
            team_info.append({'VS':row[0]})

    c.close()

def get_FPA_rankings(team, team_info, position):

    c = open(os.getcwd()+'\\raw_data\\FPA_'+position+'.csv', 'rb')

    cs = csv.reader(c)
    for item in team_info:
        if '@' in item['VS']:
            opponent = item['VS'][1:]
        else:
            opponent = item['VS']
        for row in cs:
            if opponent in row[1]:
                item['FPAR'] = row[0]
        c.seek(0)




    c.close()

def print_team_depth(team):

    c = open(os.getcwd()+'\\raw_data\\'+team+'_depth.csv', 'rb')
    cs = csv.reader(c)

    for row in cs:
        if row[0] in {'Quarterbacks','Halfbacks','Fullbacks','Wide Receivers', 'Tight Ends'}:
            print row[0]
            continue
        if row[0] == 'Depth':
            t = PrettyTable(['Depth','Player',row[8],row[9]])
            continue
        if row[0] == '':
            continue
        while row[0] in {str(x) for x in range(1,20)}:
            t.add_row([int(row[0]), row[1], row[8], row[9]])
            row = cs.next()
        print(t)

main()