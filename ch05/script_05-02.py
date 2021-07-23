# %% [markdown]
# # Filtering by a Single Condition
# A subset is a dataset that consists of some or all of the rows of another dataset
# %%
print("Maria" == "Maria")
# %% 
import pandas as pd
# %%
employees = pd.read_csv('data/employees.csv', parse_dates=['Start Date'])
employees["Mgmt"] = employees['Mgmt'].astype(bool)
employees['Salary'] = employees['Salary'].fillna(0).astype(int)
employees['Gender'] = employees['Gender'].astype('category')
employees['Team'] = employees['Team'].astype('category')
# %%
employees.info()
# %%
employees['First Name'] == 'Maria'
# %% [markdown]
# If we can get all the rows with a value of *True* in the Series above selected from our original employees DataFrame, we would have all the "Maria" records in the dataset
employees[employees['First Name'] == 'Maria']
# %% [markdown]
# we can also assign the Boolean Series to a descriptive variable, then pass that variable into the square brackets instead.
marias = employees['First Name'] == 'Maria'
employees[marias]
# %% [markdown]
# What if we wanted to pull out all employees who are not on the HR team? 
print('Engineering' != 'HR')
# %%
(employees['Team'] != "HR").head()
# %% [markdown]
# Again, we can pass the Series into square brackets to extract the DataFrame rows in which an index position has a value of *True*
employees[employees['Team'] != 'HR']
# %% [markdown]
# What if we wanted to retrieve all of our managers? Do we need to execute **employees["Mgmt"] == True**? We could do that but there is no need because we already have a Series of Booleans.
employees[employees['Mgmt']].head()
# %%
