
# ============================================================
# 1. Breast Cancer Diagnosis (sklearn)
# Dataset: load_breast_cancer()
#
# Tasks:
# • Load data and perform EDA (check class balance, feature distributions).
# • Split data (80% train, 20% test).
# • Train logistic regression without regularization (penalty=None).
# • Evaluate using confusion matrix, precision, recall, and ROC-AUC.
# • Add L2 regularization (tune C via grid search).
# • Identify top 3 most important features using coefficients.
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix,
    precision_score,
    recall_score,
    roc_auc_score,
    ConfusionMatrixDisplay
)

data = load_breast_cancer()

X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# ---------------- EDA ----------------

print("Shape:", X.shape)

print("\nClass Distribution:")
print(y.value_counts())

print("\nFeature Statistics:")
print(X.describe())

y.value_counts().plot(kind="bar")
plt.title("Class Distribution")
plt.xlabel("Class")
plt.ylabel("Count")
plt.show()

X.iloc[:, :5].hist(figsize=(12, 8))
plt.tight_layout()
plt.show()

X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.20,random_state=42,stratify=y)


scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


model = LogisticRegression(penalty=None,max_iter=5000)

model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
y_prob = model.predict_proba(X_test_scaled)[:, 1]

print("\nWithout Regularization")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_prob))


l2_model = LogisticRegression(penalty="l2",max_iter=5000)

param_grid = {"C": [0.001, 0.01, 0.1, 1, 10, 100]}

grid = GridSearchCV(l2_model,param_grid,cv=5,scoring="roc_auc")

grid.fit(X_train_scaled, y_train)

print("\nBest C:", grid.best_params_)
print("Best CV ROC-AUC:", grid.best_score_)

best_model = grid.best_estimator_

y_pred_l2 = best_model.predict(X_test_scaled)
y_prob_l2 = best_model.predict_proba(X_test_scaled)[:, 1]

print("\nL2 Regularization")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_l2))

print("Precision:", precision_score(y_test, y_pred_l2))
print("Recall:", recall_score(y_test, y_pred_l2))
print("ROC-AUC:", roc_auc_score(y_test, y_prob_l2))


coefficients = pd.Series(best_model.coef_[0], index=X.columns)

top_3 = coefficients.abs().sort_values(ascending=False).head(3)

print("\nTop 3 Important Features:")
print(top_3)

print("\nTheir coefficients:")
print(coefficients[top_3.index])

# ============================================================
# 2. Iris Flower Binary Classification (sklearn)
# Dataset: load_iris()
#
# Tasks:
# • Filter data to two classes and select sepal length and petal width.
# • Plot decision boundary using plt.scatter() and model coefficients.
# • Train model and calculate accuracy.
# • Introduce a dummy feature (random noise) and observe impact on coefficients.
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

iris = load_iris()
mask = iris.target < 2

X = iris.data[mask]
y = iris.target[mask]
X = X[:, [0, 3]]

model = LogisticRegression()

model.fit(X, y)

y_pred = model.predict(X)

print("Accuracy:", accuracy_score(y, y_pred))

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)


plt.figure(figsize=(8, 6))

plt.scatter(
    X[y == 0, 0],
    X[y == 0, 1],
    label="Setosa"
)

plt.scatter(
    X[y == 1, 0],
    X[y == 1, 1],
    label="Versicolor"
)

w1 = model.coef_[0][0]
w2 = model.coef_[0][1]
b = model.intercept_[0]

x_values = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)

y_values = -(w1 * x_values + b) / w2

plt.plot(x_values, y_values)

plt.xlabel("Sepal Length")
plt.ylabel("Petal Width")
plt.title("Logistic Regression Decision Boundary")
plt.legend()
plt.show()


np.random.seed(42)

dummy_feature = np.random.randn(len(X))

X_dummy = np.column_stack((X, dummy_feature))

model_dummy = LogisticRegression()

model_dummy.fit(X_dummy, y)

print("\nOriginal coefficients:")
print(model.coef_)

print("\nCoefficients with dummy feature:")
print(model_dummy.coef_)

print("\nDummy feature coefficient:")
print(model_dummy.coef_[0][2])

