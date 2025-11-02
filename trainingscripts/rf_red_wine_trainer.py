import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
from pathlib import Path

data = pd.read_csv("./WineQualityData/winequality-red.csv", sep=';')

X = data.drop("quality", axis=1)
y = data["quality"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("===== Red Wine Quality Prediction =====")
print("Mean Squared Error:", mse)
print("R² Score:", r2)

model_path = Path(__file__).resolve().parent.parent / "models" / "red_wine_quality_model.pkl"
joblib.dump(model, model_path)