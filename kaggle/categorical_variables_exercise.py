import pandas as pd
from sklearn.model_selection import train_test_split

# Read the data
X = pd.read_csv('kaggle/train.csv', index_col='Id')
X_test = pd.read_csv('kaggle/test.csv', index_col='Id')

# Remove rows with missing target, separate target from predictors
X.dropna(axis=0, subset=['SalePrice'], inplace=True)
y = X.SalePrice
X.drop(['SalePrice'], axis=1, inplace=True)

# To keep things simple, we'll drop columns with missing value
cols_with_missing = [col for col in X.columns if X[col].isnull().any()]
X.drop(cols_with_missing, axis=1, inplace=True)
X_test.drop(cols_with_missing, axis=1, inplace=True)

# Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

# print(X_train.head())

# To compare different models, make score_dataset() function
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

#function for comparing different approaches
def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)

############## 
# 1. Drop categorical variable
##############
drop_X_train = X_train.select_dtypes(exclude=['object'])
drop_X_valid = X_valid.select_dtypes(exclude=['object'])
# print("MAE from Approach 1 (Drop categorical variables):")
# print(score_dataset(drop_X_train, drop_X_valid, y_train, y_valid))

############## 
# 2. Label Encoding
##############
# print("Unique values in 'Condition2' column in training data:", X_train['Condition2'].unique())
# print("\nUnique values in 'Condition2' column in validation data:", X_valid['Condition2'].unique())

# Fitting a label encoder to a column in the training data creates a corresponding integer-valued label for each unique value that appears in the training data. In the case that the validation data contains values that don't also appear in the training data, the encoder will throw an error, because these values won't have an integer assigned to them. Notice that the 'Condition2' column in the validation data contains the values 'RRAn' and 'RRNn', but these don't appear in the training data -- thus, if we try to use a label encoder with scikit-learn, the code will throw an error.

# This is a common problem that you'll encounter with real-world data, and there are many approaches to fixing this issue. For instance, you can write a custom label encoder to deal with new categories. The simplest approach, however, is to drop the problematic categorical columns.

# Run the code cell below to save the problematic columns to a Python list bad_label_cols. Likewise, columns that can be safely label encoded are stored in good_label_cols.

# All categorical columns
object_cols = [col for col in X_train.columns if X_train[col].dtype == "object"]

# Columns that can be safely label encoded
good_label_cols = [col for col in object_cols if set(X_train[col]) == set(X_valid[col])]

# Problematic columns that will be dropped from dataset
bad_label_cols = list(set(object_cols)-set(good_label_cols))

# print('Categorical columns that will be label encoded:', good_label_cols)
# print('\nCategorical columns that will be dropped from the dataset:', bad_label_cols)

from sklearn.preprocessing import LabelEncoder

# Drop categorical columns that will not be encoded
label_X_train = X_train.drop(bad_label_cols, axis=1)
label_X_valid = X_valid.drop(bad_label_cols, axis=1)

#Apply label encoder
label_encoder = LabelEncoder()
for col in set(good_label_cols):
    label_X_train[col] = label_encoder.fit_transform(label_X_train[col])
    label_X_valid[col] = label_encoder.transform(label_X_valid[col])

print("MAE from Approach 2 (Label Encoding):") 
print(score_dataset(label_X_train, label_X_valid, y_train, y_valid))