# %%
import pandas as pd
# %%
# print(pd.read_csv('data/employees.csv'))
# print(pd.read_csv('data/employees.csv', parse_dates=['Start Date']))
employees = pd.read_csv('data/employees.csv', parse_dates=['Start Date'])
# %%
print(employees.info())

# %% [markdown]
## Hello
# Documentation 
employees.describe()


# %%
