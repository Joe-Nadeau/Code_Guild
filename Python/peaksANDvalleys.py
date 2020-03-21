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
                    print(f'{index} is a peak')
                    peaks.apend[index]
                continue
        return peaks
def valleys(data):
    
    valleys = []

def peaks_and_valleys(data):


def main():

    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

main()