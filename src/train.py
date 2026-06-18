import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from xgboost import XGBClassifier

from sklearn.metrics import accuracy_score

df=pd.read_csv("data/Loan_approval.csv")

print(df.shape)
print(df.head())

df.drop("Loan_ID", axis=1, inplace=True)

df["Loan_Status"] = df["Loan_Status"].map({
    "Y": 1,
    "N": 0
})
X = df.drop("Loan_Status", axis=1)

y = df["Loan_Status"]


X_train , X_test , y_train , y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

categorical_cols= X.select_dtypes(
    include=["object", "string"]
                                  ).columns

numerical_cols=X.select_dtypes(
    exclude=["object", "string"]
).columns

print("Categorical columns:", categorical_cols)
print("Numerical columns:", numerical_cols)



categorical_transformer=Pipeline([
    (
"imputer", SimpleImputer(strategy="most_frequent")
    ),
    (
"encoder", OneHotEncoder(handle_unknown="ignore")
    )
])


numerical_transformer=Pipeline([
    (
        "imputer", SimpleImputer(strategy="median")
    )
])


preprocessor=ColumnTransformer([
    (
        "cat", 
        categorical_transformer,
        categorical_cols
    ),
    (
        "num",
        numerical_transformer,
        numerical_cols
    )
])
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    
    "Random Forest": RandomForestClassifier(
        n_estimators=200,
        random_state=42
    ),
    
    "XGBoost": XGBClassifier(
        random_state=42,
        eval_metric="logloss"
    )
}
best_model = None
best_score = 0

for name, model in models.items():

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])



    pipeline.fit(X_train, y_train)

    preds = pipeline.predict(X_test)

    score = accuracy_score(
        y_test,
        preds
    )

    print(f"{name}: {score:.4f}")

    if score > best_score:
        best_score = score
        best_model = pipeline


print("\nBest Accuracy:", best_score)

joblib.dump(
    best_model,
    "models/loan_approval_pipeline.pkl"
)

print("Best pipeline saved.")