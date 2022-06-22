import random
noOfStreak = 0
Streak = 0
FlipType = []
StreakExists = False

for exp in range(10000):

    for i in range(100):
        FlipType.append(random.randint(0,1))
    for i in range(len(FlipType)):
        if i == 0:
            pass
        elif FlipType[i] == FlipType[i-1]:
            Streak += 1
        else:
            Streak = 0

        if Streak == 6:
            StreakExists = True

    if StreakExists:
        noOfStreak += 1
    Streak = 0
    FlipType = []
    StreakExists = False

print('Total Number of Streaks = ',noOfStreak/100, '%')
