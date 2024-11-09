# Name: Jayden Shofolahan
# Date: 11/06/2024
# Description: This file will modify a program with months

def monthString(monthNum):
    """
    Takes as input a number, monthNum, and
    returns the corresponding month name as a string.
    Example: monthString(1) returns "January".
    Assumes that input is an integer ranging from 1 to 12 """
   
    monthString = ""
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] 
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,] 
    monthString = monthString + months[monthNum - 1]
      


    return monthString





def main():
    n = int(input('Enter the number of the month: '))
    mString = monthString(n)
    print('The month is', mString)


# Allow script to be run directly:
if __name__ == "__main__":
    main()
