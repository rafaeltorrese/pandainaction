# %% [markdown]
# # Dealing with Duplicates
# Pandas includes several methods to identify duplicate and unique values in a dataset. The duplicated method returns a Boolean Series where a True indicates that a value has previously been encountered (i.e. a duplicate).
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
print(employees['Gender'].unique())
print(employees['Team'].unique())
# %% [markdown]
# ## The **duplicated** method
print(employees['Team'].head())
print(employees['Team'].duplicated().head())
print()
print(employees['Team'])
print()
print(employees['Team'].duplicated())
print()
print(employees['Team'].duplicated(keep='last'))
# %%
print(~(employees['Team'].duplicated()).head())
first_one_in_team = ~employees['Team'].duplicated()
print()
employees[first_one_in_team]

# %% [markdown]
# ## The drop_duplicates Method
print(employees.drop_duplicates())
# %% [markdown]
# Much like with the duplicated method, the **subset** parameter can specify a list of columns whose values will be used to determine a row's uniqueness. 
print(employees.drop_duplicates(subset=['Team']))
print()
print(employees.drop_duplicates(subset=['Team'], keep='last'))
# %% [markdown]
# The **keep** parameter accepts one other argument, False, which will discard all rows that have duplicate values
print(employees.drop_duplicates(subset=['First Name'], keep=False))
# %%
print(employees[['First Name', 'Team', 'Gender']])
print()
finance = employees['Team'] == 'Finance'
is_male = employees['Gender'] == 'Male'
print(employees[finance & is_male])
print()
print(employees.drop_duplicates(subset=['Gender', 'Team']).head())