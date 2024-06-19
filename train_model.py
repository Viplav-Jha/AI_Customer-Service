import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the data
file_path = 'bank-full.csv'
data = pd.read_csv(file_path)

# Data Preprocessing
# Assume 'Target' is the column you want to predict
encoded_data = pd.get_dummies(data, drop_first=True)
X = encoded_data.drop('Target_yes', axis=1)
y = encoded_data['Target_yes']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'model.pkl')
print("Model saved as model.pkl")
