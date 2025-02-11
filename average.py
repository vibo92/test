# Function that computes the average of a list of numbers
def average (numbers):
    return sum(numbers) / len(numbers)

# impliment the function using a splitted list from input of user
def main():
    numbers = input("Enter a list of numbers separated by space: ")
    numbers = numbers.split(" ")
    numbers = [int(x) for x in numbers]
    print("The average is:", average(numbers))
# call the main function
if __name__ == "__main__":
    main()

    