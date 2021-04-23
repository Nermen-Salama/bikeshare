import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new_york_city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    while True:
        city=input("Would you like to see data for Chicago, New_York_city, or Washington?").lower()
        if city in CITY_DATA.keys():
            print("You just select : " + city.title() + " City")
            break
        else:
            print("Please Try again, please select from (Chicago, New York, or Washington) cities")
    while True:
        filter_selection = input("Would you like to filter the data by (month, day, or not_at_all)?").lower()
        if filter_selection == "month":
            print("You just select filtering data by : " + filter_selection.title())
            month_selection = input("Which month - January, February, March, April, May, or June?").lower()
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            if month_selection in months:
                print("You just select filtering data by : " + month_selection.title())
                # filter by month to create the new dataframe
                day_selection ="all"
                break
        elif filter_selection == "day": 
            print("You just select filtering data by : " + filter_selection.title())
            day_selection = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?").lower()
            days=['Which day', 'monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday','sunday']
            if day_selection in days:
                print("You just select filtering data by : " + day_selection.title())
                month_selection = "all"
            break
        elif filter_selection == "not_at_all":
                print("You just select filtering data by : " + filter_selection.title())
                month_selection = "all"
                day_selection ="all"
                break
        else :
                print("Please Try again, please select from (month, day, or not_at_all)")
    print('-'*40)
    print('-'*40)

    #return "Loading the data for: {} city,at {} week(s) for {} day(s)......".format(city, month_selection, day_selection)
    return city, month_selection, day_selection, filter_selection
     
    print('-'*40)
    print('-'*40)
def load_data(city, month_selection, day_selection, filter_selection):
    print("\nLoading the data for: ",city + " city, ", "at ", month_selection  + " week(s) for " ,day_selection + " day(s).......\n")
    filename = city +'.csv'
    # load data file into a dataframe
    df =  pd.read_csv(filename)
    while True:
        if filter_selection == "month":
            df['Start Time'] = pd.to_datetime(df['Start Time'])
            df['Month'] = df['Start Time'].dt.month_name()
            df['Month'] = df['Month'].str.lower()
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            if month_selection in months:
                # filter by month to create the new dataframe
                df = df[df['Month'] == month_selection]
                day_selection ="all"
                print(df.head())
                break

        elif filter_selection == "day": 
            df['Start Time'] = pd.to_datetime(df['Start Time'])
            df['Day_of_week'] = df['Start Time'].dt.day_name()
            df['Day_of_week'] = df['Day_of_week'].str.lower()
            days=['Which day', 'monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday','sunday']
            if day_selection in days:
                df = df[df['Day_of_week'] == day_selection]
                month_selection = "all"
                print(df.head())
                break
        elif filter_selection == "not_at_all":
                df['Start Time'] = pd.to_datetime(df['Start Time'])
                df['Month'] = df['Start Time'].dt.month_name()
                df['Month'] = df['Month'].str.lower()
                df['Day_of_week'] = df['Start Time'].dt.day_name()
                df['Day_of_week'] = df['Day_of_week'].str.lower()
                month_selection = "all"
                day_selection ="all"
                print(df.head())
                break
        else :
                print("Please Try again, please select from (month, day, or not_at_all)")
    print('-'*40)
    print('-'*40)

    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    com_month=df['Month'].mode()[0]
    print("The most common month is: ",com_month)
   
    #return "The most comm : {} ".format(com_month)

    # display the most common day of week
    
    com_day=df['Day_of_week'].mode()[0]
    print("The most common day is: ",com_day)
    # display the most common start hour
    df['com_start_hour'] = df['Start Time'].dt.hour
    com_start_hour=df['com_start_hour'].mode()[0]
    print("The most common start time is: ",com_start_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('-'*40)
    return df
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    com_st_st = df['Start Station'].mode()[0]
    print("The most common Start Station is: ",com_start_hour)
    # display most commonly used end station
    com_end_st = df['End Station'].mode()[0] 
    print("The most common End Station is: ",com_start_hour)
    # display most frequent combination of start station and end station trip
    df['Most_com_Trip']= df['Start Station'] + " to " + df['End Station']
    com_trip=df['Most_com_Trip'].mode()[0]
    print("The most common Trip is: ",com_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("user_types: ",user_types)

    # Display counts of gender
    Gender = df['Gender'].value_counts()
    print("Gender: ",Gender)

    # Display earliest, most recent, and most common year of birth

    print("user_types: {}, Gender: {}".format(user_types, Gender))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    def main():
    while True:
        city, month, day, filterselect = get_filters()
        df = load_data(city, month, day, filterselect)
        time_stats(df)
        station_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
