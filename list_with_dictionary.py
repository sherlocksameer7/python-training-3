stud_data = [
    {"name": "sameer",
     "marks": [
         {"English": 44,
          "Science": 50},
         {"English": 84,
          "Science": 40}
     ]
     },
    {"name": "dhanush",
     "marks": [
         {"English": 64,
          "Science": 70},
         {"English": 94,
          "Science": 80}
     ]
     }
]

for i in stud_data:
    print(i["name"])
    for j in i["marks"]:
        print(j["English"])
       # print(j["Science"])

