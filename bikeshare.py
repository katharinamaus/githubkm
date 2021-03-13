# I used the following links for this project:
# https://pandas.pydata.org/pandas-docs/version/0.17.1/generated/pandas.DataFrame.mode.html
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
# https://stackoverflow.com/questions/43983622/remove-unnamed-columns-in-pandas-dataframe
# https://stackoverflow.com/questions/20490274/how-to-reset-index-in-a-pandas-dataframe
# https://stackoverflow.com/questions/50848454/pulling-most-frequent-combination-from-csv-columns


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

time_choice_list = ['month', 'day', 'no timeframe']
month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']


print('-'*40)


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs 
    while True: 
        city = input('Would you like to see "Chicago", "New York City" or "Washington"? Please state the corresponding city "Chicago", "New York City", or "Washington". \n').lower()
        if city not in CITY_DATA:
            print('Your answer does not correspond to the indicated cities: "Chicago", "New York City" or "Washington". Please enter one of the stated city names.')
            continue
        else:
            print('Thank you. We will have a look on the data for the city {}.'.format(city.title()))
            break

# TO DO: get user input for timeframe filter preference - by month, by day or not at all    
    while True:
        time_choice = input('Would you like to set a timeframe filter - by month, by day, or not at all? Please state "month", "day", or "no timeframe".\n').lower()
        if time_choice not in time_choice_list:
            print('Your answer does not correspond to one of the stated options: "month", "day" or "no timeframe". Please state one of the indicated values.')
            continue
        elif time_choice == 'no timeframe':
            month = 'all'
            day = 'all'
            print('There will be no timeframe filter.')
            break
        else:
            print('The data will be filtered by {}.'.format(time_choice))
            break

      
    # TO DO: get user input for month (all, january, february, ... , june)   
    if time_choice == 'month':
        while True:
            month = input('Which month? Please state "January", "February", "March", "April", "May", or "June".\n').lower()
            if month not in month_list:
                print('Your answer does not correspond to one of the indicates months: "January", "February", "March", "April", "May", or "June". Please state one of the indicated months.')
                continue
            else:
                day = 'all'
                print('The data will be filtered by day ({}).'.format(day.title()))
                break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if time_choice == 'day':
        while True:
            day = input('Which day? Please state "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", or "Sunday".\n').lower()
            if day not in day_list:
                print('Your answer does not correspond to one of the indicated days: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", or "Sunday". Please state one of the indicated days.')
                continue
            else:
                month = 'all'
                print('The data will be filtered by day ({}).'.format(day.title()))
                break            


    print('-'*40)
    print('Filter:\n', 'City:', city.title(), '\n Month:', month.title(), '\n Day:', day.title())
    return city, month, day
                                
    print('Here are the data:')
                  

            
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
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime            
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    # extract weekday from Start Time to create new columns
    df['day_of_week'] = df['Start Time'].dt.weekday_name     
    
    # filter by month if applicable
    if month != 'all': 
        # use the index of the months list to get the corresponding int
        month_index = month_list.index(month)+1
        #filter by month to create the new dataframe
        df = df[df['month'] == month_index]
        

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df



           
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month 
    month_index = df['month'].mode()[0]-1
    most_common_month = month_list[month_index].title()
    print('Most common month:', most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('Most common day of the week:', most_common_day_of_week)

    # extract hour from Start Time to create new column
    df['hour'] = df['Start Time'].dt.hour
    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print('Most common start hour:', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print(' ')

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station:', most_commonly_used_start_station)
            
    # TO DO: display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station:', most_commonly_used_end_station)
            
    # TO DO: display most frequent combination of start station and end station trip
    most_commonly_used_start_end_station = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print('Most commonly used combination of start and end station:\n', most_commonly_used_start_end_station)
            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print(' ')

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time amounts to:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time amounts to:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print(' ')                        


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types = df['User Type'].value_counts()
    print('The total count of user type is:\n', counts_user_types)

    # TO DO: Display counts of gender
    if city == 'washington':
        print('There are no gender data for Washington.')    
    else:
        counts_gender = df['Gender'].value_counts()
        print('The count of gender amounts to:\n', counts_gender)   

    # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'washington':
        print('There are no year of birth data available for Washington.')      
    else:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].value_counts().idxmax()
        print('The earliest year of birth is: {}'.format(int(earliest_birth_year)))
        print('The most recent year of birth is: {}'.format(int(most_recent_birth_year)))
        print('The most common year of birth is: {}'.format(int(most_common_birth_year)))
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print(' ')

def display_raw_data(df):      
    """Displays raw data at the request of the user."""
    
    count_lines = 5

    while True:
        display_raw_data = input('Do you want to see 5 lines of raw data? Enter "yes" or "no".\n').lower()
        if display_raw_data not in ['yes','no']:
            print('{} is no valid input.'.format(display_raw_data))
            continue
        elif display_raw_data == 'yes':
            print(df.head(count_lines).drop('Unnamed: 0', axis = 1).reset_index(drop = True))
            count_lines += 5
            break
        else: 
            break
    
    if display_raw_data == 'yes':
        while True: 
            more_raw_data = input('Do you want to see 5 more lines? Enter "yes" or "no".\n').lower()  
            if more_raw_data not in ['yes','no']:
                print('{} is no valid input.'.format(more_raw_data))
                continue
            elif more_raw_data == 'yes':
                print(df.head(count_lines).drop('Unnamed: 0', axis = 1).reset_index(drop = True))
                count_lines += 5
                continue
            else:
                break
    
    print('-'*40)
    print(' ')                        
                            
                            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)        
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
                            
        display_raw_data(df)                    

        restart = input('\nWould you like to restart? Enter "yes" or "no".\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
