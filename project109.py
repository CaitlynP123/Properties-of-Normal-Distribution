from os import stat
import statistics
from numpy import mat
import pandas as pd

data = pd.read_csv('C:/Users/C/OneDrive/Desktop/Coding/python/Normal Distribution/StudentsPerformance.csv')
mathScore = data['math score'].tolist()

mathMean = statistics.mean(mathScore)
mathMedian = statistics.median(mathScore)
mathMode = statistics.mode(mathScore)

print("Mean, Median and Mode of the Math Scores: {}, {} and, {}".format(mathMean, mathMedian, mathMode))

stdMath = statistics.stdev(mathScore)

std1startM, std1endM = mathMean - stdMath, mathMean + stdMath
std2startM, std2endM = mathMean - (stdMath * 2), mathMean + (stdMath * 2)
std3startM, std3endM = mathMean - (stdMath * 3), mathMean + (stdMath * 3)

liststd1M = [result for result in mathScore if result > std1startM and result < std1endM] 
liststd2M = [result for result in mathScore if result > std2startM and result < std2endM] 
liststd3M = [result for result in mathScore if result > std3startM and result < std3endM] 

print('{}% of data for the math scores lies within 1 standard deviation'.format(len(liststd1M) * 100.0 / len(mathScore)))
print('{}% of data for the math scores lies within 2 standard deviation'.format(len(liststd2M) * 100.0 / len(mathScore)))
print('{}% of data for the math scores lies within 3 stanadard deviation'.format(len(liststd3M) * 100.0 / len(mathScore)))

readingScore = data['reading score'].tolist()

readingMean = statistics.mean(readingScore)
readingMedian = statistics.median(readingScore)
readingMode = statistics.mode(readingScore)

print("Mean, Median and Mode of the Reading Scores: {}, {} and, {}".format(readingMean, readingMedian, readingMode))

stdReading = statistics.stdev(readingScore)

std1startR, std1endR = readingMean - stdReading, readingMean + stdReading
std2startR, std2endR = readingMean - (stdReading * 2), readingMean + (stdReading * 2)
std3startR, std3endR = readingMean - (stdReading * 3), readingMean + (stdReading * 3)

liststd1R = [result for result in readingScore if result > std1startR and result < std1endR] 
liststd2R = [result for result in readingScore if result > std2startR and result < std2endR] 
liststd3R = [result for result in readingScore if result > std3startR and result < std3endR] 

print('{}% of data for the reading scores lies within 1 standard deviation'.format(len(liststd1R) * 100.0 / len(readingScore)))
print('{}% of data for the reading scores lies within 2 standard deviation'.format(len(liststd2R) * 100.0 / len(readingScore)))
print('{}% of data for the reading scores lies within 3 stanadard deviation'.format(len(liststd3R) * 100.0 / len(readingScore)))

writingScore = data['writing score'].tolist()

writingMean = statistics.mean(writingScore)
writingMedian = statistics.median(writingScore)
writingMode = statistics.mode(writingScore)

print("Mean, Median and Mode of the Writing Scores: {}, {} and, {}".format(writingMean, writingMedian, writingMode))

stdWriting = statistics.stdev(writingScore)

std1startW, std1endW = writingMean - stdWriting, writingMean + stdWriting
std2startW, std2endW = writingMean - (stdWriting * 2), writingMean + (stdWriting * 2)
std3startW, std3endW = writingMean - (stdWriting * 3), writingMean + (stdWriting * 3)

liststd1W = [result for result in writingScore if result > std1startW and result < std1endW] 
liststd2W = [result for result in writingScore if result > std2startW and result < std2endW] 
liststd3W = [result for result in writingScore if result > std3startW and result < std3endW] 

print('{}% of data for the writing scores lies within 1 standard deviation'.format(len(liststd1W) * 100.0 / len(writingScore)))
print('{}% of data for the writing scores lies within 2 standard deviation'.format(len(liststd2W) * 100.0 / len(writingScore)))
print('{}% of data for the writing scores lies within 3 standard deviation'.format(len(liststd3W) * 100.0 / len(writingScore)))