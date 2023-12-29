import requests
from datetime import *
import os
GENDER = "male"
WEIGHT_KG = 71
HEIGHT_CM = 1.75
AGE = 25

API_ID=os.environ["OW_API_ID"]
API_KEY=os.environ["OW_API_KEY"]
END_POINT="https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint="https://api.sheety.co/f78847236614167da59c54f05e021939/workout/workouts"
SHEETYS_AUTH=os.environ["SHEETY_AUTH"]
text=input("Tell me which exercise u did: ")
headers={
        'x-app-id':API_ID,
        'x-app-key':API_KEY
    }
parameters = {
    "query": text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response=requests.post(url=END_POINT,json=parameters,headers=headers)
result=response.json()
print(result)

today = datetime.now().strftime("%d/%m/%Y")
now = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_inputs={
        "workout":{
            "date":today,
            "time":now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
sheet_response=requests.post(sheet_endpoint,json=sheet_inputs)
print(sheet_response.text)

#basic authentication
sheety_headers={
    "Authorization":SHEETYS_AUTH
}
sheet_response=requests.post(sheet_endpoint,
                             json=sheet_inputs,
                             auth=('tenzi','your_password'),
                             headers=sheety_headers)
