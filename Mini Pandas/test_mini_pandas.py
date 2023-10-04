import pytest
from mini_pandas import*

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

#-----------------------------------------------------------------------------
#Task 8: Create a small patients table and use it to test both the prep_data and 
#inspect functions. Write separate testing functions for these (called 
#test_prep_data and test_inspect).
small_patients_df = pd.DataFrame({
        'id' : [2, 5, 18, 23],
        'year' :[1999, 2000, 2003, 2021],
        'height': [50, 49, 65, 68],
        'smoker' : ['yes', 'no', 'no', 'yes'],
        'illnesses' : [np.NaN, np.NaN, np.NaN, np.NaN]})

#task 1 test:
def test_inspect():
    '''tests for inspect functionality and bugs'''
    assert inspect(patients) == pd.DataFrame({
        'id': [18, 25, 63, 83, 92, 118, 160, 209, 216],
        'year' : [1996, 1949, 1992, 1965, 1930, 1999, 1956, 1951, 1943],
        'height': [84, 67, 28, 60, 63, 67, 69, 59, 63],
        'smoker' : ['yes', np.NaN, 'no', np.NaN, np.NaN, np.NaN, np.NaN, 
                    np.NaN, np.NaN],
        'illnesses' : [np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, 
                    np.NaN, np.NaN]})

    assert inspect(small_patients_df) == pd.DataFrame({
        'id': [], 
        'year' : [],
        'height': [], 
        'smoker': [], 
        'illnesses' : []})

    ex_df2 = pd.DataFrame({
        'id' : [2, 5, 18, 23],
        'year' :[1999, 2000, 2003, 2021],
        'height': [20, 49, 65, 90],
        'smoker' : ['yes', 'no', 'no', 'yes'],
        'illnesses' : [np.NaN, np.NaN, np.NaN, np.NaN]})
    assert inspect(ex_df2) == pd.DataFrame({
        'id': [2, 23], 
        'year' : [1999, 2021], 
        'height': [20, 90], 
        'smoker': ['yes', 'yes'], 
        'illnesses' : [np.NaN, np.NaN]})

    ex_df3 = pd.DataFrame({
        'id' : [2, 5, 18, 23],
        'year' :[1999, 2000, 2003, 2021],
        'height': [50, 49, 65, 68],
        'smoker' : ['yes', np.NaN, 'no', 'yes'],
        'illnesses' : [np.NaN, np.NaN, np.NaN, np.NaN]})
    assert inspect(ex_df3) == pd.DataFrame({
        'id': [5], 
        'year' : [2000], 
        'height': [49], 
        'smoker': [np.NaN], 
        'illnesses' : [np.NaN]})
    
    ex_df4 = pd.DataFrame({
        'id' : [2, 5, 18, 23],
        'year' :[1999, 2000, 2003, 2021],
        'height': [50, 49, 65, 99],
        'smoker' : ['yes', np.NaN, 'no', 'yes'],
        'illnesses' : [np.NaN, np.NaN, np.NaN, np.NaN]})
    assert inspect(ex_df4) == pd.DataFrame({
        'id': [5, 23], 
        'year' : [2000, 2021], 
        'height': [49, 99], 
        'smoker': [np.NaN, 'yes'], 
        'illnesses' : [np.NaN, np.NaN]})
    
