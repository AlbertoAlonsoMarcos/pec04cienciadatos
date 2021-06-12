
def transform_datasets():
    '''
    The main objective for this function is to read, transform and save two datasets
    from the three original resources. One of those is a xlsx file that required openpyxl module

    Args:
        None

    Returns:
        :obj:`str`: inform user it has been completed
        :obj:`file`: save two new datasets from originals
    '''
if __name__ == "__main__":

    import pandas as pd
    import openpyxl

    approval = pd.read_csv('../data/covid_approval_polls.csv')
    concern = pd.read_csv('../data/covid_concern_polls.csv')
    ratings = pd.read_excel('../data/pollster_ratings.xlsx', engine = 'openpyxl')
    ratings.rename(columns={'Pollster':'pollster'}, inplace=True)

    # We have to follow request made in Exercis 2
    # Excluse approval polls without rating joining both
    # Filter using tracking column value like False and Banned by 538 like no
    approvals = pd.merge(approval, ratings, on='pollster')
    approvals = approvals[approvals['tracking']==False]
    approvals = approvals[approvals['Banned by 538']=='no']

    approvals.to_csv('../data/exercise_three.csv')

    # We have to follow request made in Exercis 2
    # Excluse approval polls without rating joining both
    # Filter using tracking column value like False and Banned by 538 like no
    concerns = pd.merge(concern, ratings, on='pollster')
    concerns = concerns[concerns['tracking']==False]
    concerns = concerns[concerns['Banned by 538']=='no']

    concerns.to_csv('../data/exercise_four.csv')

    print('Datasets have been transformed')










