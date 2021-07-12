# %%
import pandas as pd
# %%
print(pd.read_csv('data/employees.csv'))
# print(pd.read_csv('data/employees.csv', parse_dates=['Start Date']))
# %%
employees = pd.read_csv('data/employees.csv', parse_dates=['Start Date'])
print(employees.info())
# %%
employees["Mgmt"].astype(bool)
# %%
employees["Mgmt"] = employees['Mgmt'].astype(bool)
print(employees.info())
# %%
print(employees['Salary'].tail())

# %%
print(employees['Salary'].fillna(0).tail())
# %%
print(employees['Salary'].fillna(0).astype(int).head())
employees['Salary'] = employees['Salary'].fillna(0).astype(int)
print(employees['Salary']) 
# %% [markdown]
# The *nunique* method can tell us the number of unique values in each column of a DataFrame.
employees.nunique()
# %%
employees['Gender'] = employees['Gender'].astype('category')
print(employees['Gender'])
print(employees.info())
# %% [markdown]
# Let's repeat the same process for the **Team** column. There are only ten unique values among 1001 rows
employees['Team'] = employees['Team'].astype('category')
print(employees['Team'])
print(employees.info())
# %%
