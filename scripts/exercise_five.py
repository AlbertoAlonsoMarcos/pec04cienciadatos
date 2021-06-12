def evolution():
    '''
    This function implement all the Exercise 5 aparts

    There are a lot of pandas transformations made, and those are commented below 

    Args:
        None

    Returns:
        :obj:`srt`: exercise results
        :obj:`charts`: two bar chars to compare between before and after 2020-09-01 
    '''
if __name__ == "__main__":

    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    concerns = pd.read_csv('../data/exercise_four.csv')

    # Ejercicio 4.5.1
    # Creating Point and replace default value (0) based on Grade, following exercise rules
    concerns['Points'] = 0
    concerns.loc[(concerns['538 Grade']=='A'), 'Points'] = 1
    concerns.loc[(concerns['538 Grade']=='B'), 'Points'] = 0.5
    concerns.loc[(concerns['538 Grade']=='C'), 'Points'] = 0
    concerns.loc[(concerns['538 Grade']=='D'), 'Points'] = -0.5
    concerns.loc[(concerns['538 Grade']=='F'), 'Points'] = -1


    # Create a new column adding Points + Predictive values
    concerns['puntuacion']= concerns['Points'] + concerns['Predictive    Plus-Minus']

    # Filtering by puntuacion >= 1.5
    high = concerns[concerns['puntuacion']>=1.5]

    # Creating new dataset from high only with end_date, sample_size, a corcern percentage for each classification column
    highest = high[['end_date', 'sample_size', 'very', 'somewhat', 'not_very', 'not_at_all']]
    highest['total_very'] = highest['sample_size'] * highest['very'] / 100
    highest['total_somewhat'] = highest['sample_size'] * highest['somewhat'] / 100
    highest['total_not_very'] = highest['sample_size'] * highest['not_very'] / 100
    highest['total_not_at_all'] = highest['sample_size'] * highest['not_at_all'] / 100


    # Split based on date '2020-09-01', before date
    date_before = highest[highest['end_date']<'2020-09-01']

    # Preparing variables with summatory    
    very_date_before = date_before['total_very'].sum()
    somewhat_date_before = date_before['somewhat'].sum() 
    not_very_date_before = date_before['not_very'].sum()
    not_at_all_date_before = date_before['not_at_all'].sum()
    total_date_before = very_date_before + somewhat_date_before + not_very_date_before + not_at_all_date_before

    # Calculate percentages using total_date_before 
    p_very_date_before = very_date_before / total_date_before
    p_somewhat_date_before = somewhat_date_before/ total_date_before
    p_not_very_date_before = not_very_date_before / total_date_before
    p_not_at_all_date_before = not_at_all_date_before / total_date_before

    # Split based on date '2020-09-01', after date
    date_after = highest[highest['end_date']>='2020-09-01']

    # Preparing variables with summatory    
    very_date_after = date_after['total_very'].sum()
    somewhat_date_after = date_after['somewhat'].sum()
    not_very_date_after = date_after['not_very'].sum()
    not_at_all_date_after = date_after['not_at_all'].sum()
    total_date_after = very_date_after + somewhat_date_after + not_very_date_after + not_at_all_date_after

    # Calculate percentages using total_date_after 
    p_very_date_after = very_date_after / total_date_after
    p_somewhat_date_after = somewhat_date_after / total_date_after
    p_not_very_date_after = not_very_date_after / total_date_after
    p_not_at_all_date_after = not_at_all_date_after / total_date_after

    # Graphic 4.5.1
    before = [very_date_before, somewhat_date_before, not_very_date_before, not_at_all_date_before]
    after = [very_date_after, somewhat_date_after, not_very_date_after, not_at_all_date_after]
    indice_barras = np.arange(4)
    ancho_barras = 0.35

    plt.bar(indice_barras, before, width=ancho_barras, label='before 2020-09-01')
    plt.bar(indice_barras + ancho_barras, after, width=ancho_barras, label='after 2020-09-01')
    plt.xticks(indice_barras + ancho_barras, ('very', 'somewhat', 'not very', 'not at all'))
    plt.ylabel('Total')
    plt.xlabel('Concern')
    plt.title('Concern evolution by totals')
    plt.legend(loc='best')
    plt.show()

    # Graphic 4.5.2
    p_before = [p_very_date_before, p_somewhat_date_before, p_not_very_date_before, p_not_at_all_date_before]
    p_after = [p_very_date_after, p_somewhat_date_after, p_not_very_date_after, p_not_at_all_date_after]

    plt.bar(indice_barras, p_before, width=ancho_barras, label='before 2020-09-01')
    plt.bar(indice_barras + ancho_barras, p_after, width=ancho_barras, label='after 2020-09-01')
    plt.xticks(indice_barras + ancho_barras, ('very', 'somewhat', 'not very', 'not at all'))
    plt.ylabel('Percentage')
    plt.xlabel('Concern')
    plt.title('Concern evolution by percentage')
    plt.legend(loc='best')
    plt.show()