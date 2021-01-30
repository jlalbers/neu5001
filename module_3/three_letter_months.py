'''
Jameson Albers
CS 5001, Spring 2021
Module 3 Practice 10

Outputs the number of days in the inputted month.
'''


def main():
   month = input("Enter month: ")
   # determine the number of days
   if month == "Jan" or month == "January" or month == '1':
       days = 31
   elif month == "Feb" or month == "February" or month == '2':
       days = 28
   elif month == "Mar" or month == "March" or month == '3':
       days = 31
   elif month == "Apr" or month == "April" or month == '4':
       days = 30
   elif month == "May" or month == "May" or month == '5':
       days = 31
   elif month == "Jun" or month == "June" or month == '6':
       days = 30
   elif month == "Jul" or month == "July" or month == '7':
       days = 31
   elif month == "Aug" or month == "August" or month == '8':
       days = 31
   elif month == "Sep" or month == "September" or month == '9':
       days = 30
   elif month == "Oct" or month == "October" or month == '10':
       days = 31
   elif month == "Nov" or month == "November" or month == '11':
       days = 30
   elif month == "Dec" or month == "December" or month == '12':
       days = 31
   else:
       days = "Unknown"
   print(month, "has", days, "days")


main()