#task 2 tests:
def test_prep_data():
    '''tests for prep_data functionality and bugs'''
    assert prep_data(small_patients_df) == pd.DataFrame({
        'id' : [2, 5, 18, 23],
        'year' :[1999, 2000, 2003, 2021],
        'height': [50, 49, 65, 68],
        'smoker' : [True, False, False, True],
        'illnesses' : [[''], [''], [''], ['']]})
    
    ex_df5 = pd.DataFrame({
        'id' : [2, 5],
        'year' :[1999, 2000],
        'height': [50, 49],
        'smoker' : [np.NaN, np.NaN],
        'illnesses' : [np.NaN, np.NaN]})
    assert prep_data(ex_df5) == pd.DataFrame({
        'id': [2, 5], 
        'year' : [1999, 2000],
        'height': [50, 49], 
        'smoker': [np.NaN, np.NaN], 
        'illnesses' : [[''], ['']]})

    ex_df6 = pd.DataFrame({
        'id' : [2, 5],
        'year' :[1999, 2000],
        'height': [50, 49],
        'smoker' : [np.NaN, np.NaN],
        'illnesses' : [np.NaN, 'high-blood pressure;stroke']})
    assert prep_data(ex_df6) == pd.DataFrame({
        'id': [2, 5], 
        'year' : [1999, 2000], 
        'height': [50, 49], 
        'smoker': [np.NaN, np.NaN], 
        'illnesses' : [[''], ['high-blood pressure', 'stroke']]})
    
    ex_df7 = pd.DataFrame({
        'id' : [2, 5],
        'year' :[1999, 2000],
        'height': [50, 49],
        'smoker' : ['yes', 'no'],
        'illnesses' : [np.NaN, 'high-blood pressure;stroke']})
    assert prep_data(ex_df7) == pd.DataFrame({
        'id': [2, 5], 
        'year' : [1999, 2000], 
        'height': [50, 49], 
        'smoker': [True, False], 
        'illnesses' : [[''], ['high-blood pressure', 'stroke']]})
    
    ex_df8 = pd.DataFrame({
        'id' : [2, 5],
        'year' :[1999, 2000],
        'height': [50, 49],
        'smoker' : ['noo', 'ye s'],
        'illnesses' : [np.NaN, 'high-blood pressure;stroke']})
    assert prep_data(ex_df8) == pd.DataFrame({
        'id': [2, 5], 
        'year' : [1999, 2000], 
        'height': [50, 49], 
        'smoker': ['noo', 'ye s'], 
        'illnesses' : [[''], ['high-blood pressure', 'stroke']]})
    
    ex_df9 = pd.DataFrame({
        'id' : [2, 5],
        'year' :[1999, 2000],
        'height': [50, 49],
        'smoker' : ['noo', 'ye s'],
        'illnesses' : [np.NaN, 'high-blood pressure;stroke']})
    assert prep_data(ex_df9) == pd.DataFrame({
        'id': [2, 5], 
        'year' : [1999, 2000],
        'height': [50, 49], 
        'smoker': ['noo', 'ye s'], 
        'illnesses' : [[''], ['high-blood pressure', 'stroke']]})

    
#-----------------------------------------------------------------------------
#I know task 3 and 4 techinclly don't have outputs, but if they did, this is what
#the dataframs would look like 

#task 3 tests:
def test_record_illness():
    '''Tests for the THEORETICAL output of record_illness. The actual function 
    has no output'''
    ex_df10 = pd.DataFrame({
        'id' : [2, 5],
        'year' :[1999, 2000],
        'height': [50, 49],
        'smoker' : ['no', 'yes'],
        'illnesses' : [np.NaN, 'high-blood pressure;stroke']})
    assert record_illness(ex_df10, 2, 'stroke') == pd.DataFrame({
        'id': [2, 5], 
        'year' : [1999, 2000], 
        'height': [50, 49], 
        'smoker': ['no', 'yes'], 
        'illnesses' : [['stroke'], ['high-blood pressure', 'stroke']]})

    ex_df11 = pd.DataFrame({
        'id' : [2, 5],
        'year' :[1999, 2000],
        'height': [50, 49],
        'smoker' : ['no', 'yes'],
        'illnesses' : [np.NaN, 'high-blood pressure;stroke']})
    assert record_illness(ex_df11, 6, 'stroke') == pd.DataFrame({
        'id': [2, 5], 
        'year' : [1999, 2000], 
        'height': [50, 49], 
        'smoker': ['no', 'yes'], 
        'illnesses' : [[''], ['high-blood pressure', 'stroke']]})
    
    ex_df12 = pd.DataFrame({
        'id' : [2, 5],
        'year' :[1999, 2000],
        'height': [50, 49],
        'smoker' : ['no', 'yes'],
        'illnesses' : [np.NaN, 'high-blood pressure;stroke']})
    assert record_illness(ex_df12, 5, 'flu') == pd.DataFrame({
        'id': [2, 5], 
        'year' : [1999, 2000], 
        'height': [50, 49], 
        'smoker': ['no', 'yes'], 
        'illnesses' : [[''], ['high-blood pressure', 'stroke', 'flu']]})
    

#-----------------------------------------------------------------------------
#Task 9: Create a small visits table and use it to generate analysis plots with 
#the plotting functions in part 4 (so you can visually check that they work).

