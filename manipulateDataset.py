from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np

data_set=pd.read_csv('dataset.csv')

columns_to_impute=['Age','Email']

data_set.replace("NAN", np.nan,inplace=True)

imputer=SimpleImputer(missing_values=np.nan,strategy='most_frequent')

data_set[columns_to_impute] = imputer.fit_transform(data_set[columns_to_impute])

print("\nDataset after Imputation")
print(data_set)