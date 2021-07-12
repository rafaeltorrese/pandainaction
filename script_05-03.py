# %% [markdown]
# # Filtering by Multiple Conditions
# %%  
import pandas as pd
# %%
employees = pd.read_csv('data/employees.csv', parse_dates=['Start Date'])
employees['Mgmt'] = employees['Mgmt'].astype(bool)
employees['Salary'] = employees['Salary'].fillna(0).astype(int)
employees['Gender'] = employees['Gender'].astype('category')
employees['Team'] = employees['Team'].astype('category')

# %%
print(employees.columns)
print(employees["Gender"].unique())
print(employees['Team'].unique())
# %% [markdown]
# ## The AND Condition

is_female = employees['Gender'] == 'Female'
print(is_female.head())
in_biz_dev = employees['Team'] == 'Business Dev'
print(in_biz_dev.head())
# %% [markdown]
# we need to calculate the intersection of the two Series, the rows in which both of them have a value of True. Pass both of the Series into the square brackets and place an ampersand __(&)__ symbol in between them
print(employees[is_female & in_biz_dev].head())


# %% [markdown]
# We can pass as many Series in the square brackets as we want as long as we separate every subsequent two with a **&** symbol
print(employees.columns)
is_manager = employees['Mgmt']
print(employees[is_female & in_biz_dev & is_manager].head())
# %% [markdown]
# ## The OR Condition
earning_below_40k = employees['Salary'] < 40000
started_after_2015 = employees['Start Date'] > "2015-01-01"
# %% [markdown]
# To specify an OR criteria, use a pipe symbol **( | )**. In the next example, a row will be selected if either of the Boolean Series at that index position holds a True
print(employees[earning_below_40k | started_after_2015].tail())
# %% [markdown] 
# ## Inversion with **~**
# The tilde symbol ( ~ ) inverts the values in a Series of Booleans. All True values become False, and all *False* values become *True*. 
my_series = pd.Series([True, False, True])
print(my_series)
print()
print(~my_series)
# %%
print(employees[employees['Salary'] < 100000].head())
print()
print(employees[~(employees['Salary'] >= 100000)].head())