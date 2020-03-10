def main():

    nums = [5, 0, 8, 3, 4, 1, 6]
    numsum = []
    x = 0
    for i in nums:
        x += i
        numsum.append(x)
        print(numsum)
    print(f'The sum of the numbers in the list is:{numsum[6:]}')

main()