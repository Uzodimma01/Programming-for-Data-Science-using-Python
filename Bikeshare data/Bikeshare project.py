import time
import pandas as pd
import numpy as np

CITY_DATA = { "chicago": "chicago.csv",
              "new york city": "new_york_city.csv",
              "washington": "washington.csv" }

def while_error_message(arguement):
    """
    This function catches a wrong selection made by the user and prints out the error message.
    It is a continuation of the while loop which keeps the line of program repeating till the specified condition is met.
    
    arg:
    A string of either city, month or day.
    """
    if arguement == "": # catches an empty input from the user which also includes white spaces.
        message = "\nSorry, you did not make any selection" 
    else:
        message = "\nError, you entered '{}' which is an invalid selection. Please check your spelling or the number selected.".format(arguement)
    print(message)
    
    
def most_common(df,column):
    '''
    This function calculates the most common event based on arguments given and prints it.

    args:
    df = DataFrame to be queried
    column = df column to be evaluated
    '''
    most_common = df[column].value_counts().idxmax()
    if column == "Start Hour":
        message = "The most common {} is {}:00".format(column, most_common)
    else:
        message = "The most common {} is {}".format(column, most_common)
    print(message)
    
    
def time_conversion(arguement):
    """
    gets the total time in seconds, converts it to the appropriate day, hour, minute and second equivalent then returns 
    the them.
    
    arg:
    seconds: the seconds valve to be converted
    """
    day = arguement // (24 * 3600)
    arguement = arguement % (24 * 3600)
    hour = arguement // 3600
    arguement %= 3600
    minute = arguement // 60
    arguement %= 60
    second = arguement
    return(int(day), int(hour), int(minute), int(second))