# ============================================================
# 3. Wine Type Classification (sklearn)
# Dataset: load_wine()
#
# Tasks:
# • StandardScaler preprocessing.
# • Train model with solver='sag' and compare convergence to 'lbfgs'.
# • Use cross_val_score (k=5) to estimate robustness.
# • Visualize feature importance via horizontal bar chart.
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

wine = load_wine()

X = wine.data
y = wine.target

mask = y < 2

X = X[mask]
y = y[mask]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


sag_model = LogisticRegression(solver="sag",max_iter=5000)

sag_model.fit(X_train_scaled, y_train)

print("SAG iterations:", sag_model.n_iter_)


lbfgs_model = LogisticRegression(solver="lbfgs",max_iter=5000)

lbfgs_model.fit(X_train_scaled, y_train)

print("LBFGS iterations:", lbfgs_model.n_iter_)


cv_scores = cross_val_score(sag_model,scaler.fit_transform(X),
    y,cv=5,scoring="accuracy")

print("\nCross Validation Scores:")
print(cv_scores)

print("Mean CV Accuracy:", cv_scores.mean())


coefficients = sag_model.coef_[0]

importance = pd.Series(coefficients,index=wine.feature_names)

importance = importance.abs().sort_values()

plt.figure(figsize=(10, 7))

importance.plot(kind="barh")

plt.xlabel("Absolute Coefficient")
plt.ylabel("Feature")
plt.title("Wine Feature Importance")

plt.show()

# ============================================================
# 4. Titanic Survival Prediction (Kaggle)
#
# Tasks:
# • Handle missing Age (impute median) and Embarked (impute mode).
# • One-hot encode Sex and Embarked.
# • Train model using Pclass, Sex, Age, SibSp.
# • Evaluate with ROC curve and calculate Youden’s J statistic.
# • Interpret odds ratios for Sex_male and Pclass.
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score

# Load the correct dataset for Titanic training
df = pd.read_csv("/content/train.csv")

features = ["Pclass","Sex","Age","SibSp","Embarked"]

X = df[features]
y = df["Survived"]

numeric_features = [
    "Pclass",
    "Age",
    "SibSp"
]

categorical_features = [
    "Sex",
    "Embarked"
]

numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median"))
])

categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(
        handle_unknown="ignore",
        drop="first"
    ))
])

preprocessor = ColumnTransformer([
    ("num", numeric_transformer, numeric_features),
    ("cat", categorical_transformer, categorical_features)
])

model = LogisticRegression(max_iter=1000)

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", model)
])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


pipeline.fit(X_train, y_train)

y_prob = pipeline.predict_proba(X_test)[:, 1]

# ROC
fpr, tpr, thresholds = roc_curve(y_test, y_prob)

roc_auc = roc_auc_score(y_test, y_prob)

plt.figure(figsize=(8, 6))

plt.plot(
    fpr,
    tpr,
    label=f"ROC-AUC = {roc_auc:.3f}"
)

plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--"
)

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Titanic ROC Curve")
plt.legend()
plt.show()


J = tpr - fpr

best_index = np.argmax(J)

best_threshold = thresholds[best_index]
best_J = J[best_index]

print("Best Threshold:", best_threshold)
print("Youden's J:", best_J)


feature_names = pipeline.named_steps[
    "preprocessor"
].get_feature_names_out()

coefficients = pipeline.named_steps[
    "model"
].coef_[0]

odds_ratios = np.exp(coefficients)

odds_df = pd.DataFrame({
    "Feature": feature_names,
    "Coefficient": coefficients,
    "Odds Ratio": odds_ratios
})

print("\nOdds Ratios:")
print(odds_df)

# ============================================================
# 5. Diabetes Prediction (Kaggle)
# Dataset: Pima Indians Diabetes
#
# Tasks:
# • Replace Glucose, BMI=0 values with mean.
# • Use LogisticRegressionCV for automated L1 regularization tuning.
# • Plot regularization path for Insulin vs Glucose.
# • Evaluate precision-recall tradeoff using PrecisionRecallDisplay.
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import PrecisionRecallDisplay

df = pd.read_csv("diabetes.csv")

df["Glucose"] = df["Glucose"].replace(0, np.nan)
df["BMI"] = df["BMI"].replace(0, np.nan)

