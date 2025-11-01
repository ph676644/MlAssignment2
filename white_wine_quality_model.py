import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

data = pd.read_csv("./WineQualityData/winequality-white.csv", sep=';')

X = data.drop("quality", axis=1)
y = data["quality"]  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(
    n_estimators=200,
    min_samples_split=2,
    min_samples_leaf=1,
    random_state=42
)
model.fit(X_train, y_train)


# Evaluate on training data
y_train_pred = model.predict(X_train)
train_mse = mean_squared_error(y_train, y_train_pred)
train_r2 = r2_score(y_train, y_train_pred)

# Evaluate on testing data
y_test_pred = model.predict(X_test)
test_mse = mean_squared_error(y_test, y_test_pred)
test_r2 = r2_score(y_test, y_test_pred)

print("===== White Wine Quality Prediction =====")
print("Training MSE:", train_mse)
print("Training R²:", train_r2)
print("Testing MSE:", test_mse)
print("Testing R²:", test_r2)

joblib.dump(model, "white_wine_quality_model.pkl")