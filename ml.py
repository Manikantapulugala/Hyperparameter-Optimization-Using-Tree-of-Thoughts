import numpy as np
import pandas as pd
import sklearn
import seaborn as sns
from sklearn.model_selection import GridSearchCV
import time
import matplotlib.pyplot as plt

df = pd.read_csv("merged_crop_dataset.csv")
df.head()

df.info()

df = df.rename(columns = {
    "N" : 'Nitrogen(N)',
    "P" : 'Phosphorus(P)',
    "K" : 'Potassium(K)'})

df.head()

df.isnull().sum()

df.duplicated().sum()

cols = df.select_dtypes(include="number")

plt.figure(figsize=(12, 6))
for i, j in enumerate(cols):
  plt.subplot(2, 4, i+1)
  sns.boxplot(y=df[j])
  plt.title(j)

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
for i, j in enumerate(cols):
  plt.subplot(2, 4, i+1)
  sns.kdeplot(df[j])
  plt.title(j)

plt.tight_layout()
plt.show()

## **Target Column**

y = df["label"]
x = df.drop(columns = "label")
x.shape, y.shape

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

y = le.fit_transform(y)

## **Split data**

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
x_train.shape, x_test.shape, y_train.shape, y_test.shape

x_train.info()

## **preprocessing**

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.linear_model   import LogisticRegression

trans = ColumnTransformer([("t1", StandardScaler(), [0,1,2,3,4,5,6])], remainder="passthrough")

log_model = make_pipeline(trans, LogisticRegression())
log_model.fit(x_train, y_train)


## **LogisticRegression**

from sklearn.metrics import accuracy_score
y_pred = log_model.predict(x_test)
test_acc = accuracy_score(y_test, y_pred)

x_pred = log_model.predict(x_train)
train_acc = accuracy_score(y_train, x_pred)

print("Random Forest Train Accuracy:", train_acc)
print("Random Forest Test Accuracy :", test_acc)

## **RandomForest**

from sklearn.ensemble import RandomForestClassifier

rf_model = make_pipeline(trans, RandomForestClassifier())
rf_model.fit(x_train, y_train)

param_grid = {
    'randomforestclassifier__n_estimators': [50, 100, 200],
    'randomforestclassifier__max_depth': [5, 10, None],
    'randomforestclassifier__min_samples_split': [2, 5],
    'randomforestclassifier__min_samples_leaf': [1, 2],
    'randomforestclassifier__max_features': [None, 'sqrt', 'log2']
}

grid_search = GridSearchCV(
    estimator=rf_model,
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    return_train_score=True,
    n_jobs=-1
)

# Start timer
start_time = time.time()

# Train model
grid_search.fit(x_train, y_train)

# End timer
training_time = time.time() - start_time

best_params = grid_search.best_params_
best_score = grid_search.best_score_
best_model = grid_search.best_estimator_

print("Best Model:", best_model)
print("Best Parameters:", best_params)
print("Best Score:", best_score)

print("Training Time:", training_time, "seconds")

from sklearn.ensemble import RandomForestClassifier

rf_model = make_pipeline(trans, RandomForestClassifier())
rf_model.fit(x_train, y_train)
y_pred = rf_model.predict(x_test)
accuracy_score(y_test, y_pred)

x_pred = rf_model.predict(x_train)
accuracy_score(y_train, x_pred)

results = pd.DataFrame(grid_search.cv_results_)

final_results = pd.DataFrame({
    "n_estimators": results["param_randomforestclassifier__n_estimators"],
    "max_depth": results["param_randomforestclassifier__max_depth"],
    "min_samples_split":results["param_randomforestclassifier__min_samples_split"],
    "min_samples_leaf":results["param_randomforestclassifier__min_samples_leaf"],
    "max_features":results["param_randomforestclassifier__max_features"],

    "CV Score":results["mean_test_score"],

    "Train Score":results["mean_train_score"],

    "Training Time":results["mean_fit_time"]
})

final_results["Overfitting Gap"] = (final_results["Train Score"] - final_results["CV Score"])

final_results.head()

# Convert results to text
results_text = final_results.to_string(index=False)

#print("Sending results to Gemini...")

# Get Gemini analysis
#analysis = analyze_results(results_text)

#print("\nGemini Analysis:\n")
#print(analysis)