df["Glucose"] = df["Glucose"].fillna(df["Glucose"].mean())
df["BMI"] = df["BMI"].fillna(df["BMI"].mean())

X = df.drop("Outcome", axis=1)
y = df["Outcome"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegressionCV(
    penalty="l1",
    solver="liblinear",
    cv=5,
    Cs=20,
    max_iter=5000
)

model.fit(X_train_scaled, y_train)

print("Best C:", model.C_[0])

# ---------------- Precision Recall ----------------

y_prob = model.predict_proba(X_test_scaled)[:, 1]

PrecisionRecallDisplay.from_predictions(
    y_test,
    y_prob
)

plt.title("Precision-Recall Curve")
plt.show()

# ---------------- Regularization Path ----------------

Cs = np.logspace(-4, 4, 20)

insulin_coef = []
glucose_coef = []

for C in Cs:

    temp_model = LogisticRegressionCV(
        penalty="l1",
        solver="liblinear",
        Cs=[C],
        cv=5,
        max_iter=5000
    )

    temp_model.fit(X_train_scaled, y_train)

    insulin_index = list(X.columns).index("Insulin")
    glucose_index = list(X.columns).index("Glucose")

    insulin_coef.append(
        temp_model.coef_[0][insulin_index]
    )

    glucose_coef.append(
        temp_model.coef_[0][glucose_index]
    )

plt.figure(figsize=(9, 6))

plt.semilogx(
    Cs,
    insulin_coef,
    label="Insulin"
)

plt.semilogx(
    Cs,
    glucose_coef,
    label="Glucose"
)

plt.xlabel("C")
plt.ylabel("Coefficient")
plt.title("L1 Regularization Path")
plt.legend()

plt.show()

# ============================================================
# 6. Spam Email Detection (Kaggle)
# Dataset: SMS Spam Collection
#
# Tasks:
# • Preprocess text: lowercase, remove punctuation.
# • Create TF-IDF features (TfidfVectorizer, max_features=500).
# • Train model and identify top 10 spam-indicative words.
# • Test model on custom input: "Congrats! You won $1000."
# ============================================================

import pandas as pd
import string

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


df = pd.read_csv(
    "spam.csv",
    sep='\t',
    header=None,
    names=["label", "message"],
    encoding="latin-1"
)


def clean_text(text):

    text = text.lower()

    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    return text

df["message"] = df["message"].apply(clean_text)

df["label"] = df["label"].map({
    "ham": 0,
    "spam": 1
})


X_train, X_test, y_train, y_test = train_test_split(
    df["message"],
    df["label"],
    test_size=0.2,
    random_state=42,
    stratify=df["label"]
)


vectorizer = TfidfVectorizer(
    max_features=500
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


model = LogisticRegression(max_iter=1000)

model.fit(X_train_tfidf, y_train)

y_pred = model.predict(X_test_tfidf)

print("Accuracy:", accuracy_score(y_test, y_pred))

# ---------------- Top 10 Spam Words ----------------

feature_names = vectorizer.get_feature_names_out()

coefficients = model.coef_[0]

word_importance = pd.Series(
    coefficients,
    index=feature_names
)

top_spam_words = word_importance.sort_values(
    ascending=False
).head(10)

print("\nTop 10 Spam Indicative Words:")
print(top_spam_words)

# ---------------- Custom Input ----------------

message = "Congrats! You won $1000."

message = clean_text(message)

message_tfidf = vectorizer.transform([message])

prediction = model.predict(message_tfidf)[0]

probability = model.predict_proba(
    message_tfidf
)[0, 1]

print("\nCustom Message:")
print("Congrats! You won $1000.")

if prediction == 1:
    print("Prediction: SPAM")
else:
    print("Prediction: HAM")

print("Spam Probability:", probability)

# ============================================================
# 7. Credit Card Fraud Detection (Kaggle)
#
# Tasks:
# • Use StandardScaler on Amount and Time.
# • Train model with class_weight='balanced'.
# • Optimize threshold to maximize F1-score.
# • Compare precision-recall curves with/without class weighting.
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    precision_recall_curve,
    f1_score
)

df = pd.read_csv("creditcard.csv")

X = df.drop("Class", axis=1)
y = df["Class"]

scaler = StandardScaler()

X["Amount"] = scaler.fit_transform(
    X[["Amount"]]
)

X["Time"] = scaler.fit_transform(
    X[["Time"]]
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


model_normal = LogisticRegression(
max_iter=1000
)

model_normal.fit(X_train, y_train)

prob_normal = model_normal.predict_proba(
    X_test
)[:, 1]

precision_normal, recall_normal, _ = precision_recall_curve(
    y_test,
    prob_normal
)

# ---------------- With Class Weight ----------------

model_balanced = LogisticRegression(
    class_weight="balanced",
    max_iter=1000
)

model_balanced.fit(X_train, y_train)

prob_balanced = model_balanced.predict_proba(
    X_test
)[:, 1]

precision_balanced, recall_balanced, thresholds = precision_recall_curve(
    y_test,
    prob_balanced
)

# ---------------- Optimize Threshold ----------------

f1_scores = 2 * (
    precision_balanced * recall_balanced
) / (
    precision_balanced + recall_balanced + 1e-10
)

best_index = np.argmax(f1_scores)

best_threshold = thresholds[best_index]

print("Best Threshold:", best_threshold)
print("Best F1:", f1_scores[best_index])

# ---------------- Plot PR Curves ----------------

plt.figure(figsize=(9, 6))

plt.plot(
    recall_normal,
    precision_normal,
    label="Without Class Weight"
)

plt.plot(
    recall_balanced,
    precision_balanced,
    label="With Class Weight"
)

plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision-Recall Comparison")

plt.legend()
plt.show()

# ============================================================
# 8. Employee Attrition (Kaggle)
# Dataset: IBM HR Analytics
#
# Tasks:
# • One-hot encode Department, JobRole, OverTime.
# • Analyze coefficient for OverTime_Yes and MonthlyIncome.
# • Calculate log-loss using log_loss(y_test, y_pred_proba).
# • Deploy model via pickle and predict attrition for synthetic input.
# ============================================================

import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

features = [
    "Department",
    "JobRole",
    "OverTime",
    "MonthlyIncome"
]

X = df[features]
y = df["Attrition"].map({
    "Yes": 1,
    "No": 0
})

categorical_features = [
    "Department",
    "JobRole",
    "OverTime"
]

numeric_features = [
    "MonthlyIncome"
]


preprocessor = ColumnTransformer([
    (
        "cat",
        OneHotEncoder(
            drop="first",
            handle_unknown="ignore"
        ),
        categorical_features
    )
], remainder="passthrough")

model = LogisticRegression(
    max_iter=2000
)

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", model)
])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

