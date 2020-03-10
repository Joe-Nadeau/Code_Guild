def main():
    nums = []
    def user_numlist():
            
        while True:
            user_input = input('Enter a number or type \'done\': ')
            if user_input == 'done':
                break
            nums.append(int(user_input))

    user_numlist()
    numsum = []
    x = 0
    for i in nums:
        x += i
        numsum.append(x)
        print(numsum)
    print(f'The sum of the numbers in the list is:{numsum[len(numsum)-1]}')
    print(f'The average of the numbers in the list is: {numsum[len(numsum)-1] / len(numsum)}')

main()