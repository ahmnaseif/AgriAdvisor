import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import joblib


# Load data
df = pd.read_csv('price_history.csv')

# Preprocess the data
df['Date'] = pd.to_datetime(df['Date'])
df.fillna(method='ffill', inplace=True)

# Reshape the data using melt
df_melted = pd.melt(df, id_vars=['Date', 'Location'], 
                    var_name='Crop', value_name='Price')

# Drop rows where Price is NaN
df_melted.dropna(subset=['Price'], inplace=True)


# Prepare features and target
X = df_melted[['Date', 'Crop', 'Location']]
y = df_melted['Price']

print("AAAA")
print(X)
print(y)

# Convert Date to ordinal
X.loc[:, 'Date'] = X['Date'].map(pd.Timestamp.toordinal)

# Label encoding for crops and locations
le_crop = LabelEncoder()
le_location = LabelEncoder()

# Safely transform and avoid SettingWithCopyWarning
X.loc[:, 'Crop'] = le_crop.fit_transform(X['Crop'])
X.loc[:, 'Location'] = le_location.fit_transform(X['Location'])

# Train model
model = LinearRegression()
model.fit(X, y)

# Save the model and encoders
joblib.dump(model, 'crop_price_model.pkl')
joblib.dump(le_crop, 'label_encoder_crop.pkl')
joblib.dump(le_location, 'label_encoder_location.pkl')

# Prediction function
def predict_price(crop, date, location):
    print("Start Prediction")
    model = joblib.load('crop_price_model.pkl')
    le_crop = joblib.load('label_encoder_crop.pkl')
    le_location = joblib.load('label_encoder_location.pkl')

    print("Process Input.....")
    # Preprocess input
    crop_encoded = le_crop.transform([crop])[0]
    date_ordinal = pd.to_datetime(date).toordinal()
    location_encoded = le_location.transform([location])[0]
    
    print("Make prediction...")
    print(date_ordinal)
    print(crop_encoded)
    print(location_encoded)
    # Make prediction
    prediction = model.predict([[date_ordinal, crop_encoded, location_encoded]])
    print("Prediction")
    print(prediction)
    return prediction[0]