pipeline.fit(X_train, y_train)

y_pred_proba = pipeline.predict_proba(
    X_test
)[:, 1]

loss = log_loss(
    y_test,
    y_pred_proba
)

print("Log Loss:", loss)

# ---------------- Coefficients ----------------

feature_names = pipeline.named_steps[
    "preprocessor"
].get_feature_names_out()

coefficients = pipeline.named_steps[
    "model"
].coef_[0]

coef_df = pd.DataFrame({
    "Feature": feature_names,
    "Coefficient": coefficients
})

print("\nCoefficients:")
print(coef_df)

# ---------------- Pickle ----------------

with open("employee_attrition_model.pkl", "wb") as file:

    pickle.dump(
        pipeline,
        file
    )

print("\nModel saved successfully.")

# ---------------- Synthetic Employee ----------------

new_employee = pd.DataFrame({
    "Department": ["Sales"],
    "JobRole": ["Sales Executive"],
    "OverTime": ["Yes"],
    "MonthlyIncome": [5000]
})

prediction = pipeline.predict(
    new_employee
)[0]

probability = pipeline.predict_proba(
    new_employee
)[0, 1]

print("\nSynthetic Employee Prediction:")

if prediction == 1:
    print("Attrition: Yes")
else:
    print("Attrition: No")

print("Probability:", probability)

