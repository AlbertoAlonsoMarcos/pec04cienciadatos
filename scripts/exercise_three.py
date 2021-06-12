
def results_by_party():
    '''
    This function read a previous dataset transformed and persisted from exercise_two.py
    Pick up only rows which text contains Trump and coronavirus
    Finally aggregate by party sum values and present it through pie charts
    One for approve and another one for disapprove

    Args:
        None

    Returns:
        :obj:`pie chart`: provide two pie charts as a result of the function execution
    '''
if __name__ == "__main__":

    import matplotlib.pyplot as plt
    import pandas as pd

    approvals = pd.read_csv('../data/exercise_three.csv')

     # Filter all rows tiwh Trump and coronavirus in there
    approvals = approvals[approvals['text'].str.contains('Trump || coronavirus')]

    exercise_three = pd.DataFrame(approvals[['party', 'approve', 'disapprove']])
    values = exercise_three.groupby(['party']).agg({'approve':'sum', 'disapprove':'sum'}).reset_index()

    x_values = values['party'].tolist()
    y_approve = values['approve'].tolist()
    y_disapprove = values['disapprove'].tolist()

    plt.bar(x_values, y_approve)
    plt.title('Approve by Party')
    plt.show()

    plt.bar(x_values, y_disapprove)
    plt.title('Disapprove by Party')
    plt.show()