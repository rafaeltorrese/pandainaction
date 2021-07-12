# %% [markdown]
# # Filtering by Condition
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
# ## The **isin** Method
# What if we wanted to isolate all employees on either the Sales, Legal, or Marketing teams? We could declare three separate Series and use them all inside the square brackets with the OR criteria.
sales = employees['Team'] == 'Sales'
legal = employees['Team'] == 'Legal'
mktg = employees['Team'] == 'Marketing'
employees[sales | legal | mktg].head()
# %% [markdown]
# A better solution is the **isin** method, which accepts a list of elements. It returns a Boolean Series in which a True indicates that a row's value is found amongst the list's values.
all_star_teams = ['Sales', 'Legal', 'Marketing']
in_team = employees['Team'].isin(all_star_teams)
employees[in_team].head() 

# %% [markdown]
# ##  The between Method 
# Another common challenge, especially when dealing with numeric data, is extracting values that fall within a range
higher_than_80 = employees['Salary'] >= 80000
lower_than_90 = employees['Salary'] < 90000
employees[higher_than_80 & lower_than_90].head()
# %% [markdown] 
# Note that the first argument, the lower bound, is inclusive while the second argument, the upper bound, is exclusive
between_80k_and_90k = employees['Salary'].between(80000, 90000)
print(employees[between_80k_and_90k].head())
# %% [markdown]
# The between method also works on columns of datetime values. We can pass strings representing the start and end dates of our time range. The respective parameters are *left* and *right*. Below, we find all employees who started with the company in the 1980s
eighties_folk = employees['Start Date'].between(
    left = '1980-01-01',
    right = '1990-01-01',
)
print(employees[eighties_folk].head())
# %% [markdown]
# Finally, we can apply the between method to string columns. Let's extract all employees whose first name starts with "R". We'll start with a capital "R" as our inclusive lower bound and go up to the non-inclusive upper bound of "S".
name_starts_with_r = employees['First Name'].between('R', 'S')
print(employees[name_starts_with_r].head())
# %% [markdown]
# ## The **isnull** and **notnull** Methods
print(employees.head())
print()
print(employees['Team'].isnull().head())
print()
print(employees['Team'].notnull().head())
print()
print(
    ~(employees['Team'].isnull()).head()
    )
# %% [markdown]
# Once again, we can use these Boolean Series to select specific rows from the DataFrame
no_team = employees['Team'].isnull()
employees[no_team].head()
# %%
has_name = employees['First Name'].notnull()
print(employees[has_name].tail())
# %% [markdown]
# ## Dealing with Null Values
employees = pd.read_csv('data/employees.csv', parse_dates=['Start Date'])
employees

# %% [markdown] 
# By default, the drop_na method will remove all rows from the DataFrame that hold any **NaN** values. 
employees.dropna()
# %% [markdown] 
#  We can pass an argument of "all" to the how parameter of the dropna method to remove rows where all values are **NaN** or **NaT**
employees.dropna(how='all')
# %% [markdown]
# The subset parameter is used to remove rows with a missing value in a specific column.
employees.dropna(subset=['Gender']).tail() 
# %% [markdown]
# We can also pass the subset parameter a list of several strings. A row will be removed if it has a missing value in any of the specified columns.
employees.dropna(subset=['Start Date', 'Salary'])
# %% [markdown]
# The **thresh** parameter specifies a minimum threshold of non-null values that a row must have in order to be kept. 
employees.dropna(how='any', thresh=4).head()