small_visits_df = pd.DataFrame({
        'id': [17, 22, 33, 43],
        'when': [pd.Timestamp('2022-10-22 10:15:00'), 
                 pd.Timestamp('2003-09-16 8:45:00'), 
                 pd.Timestamp('1999-01-18 2:27:00'), 
                 pd.Timestamp('2021-05-13 16:00:10')],
        'clinic': ['Oakdale', 'Beaumont', 'Oakdale', 'Healthbridge'],
        'weight': [155, 120, 230, 94],
        'heartrate': [91, 123, 101, 134]})

#task 4 tests:
#I know task 3 and 4 techinclly don't have outputs, but if they did, this is what
#the dataframes would look like 
def test_new_visit():
    '''Tests for the THEORETICAL output of new_visit. The actual function 
    has no output'''
    assert new_visit(small_visits_df, 4, pd.Timestamp('2023-04-26 10:30:00'), 
            'Beaumont', 134, 99) == pd.DataFrame({
        'id': [17, 22, 33, 43, 4],
        'when': [pd.Timestamp('2022-10-22 10:15:00'), 
                 pd.Timestamp('2003-09-16 8:45:00'), 
                 pd.Timestamp('1999-01-18 2:27:00'), 
                 pd.Timestamp('2021-05-13 16:00:10'),
                 pd.Timestamp('2023-04-26 10:30:00')],
        'clinic': ['Oakdale', 'Beaumont', 'Oakdale', 'Healthbridge', 'Beaumont'],
        'weight': [155, 120, 230, 94, 134],
        'heartrate': [91, 123, 101, 134, 99]})
    
    assert new_visit(small_visits_df, 4.0 , pd.Timestamp('2023-04-26 10:30:00'), 
            'Beaumont', 134, 99) == pd.DataFrame({
        'id': [17, 22, 33, 43, 4.0],
        'when': [pd.Timestamp('2022-10-22 10:15:00'), 
                 pd.Timestamp('2003-09-16 8:45:00'), 
                 pd.Timestamp('1999-01-18 2:27:00'), 
                 pd.Timestamp('2021-05-13 16:00:10'),
                 pd.Timestamp('2023-04-26 10:30:00')],
        'clinic': ['Oakdale', 'Beaumont', 'Oakdale', 'Healthbridge', 'Beaumont'],
        'weight': [155, 120, 230, 94, 134],
        'heartrate': [91, 123, 101, 134, 99]})
    
    assert new_visit(small_visits_df, 12, pd.Timestamp('2022-10-22 10:15:00'), 
            'Beaumont', 134, 99) == pd.DataFrame({
        'id': [17, 22, 33, 43, 12],
        'when': [pd.Timestamp('2022-10-22 10:15:00'), 
                 pd.Timestamp('2003-09-16 8:45:00'), 
                 pd.Timestamp('1999-01-18 2:27:00'), 
                 pd.Timestamp('2021-05-13 16:00:10'),
                 pd.Timestamp('2022-10-22 10:15:00')],
        'clinic': ['Oakdale', 'Beaumont', 'Oakdale', 'Healthbridge', 'Beaumont'],
        'weight': [155, 120, 230, 94, 134],
        'heartrate': [91, 123, 101, 134, 99]})
    
    assert new_visit(small_visits_df, 43, pd.Timestamp('2023-04-26 10:30:00'), 
            'Beaumont', 134, 99) == pd.DataFrame({
        'id': [17, 22, 33, 43, 43],
        'when': [pd.Timestamp('2022-10-22 10:15:00'), 
                 pd.Timestamp('2003-09-16 8:45:00'), 
                 pd.Timestamp('1999-01-18 2:27:00'), 
                 pd.Timestamp('2021-05-13 16:00:10'),
                 pd.Timestamp('2023-04-26 10:30:00')],
        'clinic': ['Oakdale', 'Beaumont', 'Oakdale', 'Healthbridge', 'Beaumont'],
        'weight': [155, 120, 230, 94, 134],
        'heartrate': [91, 123, 101, 134, 99]})
    

#task 5 tests:
def test_plot_weight_heart_data():
    '''outputs a plot based off of the small dataframe created to check 
    functionality'''
    plot_weight_heart_data(small_visits_df)

#task 6 tests:
def test_plot_visits_per_month():
    '''outputs a plot based off of the small dataframe created to check 
    functionality'''
    plot_visits_per_month(small_visits_df)

#task 7 tests:
def test_visits_per_clinic():
    '''outputs a plot based off of the small dataframe created to check 
    functionality'''
    visits_per_clinic(small_visits_df)


