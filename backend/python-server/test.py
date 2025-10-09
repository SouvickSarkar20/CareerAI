import requests

url = "http://127.0.0.1:5000/predict-placement"

data = {
    "tier": 3,
    "cgpa": 6.5,
    "inter_gpa": 8.1,
    "ssc_gpa": 8.6,
    "internships": 2,
    "no_of_projects": 3,
    "is_participate_hackathon": 1,
    "is_participated_extracurricular": 1,
    "no_of_programming_languages": 4,
    "dsa": 1,
    "mobile_dev": 0,
    "web_dev": 1,
    "Machine Learning": 1,
    "cloud": 0,
    "CSE": 1,
    "ECE": 0,
    "MECH": 0
}

response = requests.post(url, json=data)
print("Response:", response.json())
