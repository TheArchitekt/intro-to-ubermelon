log_file = open("um-server-01.txt")


def generate_sales_reports(log_file): # Defines the function with log_file as parameter
    for line in log_file: # Start of loop that iterates through each line in a log file
        line = line.rstrip() # Strips the whitespace from the right side of the line
        day = line[0:3] # This index represents the characters of the day
        if day == "Mon": # Conditional statement to do something if it lines up with the day
            print(line) # Executes the print function if the condition(s) is met


generate_sales_reports(log_file) # Calls the function with log_file as the argument
