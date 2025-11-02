import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
from pathlib import Path
from itertools import product


data = pd.read_csv("./WineQualityData/winequality-white.csv", sep=';')

X = data.drop("quality", axis=1)
y = data["quality"]  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

param_grid = {
    'n_estimators': [100, 200, 300, 400],
    'learning_rate': [0.05, 0.1, 0.2],
    'max_depth': [2, 3, 4, 5, 6, 7],
    'min_samples_split': [2, 3, 4, 5, 6],
    'min_samples_leaf': [1, 2, 3, 4]
}

best_model = None
best_r2 = float('-inf')
best_params = None

for n_estimators, learning_rate, max_depth, min_samples_split, min_samples_leaf in product(
    param_grid['n_estimators'],
    param_grid['learning_rate'],
    param_grid['max_depth'],
    param_grid['min_samples_split'],
    param_grid['min_samples_leaf']
):
    model = GradientBoostingRegressor(
        n_estimators=n_estimators,
        learning_rate=learning_rate,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        min_samples_leaf=min_samples_leaf,
        random_state=42
    )
    model.fit(X_train, y_train)


    y_test_pred = model.predict(X_test)
    test_r2 = r2_score(y_test, y_test_pred)

    print(f"Params: n_estimators={n_estimators}, learning_rate={learning_rate}, max_depth={max_depth}, "
          f"min_samples_split={min_samples_split}, min_samples_leaf={min_samples_leaf}")
    print(f"Test R²: {test_r2:.4f}")
    print("-" * 50)


    if test_r2 > best_r2:
        best_r2 = test_r2
        best_model = model
        best_params = (n_estimators, learning_rate, max_depth, min_samples_split, min_samples_leaf)


print(f"Best Params: n_estimators={best_params[0]}, learning_rate={best_params[1]}, max_depth={best_params[2]}, "
      f"min_samples_split={best_params[3]}, min_samples_leaf={best_params[4]}")
print(f"Best Test R²: {best_r2:.4f}")

model_path = Path(__file__).resolve().parent.parent / "models" / "white_wine_test.pkl"
joblib.dump(best_model, model_path)
