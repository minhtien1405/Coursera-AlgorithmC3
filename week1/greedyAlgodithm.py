def score1(w, l):
    return w - l

def score2(w, l):
    return w/float(l)

def sortJobs (jobList, scoreFunc):
    scoreJobList = [(w,l, scoreFunc (w,l)) for w, l in jobList ]
    scoreJobList.sort(key=lambda tup: tup[0], reverse=True)   # sort by weight first to resolve ties
    scoreJobList.sort(key=lambda tup: tup[2], reverse=True)   # sort by score function
    return scoreJobList;

def loadData(fName):
    with open(fName,'r') as fileObj:
        lines = fileObj.readlines()
        numJobs = int (lines[0].strip())
        jobList = [ (int(line.split()[0]), int(line.split()[1])) for line in lines[1:]]
    return jobList

def sumCompletionTimes (sortedJobList):
    weightedSum = 0
    lengthSum = 0
    
    for job in sortedJobList:
        lengthSum += job[1]
        weightedSum += job[0] * lengthSum
        
    return weightedSum, lengthSum
    
def main(fName):
    jobList = loadData(fName);
    scoreJobList = sortJobs(jobList, score2)    #change to score1 or score2
    weightedSum, lengthSum = sumCompletionTimes (scoreJobList)
    print(weightedSum, lengthSum)
    
if __name__ == '__main__':
    main('jobs.txt')
    
#Score1: 69119377652 510289
#Score2: 67311454237 510289