# ============================================================
# 9. Heart Disease Prediction (Kaggle)
# Dataset: UCI Heart Disease
#
# Tasks:
# • Handle categorical features: cp, restecg (one-hot encode).
# • Use PolynomialFeatures(degree=2) + feature selection (SelectKBest).
# • Tune tol (tolerance) to control training time.
# • Build calibration curve with CalibrationDisplay.
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import (
    OneHotEncoder,
    PolynomialFeatures,
    StandardScaler
)
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.linear_model import LogisticRegression
from sklearn.calibration import CalibrationDisplay

df = pd.read_csv("heart.csv")

X = df.drop("target", axis=1)
y = df["target"]

categorical_features = [
    "cp",
    "restecg"
]

numeric_features = [
    col for col in X.columns
    if col not in categorical_features
]

preprocessor = ColumnTransformer([
    (
        "cat",
        OneHotEncoder(handle_unknown="ignore"),
        categorical_features
    )
], remainder="passthrough")

pipeline = Pipeline([
    (
        "preprocessing",
        preprocessor
    ),

    (
        "poly",
        PolynomialFeatures(
            degree=2,
            include_bias=False
        )
    ),

    (
        "scaler",
        StandardScaler()
    ),

    (
        "selection",
        SelectKBest(
            score_func=f_classif,
            k=20
        )
    ),

    (
        "model",
        LogisticRegression(
            tol=1e-4,
            max_iter=5000
        )
    )
])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

pipeline.fit( X_train, y_train)

y_prob = pipeline.predict_proba( X_test)[:, 1]

CalibrationDisplay.from_predictions( y_test,y_prob, n_bins=10)

plt.title("Heart Disease Calibration Curve")
plt.show()

for tol in [1e-2, 1e-3, 1e-4, 1e-5]:

    temp_pipeline = Pipeline([
        ("preprocessing", preprocessor),
        (
            "poly",
            PolynomialFeatures(
                degree=2,
                include_bias=False
            )
        ),
        ("scaler", StandardScaler()),
        (
            "selection",
            SelectKBest(
                score_func=f_classif,
                k=20
            )
        ),
        (
            "model",
            LogisticRegression(
                tol=tol,
                max_iter=5000
            )
        )
    ])

    temp_pipeline.fit(
        X_train,
        y_train
    )

    iterations = temp_pipeline.named_steps[
        "model"
    ].n_iter_

    print(
        "tol =", tol,
        "iterations =", iterations
    )

# ============================================================
# 10. Loan Default Prediction (Kaggle)
# Dataset: Loan Data
#
# Tasks:
# • Impute missing Credit_History (mode).
# • Convert Property_Area (rural/semiurban/urban) to ordinal.
# • Train logistic regression with stochastic gradient descent solver
#   (solver='saga').
# • Generate SHAP values for explainability.
# ============================================================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("loan_data.csv")

# ---------------- Target ----------------

target = "Loan_Status"

df[target] = df[target].map({
    "Y": 1,
    "N": 0
})

# ---------------- Credit History ----------------


mode_value = df["Credit_History"].mode()[0]

df["Credit_History"] = df[
    "Credit_History"
].fillna(mode_value)

# ---------------- Property Area ----------------


property_mapping = {
    "Rural": 0,
    "Semiurban": 1,
    "Urban": 2
}

df["Property_Area"] = df[
    "Property_Area"
].map(property_mapping)

# ---------------- Prepare X/y ----------------

X = df.drop(target, axis=1)
y = df[target]

X = X.select_dtypes(
    include=["int64", "float64"]
)

imputer = SimpleImputer(
    strategy="median"
)

X = pd.DataFrame(
    imputer.fit_transform(X),
    columns=X.columns
)

# ---------------- Split ----------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ---------------- Scaling ----------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ---------------- SAGA Logistic Regression ----------------

model = LogisticRegression(
    solver="saga",
    max_iter=5000
)

model.fit(
    X_train_scaled,
    y_train
)

print("Training completed.")

print(
    "Number of iterations:",
    model.n_iter_
)

y_pred = model.predict(
    X_test_scaled
)

print("\nPredictions:")
print(y_pred[:10])



import shap

explainer = shap.LinearExplainer(
    model,
    X_train_scaled
)

shap_values = explainer(
    X_test_scaled
)

shap.summary_plot(
    shap_values,
    X_test_scaled,
    feature_names=X.columns
)