def time_message(total, day, hour, minute, second, message):
    '''
    Takes total, day, hour, minute and second values as args and prints the appropriate message after evaluating the values.
    The total and message values are not evaluated, it is only passed into the message to be printed
    
    args:
    int(total) = the total in seconds to be printed
    int(day) = the day in value to be printed
    int(hour) = the hour in value to be printed
    int(minute) = the minute value to be printed
    int(second) = the second value to be printed
    str(message) = the word to be passed as the subject of the message to be printed
    '''
    if day > 1:
        day_form = "days"
    else:
        day_form = "day"
    if hour > 1:
        hour_form = "hours"
    else:
        hour_form = "hour"
    if minute > 1:
        minute_form = "minutes"
    else:
        minute_form = "minute"
    if second > 1:
        second_form = "seconds"
    else:
        second_form = "second"

    if day >= 1:
        message = "The {} travel time is {} {} which is equivalent to {} {}, {} {}, {} {} and {} {}".format(message, total, second_form, day, day_form, hour, hour_form, minute, minute_form, second, second_form)
    elif day < 1 and hour >= 1:
        message = "The {} travel time is {} {} which is equivalent to {} {}, {} {} and {} {}".format(message, total, second_form, hour, hour_form, minute, minute_form, second, second_form)
    elif day < 1 and hour < 1 and minute >= 1:
        message = "The {} travel time is {} {} which is equivalent to {} {} and {} {}".format(message, total, second_form, minute, minute_form, second, second_form)
    else:
        message = "The {} travel time is {} {} which is equivalent to {} {}".format(message, total, second_form, second, second_form)
    print(message)
    

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    name = str(input("Hello there, kindly tell me your name: ")).rstrip(".").strip().title()
    if name == "":
        message = "Okay, Let's explore some US bikeshare data!"
    else:
        message = "Hello! {}, Let's explore some US bikeshare data!".format(name)
    print(message)

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ("chicago","new york city","washington")
    cities_num = ("1","2","3")
    city = str(input("\nPlease select a city between Chicago, New York City and Washington,\nCorresponding number is also accepted: ")).lower().rstrip(".").strip()
    # the code above gets input from the user, converts it to lowercase, strips any . at the end of the input
    # and also strips any whitespace at the beginning, the end or both at the beginning and end of the input.
    while city not in ("chicago","new york city","washington","1","2","3"):
        while_error_message(city) # line 9
        city = str(input("\nPlease select a city between Chicago, New York City and Washington,\nCorresponding number is also accepted: ")).lower().rstrip(".").strip()
    if city in cities_num: # if the numeric input from the user is in cities_num, the next line converts it to an integer.
        city = int(city)
        # [select -1] in the next line removes the zero indexing in python by removing one from the index
        # to make the indexing rhyme with human indexing.
        message = "You selected {}".format(cities[city -1].title())
        city = cities[city -1]
    elif city in cities:
        #the next line finds and returns the index of the input 
        city = cities.index(city)
        message = "You selected {}".format(cities[city].title())
        # int(day +1) converts day string to int and adds 1 to the index so as to return a 
        # distinct value from month all when the user selects all
        city = cities[city]
    print(message)     

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ("all","monday","tuesday","wednesday","thursday","friday","saturday","sunday")
    days_num = ("0","1","2","3","4","5","6","7") # gets a numeric input from the user in form of a string.
    day = str(input("\nPlease select a day starting from Monday,\nDay number is also accepted. You can also select all by typing 'All' or '0': ")).lower().rstrip(".").strip()
    # the code above gets input from the user, converts it to lowercase, strips any . at the end of the input
    # and also strips any whitespace at the beginning, the end or both at the beginning and end of the input.
    while day not in ("all","monday","tuesday","wednesday","thursday","friday","saturday","sunday","0","1","2","3","4","5","6","7"):
        while_error_message(day)# line 9
        day = str(input("\nPlease select a day starting from Monday,\nDay number is also accepted. You can also select all by typing 'All' or '0': ")).lower().rstrip(".").strip()
    if day in days_num: # if the numeric input from the user is in days_num, the next line converts it to an integer.
        day = int(day)
        message = "You selected {}".format(days[day].title())
        day = days[day].title()
    elif day in days:
        day = days.index(day)
        message = "You selected {}".format(days[day].title())
        day = days[day].title()
    print(message)

    # get user input for month (all, january, february, ... , june)
    months = ("all","january","february","march","april","may","june")
    months_num = ("0","1","2","3","4","5","6")
    month = str(input("\nPlease select a month between January and June,\nMonth number is also accepted. You can also select all by typing 'All' or '0': ")).lower().rstrip(".").strip()
    # the code above gets input from the user, converts it to lowercase, strips any . at the end of the input
    # and also strips any whitespace at the beginning, the end or both at the beginning and end of the input.
    while month not in ("all","january","february","march","april","may","june","0","1","2","3","4","5","6"):
        while_error_message(month)# line 9
        month = str(input("\nPlease select a month between January and June,\nMonth number is also accepted. You can also select all by typing 'All' or '0': ")).lower().rstrip(".").strip()
    if month in months_num: # if the numeric input from the user is in months_num, the next line converts it to an integer.
        month = int(month)
        message = "You selected {}".format(months[month].title())
        month = months[month].title()
    elif month in months:
        #the next line finds and returns the index of the input 
        month = months.index(month) 
        message = "You selected {}".format(months[month].title())
        month = months[month].title()
    print(message)
    return (city, month, day)

    print("-"*40)


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    # Converting the date and time columns to actual date and time objects
    df["Start Time"] = pd.to_datetime(df["Start Time"],format='%Y-%m-%d')
    df["End Time"] = pd.to_datetime(df["End Time"],format='%Y-%m-%d')
    # converts the Birth Year column to actual year date 
    if "Birth Year" in df.columns:
        df["Birth Year"] = pd.to_datetime(df["Birth Year"],format="%Y").dt.to_period("Y")
    # generating the month and day for the filter
    df["Month"] = df["Start Time"].dt.month_name()
    df["Day"] = df["Start Time"].dt.weekday_name
    df["Start Hour"] = df["Start Time"].dt.hour
    if month != "All":
        df = df[df["Month"] == month]
    if day != "All":
        df = df[df["Day"] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    # display the Most Frequent Times of Travel...
    start_time = time.time()

    # display the most common month
    print("\nCalculating the most common month of travel...")
    most_common(df, "Month")
    # display the most common day of week
    print("\nCalculating the most common day of travel...")
    most_common(df, "Day")
    # display the most common start hour
    print("\nCalculating the most common start hour of travel...")
    most_common(df, "Start Hour")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("Calculating The Most Popular Stations and Trip...")
    start_time = time.time()

    # display most commonly used start station
    print("\nCalculating the most commonly used start station for travel...")
    most_common(df, "Start Station")
    # display most commonly used end station
    print("\nCalculating the most commonly used end station for travel...")
    most_common(df, "End Station")
    # display most commonly used start station and end station combination
    print("\nCalculating the most frequent combination of start station and end station trip...")
    combined_station = (df["Start Station"] + " and " + df["End Station"]).mode()[0]
    print("The most frequent combination of start and end station is ",combined_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("Calculating Trip Duration...")
    start_time = time.time()

    print("\nCalculating the total travel time...")
    total_duration = df["Trip Duration"].sum()
    day, hour, minute, second = time_conversion(total_duration) # calling the time_conversion function
    time_message(total_duration, day, hour, minute, second, "total") # calling the time_message function

    print("\nCalculating the average travel time...")
    mean_duration = df["Trip Duration"].mean()
    day, hour, minute, second = time_conversion(mean_duration) # calling the time_conversion function
    time_message(mean_duration, day, hour, minute, second, "average") # calling the time_message function

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""    

    print("Calculating User Stats...")
    start_time = time.time()
    print("\nCalculating the counts of user types...")
    print("The number of user types are shown below")
    user_types = df["User Type"].value_counts()
    print(user_types)
    
    print("\nCalculating the counts of gender...")
    if "Gender" in df.columns:  
        gender = df["Gender"].value_counts()
        print("The number of male and female bike users are shown below")
        print(gender)
    else:
        print("Data not available in the selected city")
    
    print("\nCalculating earliest year of birth...")
    if "Birth Year" in df.columns:
        earliest_year_of_birth = df["Birth Year"].min()
        print("The earliest birth year is {}".format(earliest_year_of_birth))
    else:
        print("Data not available in the selected city")
      
    print("\nCalculating recent year of birth...")
    if "Birth Year" in df.columns:  
        recent_year_of_birth = df["Birth Year"].max()
        print("The recent birth year is {}".format(recent_year_of_birth))
    else:
        print("Data not available in the selected city")
 
    print("\nCalculating the most common birth year...")
    if "Birth Year" in df.columns:
        most_common(df, "Birth Year")
    else:
        print("Data not available in the selected city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*40)
    
    raw_data = input("Would you like to view the raw data?\nType 'Yes' or 'Y' to view: ").lower().rstrip(".").strip()
    reply = ("y","yes")
    if raw_data in reply:
        print("Okay, let's proceed")
        df = df.drop(["Unnamed: 0","Start Time","End Time","Month","Day","Start Hour"], axis =1) # drops the irrelevant columns
        sample_view = ("sample","s")
        view = input("Enter 'Sample' to view sample data OR enter the number of data to view in each batch between '1' and '{}' per batch,\nFor better view, kindly choose at most 50 data to be displayed per batch: ".format(len(df.index))).lower().rstrip(".").strip()
        proceed = ("y","yes","")
        if view.isalpha():
            if view in sample_view:
                print("\n\nCalculating the first 10 US bikeshare data...")
                top = df.head(10)
                print("The first 10 US bikeshare data is \n\n{}".format(top))
                print("\n\nCalculating the last 10 US bikeshare data...")
                bottom = df.tail(10)
                print("The last 10 US bikeshare data is \n\n{}".format(bottom) + "\n\nEnd of data")
            else:
                print("\nSorry, {} is a wrong entry, now ending the program...\n".format(view))
        elif "." not in view and view != "0":
            if view.isnumeric():
                print("Loading...")
                view = int(view)
                current_value = view
                data = df.iloc[:view]
                print(data)
                more_view = input("Do you want to view the next batch of data?\nUse either 'Yes', 'Y' or hit 'enter' button to proceed: ").lower().rstrip(".").strip()
                while more_view in proceed and current_value <= len(df.index) and view != "0":
                    print("Loading...")
                    next_value = current_value+view
                    previous_value = current_value
                    data = df.iloc[previous_value:next_value]
                    current_value += view
                    print(data) 
                    more_view = input("Do you want to view the next batch of data?\nUse either 'Yes', 'Y' or 'enter' button to proceed: ").lower().rstrip(".").strip()
                else:
                    print("End of data\n")
        elif "." in view or eval(view) == 0:
            print("\nSorry, {} is a wrong entry, now ending the program...\n".format(view))
        print("Okay, thank's for coming")
        
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != "yes":
            break


if __name__ == "__main__":
    main()
