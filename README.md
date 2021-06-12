# pec04cienciadatos
Repository for UOC PEC 04 for Data Science Programming

GitHub Link: https://github.com/AlbertoAlonsoMarcos/pec04cienciadatos/tree/develop

In this repo we will develop a solutions for PEC04 Exercise

In scripts folder you can figure out four programms, exercise_one.py, exercise_two.py, exercise_three.py and exercise_four.py

You need to run it in order: one, two, three and finally four

**Exercise On**

Exercise_one.py is a Python function that implement a iteration within a dataset located in data folder named covid_approval_polls.csv
When you execute this functions, the program read each dataset line trying to match two different patterns:

1. First pattern is for Huffington Post string
2. Second pattern is for url that contain http or https and finalize with .pdf

The output of this funtion is the total count of matches for this two patterns

For exercise_one.py execution, you need to open Terminal and write py exercise_one.py

**Exercise Two**

Exercise_two.py is a Python function for transforming and preparaing two new datasets.

Main transformations made:
1. Excluse approval polls without rating joining both approval and rating
2. Filter using tracking column value like False and Banned by 538 like no

3. Excluse approval polls without rating joining both concern and rating
4. Filter using tracking column value like False and Banned by 538 like no

Finally the function save these two datasets

For exercise_two.py execution, you need to open Terminal and write py exercise_two.py

**Exercise three**

Exercise_three.py is a Python function that read a previous dataset that has been transformed and persisted in exercise_two.py

After the load, this function pick up only rows filtering it thanks to text columns based on if contains Trump and coronavirus or not
Finally aggregate the dataset grouping by party and sum values and present it through two pie charts
One for approve and another one for disapprove

For exercise_three.py execution, you need to open Terminal and write py exercise_three.py

**Exercise four**

Exercise_four.py is a Python function that execute a lot of pandas process for transforming data into information that has been presented in many different charts except for 4.1

In 4.2 and 4.3 there are two pie charts one for economic concern and another one for infected concern
In both we compare very and not at all concerned people

In 4.4 we present the total number of interviews aggregated by grade in a pie chart

For exercise_four.py execution, you need to open Terminal and write py exercise_four.py

**Exercise five**

Exercise_five.py is a Python function that xecute a lot of transformations from initial exercise 4 dataset

The main transformations made:
1. Create a new columns for punctuation
2. Used this new column for filtering dataset with the condition of higher than 1.5
3. After the function eleborate several calculations and store it in variables and finally present all those in a bar chart also filtring by data '2020-09-01', and comparing the evolution of people concern

For exercise_five.py execution, you need to open Terminal and write py exercise_five.py


