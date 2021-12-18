# Model Serving and Monitoring with Flask and Heroku


This tutorial on model serving and monitoring with Flask and Heroku was prepared by **Fortune Adekogbe** and taught by **Tejumade Afonja**. Kindly reach out to [this email](teju.afonja@aisatudayslagos.com) for any questions or clarifications.


## Resources

- [Link to Tutorial Slide](https://docs.google.com/presentation/d/1MvHjWl2WEF1pEBkwQiYdrkYrMv_HQq-h3ZEVxITpoT4/edit?usp=sharing)


## APIs
- Staging: https://ai6lagos-c7-cancer-app-staging.herokuapp.com/predict
- Production:https://ai6lagos-c7-cancer-app.herokuapp.com/predict

## Using test data
```
import joblib
import requests
import json

[X_test, y_test] = joblib.load("test_data.sav")

url = "https://ai6lagos-cancer-app.herokuapp.com/predict"
response = requests.post(url, json.dumps(X_test[0]))
print(response.json(), y_test[0])
```
