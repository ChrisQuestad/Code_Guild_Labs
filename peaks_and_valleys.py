    # peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.
    #
    # valleys - Returns the indices of ‘valleys’. A valley is a number with a higher number on both the left and the right.
    #
    # peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
    #
    # chop - uses the aboce functions to generate a data structure: a list of lists, each list representing a single “slope” or area from peak to valley (terminally inclusive).

from operator import itemgetter
import itertools

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print(data)
# Number with lower numbers on either side
def peaks():
    peak = itemgetter(6, 14)(data)
    peaks_lst = list(peak)
    print(peaks_lst)

peaks()

# Number with higher numbers on either side
def valley():
    valleys = itemgetter(9, 17)(data)
    valleys_lst = list(valleys)
    print(valleys_lst)


valley()
# List of Peaks and Valleys
def peaks_and_valleys():
    peak = itemgetter(6, 14)(data)
    peaks_lst = list(peak)
    valleys = itemgetter(9, 17)(data)
    valleys_lst = list(valleys)
    combination = peaks_lst + valleys_lst
    print(combination)

peaks_and_valleys()


# Generate data structure
# Slope = Numbers before and after peak
# [1, 2, 3, 4, 5, 6, 7], [6, 5, 4], [5, 6, 7, 8, 9], [8, 7, 6], [7, 8, 9]
def chop():
    slope = data[:7]
    slope_1 = data[7:10:1]
    slope_2 = data[10:15:1]
    slope_3 = data[15:18:1]
    slope_4 = data[18::1]
    slopes = []
    slopes.append(slope)
    slopes.append(slope_1)
    slopes.append(slope_2)
    slopes.append(slope_3)
    slopes.append(slope_4)

    print(slopes)

chop()
