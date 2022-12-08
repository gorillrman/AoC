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


def score_eval(score):
    if score == "A" or score == "X":  # rock
        score = 1
    elif score == "B" or score == "Y":  # paper
        score = 2
    elif score == "C" or score == "Z":  # scissors
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

    if them > us:  # loss
        losses += 1
        # update our score
        if us == rock:  # 1 point for rock
            ourscore = ourscore + rock
            ourscores.append(rock)  # appending to score tracker list for us
        elif us == paper  # 2 points for paper
        ourscore = ourscore + paper
        ourscores.append(paper)
        else:
            ourscore = ourscore + scissors  # 3 points for scissors
            ourscores.append(scissors)
        # update their score
        if them == scissors:
            # 3 points for scissors and 6 points for win
            theirscore = theirscore + scissors + win
            theirscores.append(scissors + win)
        elif them == paper:
            theirscore = theirscore + paper + win  # 2 points for paper and 6 points for win
            theirscores.append(paper+win)b
        # No need to test for rock it would be a loss or a tie

    elif them < us:  # testing for win
        wins += 1  # update wins count
        if us == paper:
            ourscore = ourscore + paper + win  # 2 points for paper and 6 points for win
            ourscores.append(paper + win)
        else:
            # 3 points for scissors and 6 points for win
            ourscore = ourscore + scissors + win
            ourscores.append(scissors + win)
        if them == rock:
            theirscore = theirscore + rock  # 1 point for rock and 0 for loss
            theirscores.append(rock)
        elif them == paper:  # 2 points for paper and 0 for loss
            theirscore = theirscore + paper
            theirscores.append(paper)
        else:
            theirscore = theirscore + scissors  # 3 points for scissors
            theirscores.append(scissors)

    else:  # default for ties
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
print("Our score ", ourscore)
print("Their score ", theirscore)
print("wins", wins, " ties", ties, " losses", losses)
print(rps_convert.head())
print(rps_convert.shape)
