import sys
import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

MODEL_PATH = "src/best_model_rf.joblib"
DATA_PATH = "data/day_2011.csv"

# Quality gate (set a threshold that SHOULD pass for your chosen dataset)
# Start with 900 (safe). You can tune later.
RMSE_THRESHOLD = 900.0

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["dteday"] = pd.to_datetime(df["dteday"], dayfirst=True, errors="coerce")
    df["day_of_year"] = df["dteday"].dt.dayofyear
    df = df.drop(columns=["dteday"])
    return df

def main():
    model = joblib.load(MODEL_PATH)

    df = pd.read_csv(DATA_PATH)
    df = add_features(df)

    y = df["cnt"]
    X = df.drop(columns=["cnt"])

    preds = model.predict(X)

    rmse = np.sqrt(mean_squared_error(y, preds))
    mae = mean_absolute_error(y, preds)
    r2 = r2_score(y, preds)

    print(f"RMSE: {rmse:.4f}")
    print(f"MAE : {mae:.4f}")
    print(f"R2  : {r2:.4f}")
    print(f"Quality Gate: RMSE <= {RMSE_THRESHOLD}")

    if rmse > RMSE_THRESHOLD:
        print("❌ Quality Gate FAILED")
        sys.exit(1)

    print("✅ Quality Gate PASSED")
    sys.exit(0)

if __name__ == "__main__":
    main()