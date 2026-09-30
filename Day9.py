careers = [
    {"career": "Software Engineer", "salary": 30, "remote": True},
    {"career": "Cybersecurity", "salary": 25, "remote": True},
    {"career": "Web Developer", "salary": 20, "remote": True},
]

for jobs in careers:
    print(jobs["career"])
    print(jobs["salary"])

    if jobs["remote"]:
        print("Remote")
    else:
        print("Not Remote")

    if jobs["salary"] >= 25:
        print("Good Salary")
    else:
        print("Low Salary")