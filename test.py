import requests

response = requests.post("http://127.0.0.1:8000/api/feedback/",data={
    "experience" : "Bad",
    "feedback" : "Hello"
})

print(response)