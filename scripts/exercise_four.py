
def multi_results():
    '''
    This function implement all the Exercise 4 aparts

    There are a lot of pandas transformations made, and those are commented below 

    Args:
        None

    Returns:
        :obj:`srt`: exercise results
        :obj:`charts`: for all except 4.1
    '''
if __name__ == "__main__":

    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    concerns = pd.read_csv('../data/exercise_four.csv')

    print('Ejercicio 4.1, el total de personas encuestadas es:', f"{concerns['sample_size'].sum():,}")

    # Modifiying Grade following xercise comments
    concerns.loc[(concerns['538 Grade']=='B/C'), '538 Grade'] = 'B'
    concerns.loc[(concerns['538 Grade']=='B+'), '538 Grade'] = 'B'
    concerns.loc[(concerns['538 Grade']=='B-'), '538 Grade'] = 'B'
    concerns.loc[(concerns['538 Grade']=='C-'), '538 Grade'] = 'C'
    concerns.loc[(concerns['538 Grade']=='D-'), '538 Grade'] = 'D'

    # Filtering by subject = 'concern-economy'
    economy = concerns[concerns['subject']=='concern-economy']

    # Creating a subset of concerns
    economy = economy[['538 Grade', 'sample_size', 'very', 'not_at_all']]

    # Create two new columns to load total people from ecah percentage and sample_size
    economy['total_very'] = economy['sample_size'] * economy['very'] / 100
    economy['not_at_all'] = economy['sample_size'] * economy['not_at_all'] / 100

    # asigned values to variables to be reused
    very = economy['total_very'].sum()
    not_at_all = economy['not_at_all'].sum()

    # Printing resolution for Exercise 4.2
    print('Ejercicio 4.2 el total de muy preocupados es:',  f"{very:,}"
            ,'mientras que el de nada preocupados es:',  f"{not_at_all:,}")

    labels = 'Very', 'Not at all'
    sizes = [very, not_at_all]

    # Creating a pie chart for Exercise 4.3
    fig1, axis1 = plt.subplots()
    axis1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    axis1.axis('equal')
    plt.title('Economy concern')
    plt.show()

    # Filtering by subject = 'concern-infected'
    infected = concerns[concerns['subject']=='concern-infected']

    # Creating a subset of concerns
    infected = infected[['538 Grade', 'sample_size', 'very', 'not_at_all']]

    # Create two new columns to load total people from ecah percentage and sample_size
    infected['total_very'] = infected['sample_size'] * infected['very'] / 100
    infected['not_at_all'] = infected['sample_size'] * infected['not_at_all'] / 100

    # asigned values to variables to be reused
    total_infected = infected['sample_size'].sum()
    very_infected = infected['total_very'].sum() * 100 / total_infected
    not_at_all_infected = infected['not_at_all'].sum() * 100 / total_infected

    # Printing resolution for Exercise 4.3
    print('Ejercicio 4.3 el porcentaje de muy preocupados es:',  f"{very_infected:,}"
            ,'mientras que el de nada preocupados es:',  f"{not_at_all_infected:,}")

    labels_infected = 'Very', 'Not at all'
    sizes_infected = [very_infected, not_at_all_infected]

    # Creating a pie chart for Exercise 4.3
    fig1, axis1 = plt.subplots()
    axis1.pie(sizes_infected, labels=labels_infected, shadow=True, startangle=90)
    axis1.axis('equal')
    plt.title('Infected concern')
    plt.show()

    # Ejercicio 4.4
    grade = concerns[['538 Grade', 'sample_size']]

    # Considero que se refiere en el texto al número de entrevistas, no a la muestra representada por sample_size
    grades = grade.groupby(['538 Grade']).agg({'sample_size':'count'}).reset_index()

    labels_grades = grades['538 Grade'].tolist()
    sizes_grades = grades['sample_size'].tolist()

    print(grades)

    # Creating a pie chart for Exercise 4.4
    fig1, axis1 = plt.subplots()
    axis1.pie(sizes_grades, labels=labels_grades, autopct='%1.1f%%', shadow=True, startangle=90)
    axis1.axis('equal')
    plt.title('Grades concern')
    plt.show()


    