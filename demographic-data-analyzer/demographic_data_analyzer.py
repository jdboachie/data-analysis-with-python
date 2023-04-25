import numpy as np
import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("demographic-data-analyzer\\adult.data.csv")

    # How many of each race are represented in this dataset?
    # This should be a Pandas series with race names as the index labels.
    race_count = df.race.value_counts()

    # What is the average age of men?
    average_age_men = round(np.mean(df.age[df.sex == 'Male']), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(
        (df[df.education == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    advanced_education = df[df.education.isin(
        ['Bachelors', 'Masters', 'Doctorate'])]
    big_earners = advanced_education[df.salary == '>50K'].shape[0]
    higher_education_rich = round(
        (big_earners / advanced_education.shape[0]) * 100, 1)

    lower_education = df[~df.education.isin(
        ['Bachelors', 'Masters', 'Doctorate'])]
    low_ed_big_earn = lower_education[df.salary == '>50K']
    lower_education_rich = round(
        (low_ed_big_earn.shape[0] / (df.shape[0] - advanced_education.shape[0])) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = np.min(df['hours-per-week'])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    big_earners = df[(df['hours-per-week'] == min_work_hours)
                     & (df.salary == '>50K')].shape[0]
    rich_percentage = (
        big_earners / df[df['hours-per-week'] == min_work_hours].shape[0]) * 100

    # What country has the highest percentage of people that earn >50K?
    q2 = df['salary'] == '>50K'
    p = (df[q2]['native-country'].value_counts() / df['native-country'].value_counts() * 100).sort_values(ascending=False)
    highest_earning_country = p.index[0]
    highest_earning_country_percentage = round(p.iloc[0], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df.salary ==
                                                                '>50K')]['occupation'].value_counts().sort_index().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
