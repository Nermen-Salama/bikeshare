import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new_york_city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    while True:
        # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        city=input("Would you like to see data for Chicago, New_York_city, or Washington?").lower()
        if city in CITY_DATA.keys():
            print("You just select : " + city.title() + " City")
            break
        else:
            print("Please Try again, please select from (Chicago, New York, or Washington) cities")
    while True:
       
        # Get user input for the data by month, day, or not at all?
        
        filter_selection = input("Would you like to filter the data by (month, day, or not_at_all)?").lower()
        
        # Get user input for month (all, january, february, ... , june)
        
        if filter_selection == "month":
            print("You just select filtering data by : " + filter_selection.title())
            month_selection = input("Which month - January, February, March, April, May, or June?").lower()
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            if month_selection in months:
                print("You just select filtering data by : " + month_selection.title())
                
                day_selection ="all"
                break
            else :
                print("Please Try again, please select from (January, February, March, April, May, or June)")
        
        # get user input for day of week (all, monday, tuesday, ... sunday)
        
        elif filter_selection == "day": 
            print("You just select filtering data by : " + filter_selection.title())
            day_selection = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?").lower()
            days=['Which day', 'monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday','sunday']
            if day_selection in days:
                print("You just select filtering data by : " + day_selection.title())
                month_selection = "all"
                break
            else :
                print("Please Try again, please select from (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday)")      
        elif filter_selection == "not_at_all":
                print("You just select filtering data by : " + filter_selection.title())
                month_selection = "all"
                day_selection ="all"
                break
        else :
                print("Please Try again, please select from (month, day, or not_at_all)")
    print('-'*40)
    print('-'*40)

    return city, month_selection, day_selection, filter_selection
     
    print('-'*40)
    print('-'*40)

    
def load_data(city, month_selection, day_selection, filter_selection):
    print("\nLoading the data for: ",city + " city, ", "at ", month_selection  + " week(s) for " ,day_selection + " day(s).......\n")
    filename = city +'.csv'
    # Load data file into a dataframe
    df =  pd.read_csv(filename)
    while True:
        if filter_selection == "month":
            df['Start Time'] = pd.to_datetime(df['Start Time'])
            df['Month'] = df['Start Time'].dt.month_name()
            df['Month'] = df['Month'].str.lower()
            df['Day_of_week'] = df['Start Time'].dt.day_name()
            df['Day_of_week'] = df['Day_of_week'].str.lower()
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            if month_selection in months:
                # create the new dataframe column for Month
                df = df[df['Month'] == month_selection]
                day_selection ="all"
                #print(df.head())
                break

        elif filter_selection == "day": 
            df['Start Time'] = pd.to_datetime(df['Start Time'])
            df['Day_of_week'] = df['Start Time'].dt.day_name()
            df['Day_of_week'] = df['Day_of_week'].str.lower()
            df['Month'] = df['Start Time'].dt.month_name()
            df['Month'] = df['Month'].str.lower()
            days=['Which day', 'monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday','sunday']
            if day_selection in days:
                
                # create the new dataframe column for Day_of_week

                df = df[df['Day_of_week'] == day_selection]
                month_selection = "all"
                #print(df.head())
                break
        elif filter_selection == "not_at_all":
                df['Start Time'] = pd.to_datetime(df['Start Time'])
                df['Month'] = df['Start Time'].dt.month_name()
                df['Month'] = df['Month'].str.lower()
                df['Day_of_week'] = df['Start Time'].dt.day_name()
                df['Day_of_week'] = df['Day_of_week'].str.lower()
                month_selection = "all"
                day_selection ="all"
                #print(df.head())
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

    # Display the most common month
    com_month=df['Month'].mode()[0]
    print("The most common month is     : ",com_month)

    # Display the most common day of week
    
    com_day=df['Day_of_week'].mode()[0]
    print("The most common day is       : ",com_day)
    
    # Display the most common start hour
    
    df['start_hour'] = df['Start Time'].dt.hour
    com_start_hour=df['start_hour'].mode()[0]
    print("The most common start time is: ",com_start_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('-'*40)
    return df


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    
    com_st_st = df['Start Station'].mode()[0]
    print("The most common Start Station is: ",com_st_st)
    
    # Display most commonly used end station
    
    com_end_st = df['End Station'].mode()[0] 
    print("The most common End Station is  : ",com_end_st)
    
    # Display most frequent combination of start station and end station trip
    
    df['Most_com_Trip']= df['Start Station'] + " to " + df['End Station']
    com_trip=df['Most_com_Trip'].mode()[0]
    print("The most common Trip is         : ",com_trip)
    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)
    print('-'*40)

    
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    user_types = df['User Type'].value_counts()
    print("User_types:\n",user_types)
    print('-'*40)
    
    # Display counts of Gender
    
    column_val=list(df.columns)
    if "Gender" in column_val:
        Gender = df['Gender'].value_counts()
        print("Gender    :\n",Gender)
    else: print("Gender    : There is no Gender data")
  
    
    # Display earliest, most recent, and most common year of birth
    
    
    
    if "Birth Year" in column_val:
        
        # Display earliest year of birth
        
        earliest_year = min(df['Birth Year'])
        print("The earlist year of birth is    : ",earliest_year)
        
        # Display most recent year of birth
        
        recent_year = max(df['Birth Year'])
        print("The most recent year of birth is: ",recent_year)

        # Display Most common year of birth
        
        Birth = df['Birth Year'].mode()[0]
        print("The most common year of birth is: ",Birth)
        
    else: print("Birth     :There is no Birth Year data")
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('-'*40)

    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    
    total_trip=df['Trip Duration'].sum()
    print("Total trip duration    : ",total_trip)
    
    # Display mean travel time
    
    mean_trip=int(df['Trip Duration'].mean())
    print("Mean trip duration     : ",mean_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def main():
    
    while True:
        city, month, day, filterselect = get_filters()
        df = load_data(city, month, day, filterselect)
        time_stats(df)
        station_stats(df)
        user_stats(df)
        trip_duration_stats(df)
        
        # Read Some Data
        
        read_data = input('\nWould you like to read some of data? Enter yes or no.\n')
        if read_data.lower() == 'yes':
            print(df.head())
        
        # Restart program 
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
