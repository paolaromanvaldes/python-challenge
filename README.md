# Python Challenge Data Analysis Script
This Python script is designed to analyze financial and election data stored in CSV filse. For the financial analysis, the program calculates various financial metrics such as the total number of months included in the dataset, the total "Profits/Losses" over the entire period, the average change in "Profit/Loss" between months, and identifies the greatest increase and decrease in profits along with their respective dates. The election analysis, performs several calculations and generates a summary of the election results, including the total number of votes cast, the number of votes each candidate received, the percentage of votes per candidate, and determines the winner of the election.

## How to Use
### Requirements:

Python 3 installed
CSV file with election data in the specified format
CSV file with financial data in the specified format
Import necessary libraries (os and csv)

### Instructions:

Ensure the Python script and the CSV files  are in the same directory.
Update the CSV file path if stored elsewhere: 
Run the script in a Python environment.

### Code Overview
Reads the election data from the CSV file.
Calculates the total number of votes cast and identifies unique candidates.
Determines the total votes and percentage of votes each candidate received.
Determines the winner based on the highest number of votes.
### Usage
You can use this script to quickly analyze  data and obtain essential statistics. The script outputs the program results to the console and exports the analysis to a text files. 

### Sample Output
Upon running the scripts, you will see output similar to the following:<br>
Financial Analysis<br>
..........................<br>

Total: $21475215<br>

Average change: $8774.67857142857<br>

Greatest Increase in Profits: 16-Aug $1862002<br>

Greatest Increase in Profits: 14-Feb $-1825558<br>

Election Results<br>
..............................<br>
Total Votes: 369,711<br>
..............................<br>
Charles Casper Stockham: 23.049% (85,213)<br>
Diana DeGette: 73.812% (272,892)<br>
Raymon Anthony Doane: 3.139% (11,606)<br>
..............................<br>
Winner: Diana DeGette<br>

The text files will contain the same analysis details for reference.