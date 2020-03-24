#PDX Code Guild
#Lab 18
#Peaks and Valleys
#Joey Nadeau

def peaks(data):
        
        peaks = []
        # creates a list of indices that is equal to the length(or number of items) in the list named 'data'
        indices  = list(range(len(data))) 
        # for each item in the list named 'indices' do the following:
        for index in indices:
            # if there is an index in the position before the specified index and there is an idex in the position after the specified index, then do the following:
            if (index - 1) in indices and (index + 1) in indices:
                # if a certain index in the list named 'data' is greater than or equal to the index in the prior position AND it is greater than or equal to the index in the following position, then do the following:
                if data[index] is >= data[index - 1] and data[index] >= data[index + 1]:
                    # prints the index specified in line 16 and labels it a 'peak'
                    print(f'{index} is a peak')
                    # adds the index specified in line 16 to the list 'peaks'
                    peaks.apend[index]
                # repeats the for loop for the next item in the list 'indices'
                continue
        # returns the appended list 'peaks'
        return peaks
        
def valleys(data):
    
    valleys = []
    indices  = list(range(len(data)))
    for index in indices:
        if (index - 1) in indices and (index + 1) in indices:
            if data[index] is >= data[index - 1] and data[index] >= data[index + 1]:
                print(f'{index} is a valley')
                valleys.apend[index]
            continue
    return valleys

def peaks_and_valleys(data):


def main():

    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    print(peaks(data))
    print(valleys(data))

main()