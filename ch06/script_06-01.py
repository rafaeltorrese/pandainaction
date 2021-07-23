# %% [markdown] 
# # String Casing
import pandas as pd
# %%
inspections = pd.read_csv('data/chicago_food_inspections.csv')
inspections
# %%
inspections.columns
# %%
inspections['Name'].head()
# %% [markdown]
# A Series object includes a *str* attribute whose value is a StringMethods object that holds a toolbox of powerful methods
inspections['Name'].str
# %%
inspections['Name'].str.lstrip().head()
# %%
inspections['Name'].str.rstrip().head()
# %%
inspections['Name'].str.strip().head()
# %%
inspections['Name'] = inspections['Name'].str.strip()

# %%
for column in inspections.columns:
    inspections[column] = inspections[column].str.strip()
print(inspections.head())
# %% [markdown]
# Python's string casing methods are all available on Series objects. 
inspections['Name'].str.lower().head()
# %%
inspections['Name'].str.capitalize().head()
# %% [markdown]
inspections['Name'].str.title().head()
# %%
inspections['Risk'].head()
# %%
len(inspections)
# %%
inspections['Risk'].value_counts(dropna=False)