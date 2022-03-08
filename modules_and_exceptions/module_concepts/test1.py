print("this is my first module")
data = {
    "name": "venkat",
    "course": ["ML", "DL", "CV", "NLP" ],
    "msg": "this is my class"
}

def get_course():
    return data['course']

def msg():
    return data["msg"]