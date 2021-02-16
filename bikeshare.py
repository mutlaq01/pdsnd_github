import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters(city, month, day):
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hi! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city of the three do you want the data for? Chicago, New York City or Washington. \n").lower().strip()
        if city not in CITY_DATA:
            print("\nInvalid answer! Please, check your spilling and try again.\n")
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        time = input("You have 4 options: Do you want to filter by month, day, all or none. \n").lower().strip()
        if time == 'month':
            while True:
                month = input("Which month? January, Feburary, March, April, May or June. \n").lower().strip()
                if month not in months:
                    print("\nInvalid answer! Please, check your spilling and try again.\n")
                else:
                    break
            day = 'all'
            break

        elif time == 'day':
            month = 'all'
            while True:
                day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday. \n").lower().strip()
                if day not in days:
                    print("\nInvalid answer! Please, check your spilling and try again.\n")
                else:
                    break
            break

        elif time == 'all':
            while True:
                month = input("Which month? January, Feburary, March, April, May or June. \n").lower().strip()
                if month not in months:
                    print("\nInvalid answer! Please, check your spilling and try again.\n")
                else:
                    break
            while True:
                day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday. \n").lower().strip()
                if day not in days:
                    print("\nInvalid answer! Please, check your spilling and try again.\n")
                else:
                    break
            break
        elif time == 'none':
            month = 'all'
            day = 'all'
            break
        else:
            input("Invalid answer! Please, check your spilling and try again.")
            break

    print(city)
    print(month)
    print(day)
    print('-'*40)
    return city, month, day



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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
        df = df[df['month'] == month]


    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()



    # display the most common month
    common_month = df['month'].mode()[0]
    print(common_month)


    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print(common_day_of_week)


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print(most_common_start)


    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print(most_common_end)


    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    most_common_combination = df['combination'].mode()[0]
    print(most_common_combination)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)


    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("No Information!")


    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth_Year' in df:
        earliest = df['Birth_Year'].min()
        print(earliest)
        recent = df['Birth_Year'].max()
        print(most_recent)
        common_birth = df['Birth Year'].mode()[0]
        print(most_common)
    else:
        print("No Information!")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def rdata(df):
    """displays raw data if the used wants to the data as it is stored """
    raw_data = 0
    # Asking if user wants to see raw data
    while True:
        answer = input("Do you want to see new/more raw data? Enter Yes or No. \n").lower().strip()
        if answer not in ['yes', 'no']:
            answer = input("Invalid answer. Please type Yes or No. \n").lower().strip()
        elif answer == 'yes':
            raw_data += 5
            print(df.iloc[raw_data : raw_data + 5])
        elif answer == 'no':
            return




def main():
    city = ""
    month = ""
    day = ""
    while True:
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        rdata(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
