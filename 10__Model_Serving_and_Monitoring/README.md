# Model Serving and Monitoring with Flask and Heroku


====

**Prepared by:** Fortune Adekogbe \
**Taught by:** Tejumade Afonja 

====

[Slide for Model Serving and Monitoring with Flask and Heroku](https://docs.google.com/presentation/d/1MvHjWl2WEF1pEBkwQiYdrkYrMv_HQq-h3ZEVxITpoT4/edit?usp=sharing)

## APIs
- Staging: https://pectus-cancer-app-staging.herokuapp.com/predict
- Production: https://pectus-cancer-app.herokuapp.com/predict

## Using test data
```
import joblib
import requests
import json

[X_test, y_test] = joblib.load("test_data.sav")

url = "https://pectus-cancer-app.herokuapp.com/predict"
response = requests.post(url, json.dumps(X_test[0]))
print(response.json(), y_test[0])
```