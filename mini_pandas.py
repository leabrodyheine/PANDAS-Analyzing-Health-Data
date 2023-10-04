import pandas as pd

# imports for plotting
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# URLs of the three datasets
patients_url = "https://brown-csci0111.github.io/assets/projects/mini-project/patients.csv"
visits_url = "https://brown-csci0111.github.io/assets/projects/mini-project/visits.csv"
bmi_url = "https://brown-csci0111.github.io/assets/projects/mini-project/bmi.csv"

# load the patient data 
patients = pd.read_csv(patients_url, header=0, names=["id","year","height",
                                                      "smoker","illnesses"])
visits = pd.read_csv(visits_url, header=0, names=['id', 'when', 'clinic', 
                                'weight', 'heartrate'], parse_dates=['when'])
BMI_table = pd.read_csv(bmi_url, header=0, names=["height","weight_low",
                                                  "weight_high","category"])


#PART 1
# Task 1:
def inspect(df : pd.DataFrame) -> pd.DataFrame:
    '''returns a patient dataframe with suspicious rows'''
    mask_1 = (df['height'] > 78) | (df['height'] < 36)
    mask_2 = df['smoker'].isnull()
    return df[mask_1 | mask_2] 


#Task 2:
def prep_data(df : pd.DataFrame):
    '''returns modified data where illnesses are a list and smoker is a bool'''
    NaN_mask = df['illnesses'].isnull()
    df.loc[NaN_mask, 'illnesses'] = ''
    df['illnesses'] = df['illnesses'].astype('str')
    df['illnesses'] = df['illnesses'].str.split(';')

    df['smoker'] = df['smoker'].str.lower()
    df.loc[(df['smoker'] == 'yes'), 'smoker'] = True
    df.loc[(df['smoker'] == 'no'), 'smoker'] = False

prep_data(patients)


#PART 2
#Task 3:
def record_illness(df : pd.DataFrame, p_id : int, illness : str):
    '''adds an illness to the patients current list'''
    id_match = df['id'] == p_id
    df.loc[id_match, 'illnesses'].iloc[0].append(illness)

#Task 4:
def new_visit(visits_df : pd.DataFrame, id_num : int, when : pd.to_datetime, 
              clinic : str, weight : int, heartrate : int):
    '''stores a new visit in the dataframe'''
    len_of_df = len(visits_df)
    series_visits = [id_num, when, clinic, weight, heartrate]
    visits_df.loc[len_of_df] = series_visits


#Part 3
#Task 5:
def plot_weight_heart_data(df : pd.DataFrame) -> None:
    '''produces a scatter plot comparing weight and heart rate of each patient and
    raises an error if the column names are not found'''
    if ('heartrate' in df.columns) and ('weight' in df.columns):
        df.plot.scatter(x = 'heartrate', y = 'weight')
        plt.title('heartrate vs weight')
        plt.show()
    else:
        raise ValueError("col not found") 

#Task 6:
def plot_visits_per_month(visits_df2 : pd.DataFrame) -> None:
    '''shows the visits made per month within the dataframe'''
    month_sort = visits_df2['when'].dt.month
    per_month_count = visits_df2.groupby(month_sort)['when'].count()
    per_month_count.plot.line()
    plt.xlabel('month')
    plt.ylabel('num visits')

#Task 7:
def visits_per_clinic(visits_df3 : pd.DataFrame) -> None:
   '''produces a plot of visits from each clinic over time in months'''
   plot_visits_per_month(visits_df3[visits_df3['clinic'] == 'Beaumont'])
   plot_visits_per_month(visits_df3[visits_df3['clinic'] == 'Healthbridge'])
   plot_visits_per_month(visits_df3[visits_df3['clinic'] == 'Oakdale'])
   plt.show()