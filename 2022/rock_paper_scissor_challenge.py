import pandas as pd
import datetime as dt
summer = 0
#rps_data = pd.read_csv("rps_sample.txt", sep=" ", header=None)
rps_data = pd.read_csv("rps_challenge_data.txt", sep=" ", header=None)
rps_data.columns = ["them", "us"]
rps_convert = pd.DataFrame()
print(rps_data.shape)
rightNow = dt.datetime.now()
date_label = rightNow.strftime("%m%d%Y_%H%M%S")
print(date_label)

rock = 1
paper = 2
scissors = 3
win = 6
tie = 3
lose = 0
them = 0
us = 0
ourscore = 0
theirscore = 0
ourscores = []
theirscores = []
wins = 0
ties = 0
losses = 0
tSelection = []
oSelection = []
winLose = []
uChoice = ""
tChoice = ""


def score_eval(score):
    if score == "A":  # or score == "X"
        score = "Rock"
    elif score == "B":  # or score == "Y"
        score = "Paper"
    elif score == "C":  # or score == "Z"
        score = "Scissors"
    return score


def choice_value(score):
    if score == "Rock":  # or score == "X":
        score = 1
    elif score == "Paper":  # or score == "Y":
        score = 2
    elif score == "Scissors":  # or score == "Z":
        score = 3
    return score


def theFix(tChoice, us):
    if us == "X":
        if tChoice == "Rock":
            score = "Scissors"
        elif tChoice == "Scissors":
            score = "Paper"
        else:
            score = "Rock"
    elif us == "Y":
        score = tChoice
    else:
        if tChoice == "Rock":
            score = "Paper"
        elif tChoice == "Scissors":
            score = "Rock"
        else:
            score = "Scissors"
    return score


# print(rps_data.columns())
# for i in range(len(rps_data)):
# print(rps_data['them'])
# print(rps_data['us'])
for i in range(len(rps_data)):
    them = rps_data['them'][i]
    us = rps_data['us'][i]
    tChoice = score_eval(them)
    uChoice = theFix(tChoice, us)

    if (tChoice == "Rock" and uChoice == "Scissors") or (tChoice == "Scissors" and uChoice == "Paper") or (tChoice == "Paper" and uChoice == "Rock"):
        winLose.append("Loss")
        losses += 1
        ourscore = ourscore + choice_value(uChoice)
        ourscores.append(choice_value(us))
        oSelection.append(uChoice)
        theirscore = theirscore + choice_value(tChoice) + win
        theirscores.append(choice_value(tChoice) + win)
        tSelection.append(tChoice)
    elif (tChoice == "Rock" and uChoice == "Paper") or (tChoice == "Paper" and uChoice == "Scissors") or (tChoice == "Scissors" and uChoice == "Rock"):
        winLose.append("Win")
        wins += 1
        ourscore = ourscore + choice_value(uChoice) + win
        ourscores.append(choice_value(uChoice)+win)
        oSelection.append(uChoice)
        theirscore = theirscore + choice_value(tChoice)
        theirscores.append(choice_value(tChoice))
        tSelection.append(tChoice)
    else:
        winLose.append("Tie")
        ties += 1
        ourscore = ourscore + choice_value(uChoice) + tie
        ourscores.append(choice_value(uChoice) + tie)
        oSelection.append(uChoice)
        theirscore = theirscore + choice_value(tChoice) + tie
        theirscores.append(choice_value(tChoice)+tie)
        tSelection.append(tChoice)

rps_data['themValue'] = theirscores
rps_data['usValue'] = ourscores
rps_data['theirSelection'] = tSelection
rps_data['ourSelection'] = oSelection
rps_data['WinLose'] = winLose
print(ourscore)
print(theirscore)
print("wins", wins, " ties", ties, " losses", losses)
print(rps_data)
rps_data.to_csv("rps_fixed_"+date_label+".csv", index=False)
