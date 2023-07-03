import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the CSV data
data = pd.read_csv("weather_dataset.csv")

# Preprocess the data
data['wind_speed'] = data['wind'].str.split().str[1].astype(float)
data['humidity'] = data['humidity'].str.rstrip('%').astype(float)
data['update_time'] = pd.to_datetime(data['update_time'], format="%d-%m-%Y")

# Split the data into features (X) and target variable (y)
X = data[['wind_speed', 'humidity']]
y = data['temperature']

# Split the data into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing dataset
y_pred = model.predict(X_test)

# Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Predict weather for new observations
new_data = pd.DataFrame({'wind_speed': [2.5], 'humidity': [82]})
prediction = model.predict(new_data)
print("Predicted Temperature:", prediction[0])
