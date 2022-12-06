import pandas as pd
summer = 0
#rps_data = pd.read_csv("rps_sample.txt", sep=" ", header=None)
rps_data = pd.read_csv("rps_challenge_data.txt", sep=" ", header=None)
rps_data.columns = ["them", "us"]
rps_convert = pd.DataFrame()
print(rps_data.shape)

rock = 1
paper = 2
scissors = 3
win = 6
lose = 0
tie = 3
them = 0
us = 0
ourscore = 0
theirscore = 0
ourscores = []
theirscores = []
wins = 0
ties = 0
losses = 0


def score_eval(score):
    if score == "A" or score == "X":
        score = 1
    elif score == "B" or score == "Y":
        score = 2
    elif score == "C" or score == "Z":
        score = 3
    return score


# print(rps_data.columns())
# for i in range(len(rps_data)):
# print(rps_data['them'])
# print(rps_data['us'])
for i in range(len(rps_data)):
    them = rps_data['them'][i]
    us = rps_data['us'][i]
    them = score_eval(them)
    us = score_eval(us)

    if them > us:
        losses += 1
        if us == rock:
            ourscore = ourscore + rock
            ourscores.append(rock)
        elif us == paper or them == p:
            ourscore = ourscore + paper
            ourscores.append(paper)
        else:
            ourscore = ourscore + scissors
            ourscores.append(scissors)
        if them == scissors:
            theirscore = theirscore + scissors + win
            theirscores.append(scissors + win)
        elif them == paper:
            theirscore = theirscore + paper + win
            theirscores.append(paper+win)

    elif them < us:
        wins += 1
        if us == paper:
            ourscore = ourscore + paper + win
            ourscores.append(paper + win)
        else:
            ourscore = ourscore + scissors + win
            ourscores.append(scissors + win)
        if them == rock:
            theirscore = theirscore + rock
            theirscores.append(rock)
        elif them == paper:
            theirscore = theirscore + paper
            theirscores.append(paper)
        else:
            theirscore = theirscore + scissors
            theirscores.append(scissors)

    else:
        ties += 1
        if us == rock:
            ourscore = ourscore + rock + tie
            theirscore = theirscore + rock + tie
            ourscores.append(rock+tie)
            theirscores.append(rock+tie)
        elif us == paper:
            ourscore = ourscore + paper + tie
            theirscore = theirscore + paper + tie
            ourscores.append(paper + tie)
            theirscores.append(paper + tie)
        else:
            ourscore = ourscore + scissors + tie
            theirscore = theirscore + scissors + tie
            ourscores.append(scissors + tie)
            theirscores.append(scissors + tie)
rps_convert['them'] = theirscores
rps_convert['us'] = ourscores
print(ourscore)
print(theirscore)
print("wins", wins, " ties", ties, " losses", losses)
print(rps_convert.head())
print(rps_convert.shape)
