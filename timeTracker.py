#
#   WORK TIME TRACKER by WILL GREENBERG, 2017
#       A simple timer program to help me keep track of how much time I spend on
#       any given activity, and how what I expect to be doing differs from what I
#       actually get done.
#

import time, sys
import csv
from datetime import datetime
from datetime import date

# Initial screen:

print('Welcome to TIME TRACKER!')

while True:
    print("Press enter when you're ready to begin...")
    firstInput = input()
    if firstInput == 'quit':
        sys.exit()

    print('Enter expected work to be done:')
    expectedWork = input()

    startTime = time.time()
    startTimeFormatted = datetime.now().time()
    lastTime = startTime
    lastTimeFormatted = startTimeFormatted
    adjustedStartTime = startTime
    numPauses = 0
    avgPauseTime = 0
    pauseTimes = []
    print('Session started. Good luck!')
    print('Type "help" for input options.')

# Tracking time
    while True:
        # Check for different input options - pause, done, quit

        currentInput = input()

        if currentInput == 'help':
            print('''
            Type:
                'pause' - pauses the timer, such as for a lunch or bathroom break
                'done'  - ends the timer
                'quit'  - exits the program without recording the current session
            ''')
        if currentInput == 'pause':
            pauseTime = time.time()
            numPauses += 1
            print('You have paused your timer. Press any key to continue...')
            input()
            unpauseTime = time.time()
            amtTimePaused = unpauseTime - pauseTime
            adjustedStartTime += amtTimePaused
            pauseTimes.append(amtTimePaused)
            print("Timer continues. Get workin'!")
            continue

        if currentInput == 'done':
            lastTime = time.time()
            totalWorkTime = lastTime - adjustedStartTime

            lastTimeFormatted = datetime.now().time()
            minutes, seconds = divmod(totalWorkTime, 60)
            hours, minutes = divmod(minutes, 60)
            if hours > 0:
                totalWorkTimeFormatted = '%s hours, %s minutes, %s seconds' % (int(hours), int(minutes), round(seconds, 2))
            elif minutes > 0:
                totalWorkTimeFormatted = '%s minutes, %s seconds' % (int(minutes), round(seconds, 2))
            else:
                totalWorkTimeFormatted = '%s seconds' % (round(seconds, 2))

            print('Finished! Your time spent working was: ', totalWorkTimeFormatted)

            if numPauses == 1:
                print('You paused: ', numPauses, 'time')
            else:
                print('You paused: ', numPauses, 'times')
            if numPauses > 0:
                avgPauseTime = round(sum(pauseTimes)/len(pauseTimes), 2)
                print('Your average pause time was: ', avgPauseTime, 'seconds.')

            print('Did you work on', expectedWork, 'like you planned?')
            answer = input()
            if answer == 'y' or answer == 'yes' or answer == 'yeah' or answer == 'duh' or answer == 'ye':
                doneWork = expectedWork
                print("Cool. Then you're all done. See you next time, Will!")
            else:
                print('What did you do instead?')
                doneWork = input()
                print("Nice. You're all set. See you next time, Will!")

            sessionData = [
                date.today(),            # Date - formatted
                startTimeFormatted,      # Started session
                lastTimeFormatted,       # Ended session - formatted
                totalWorkTime,           # Total time working in seconds
                totalWorkTimeFormatted,  # Total time working - formatted
                numPauses,               # Number of pauses
                avgPauseTime,            # Average pause time
                expectedWork,            # Expected work
                doneWork                 # Done work
            ]

            with open('/Users/willgreenberg/Dropbox/Developer/Python/Projects/Work Time Tracker Data/timeLogRAW.csv', 'a') as outputFile:
                outputWriter = csv.writer(outputFile)
                outputWriter.writerow(sessionData)
            break

        if currentInput == 'quit':
            sys.exit()

# First row generator:
#   outputWriter.writerow(['Date', 'Started session', 'Ended session', 'Total time working',
#                          '# of pauses', 'Average pause time', 'Expected work', 'Done work'])
