from benedict import benedict

data = {
    "id_1": {
        "name": "John",
        "surname": "Doe",
        "age": 25,
        "skills": {
            "programming": {
                "Python": "5",
                "Java": "4",
            },
        },
        "languages": ["English", "French", "Spanish"],
    },
    "id_2": {
        "name": "Bob",
        "surname": "Marley",
        "age": 29,
        "skills": {
            "programming": {
                "Python": "4",
                "JavaScript": "4",
            },
        },
        "languages": ["English", "Portugal", "Italy"],
    }
}

data = benedict(data)


[data[key, "name"] for key in data ]
# output:
['John', 'Bob']

[(data[key, "name"], data[key, "skills"]) for key in data ]
# output:
[('John', {'programming': {'Python': '5', 'Java': '4'}}), ('Bob', {'programming': {'Python': '4', 'JavaScript': '4'}})]



# keypaths
# Return a list of all keypaths in the dict.
# If indexes is True, the output will include list values indexes.
# k = d.keypaths(indexes=False)
data.keypaths()
# output:
['id_1', 'id_1.age', 'id_1.languages', 'id_1.name', 'id_1.skills', 'id_1.skills.programming', 'id_1.skills.programming.Java', 'id_1.skills.programming.Python', 'id_1.surname', 'id_2', 'id_2.age', 'id_2.languages', 'id_2.name', 'id_2.skills', 'id_2.skills.programming', 'id_2.skills.programming.JavaScript', 'id_2.skills.programming.Python', 'id_2.surname']


# filter
# Return a filtered dict using the given predicate function.
# Predicate function receives key, value arguments and should return a bool value.
# predicate = lambda k, v: v is not None
# f = d.filter(predicate)
data.filter(lambda key, value: value.age == 29)
# output:
{'id_2': {'name': 'Bob', 'surname': 'Marley', 'age': 29, 'skills': {'programming': {'Python': '4', 'JavaScript': '4'}}, 'languages': ['English', 'Portugal', 'Italy']}}
data.filter(lambda key, value: "Java" in value.skills.programming)
# output:
{'id_1': {'name': 'John', 'surname': 'Doe', 'age': 25, 'skills': {'programming': {'Python': '5', 'Java': '4'}}, 'languages': ['English', 'French', 'Spanish']}}


# flatten
# Return a new flattened dict using the given separator to join nested dict keys to flatten keypaths.
# f = d.flatten(separator="_")
print(data.flatten(separator="/").dump())
# output:
{
    "id_1/age": 25,
    "id_1/languages": [
        "English",
        "French",
        "Spanish"
    ],
    "id_1/name": "John",
    "id_1/skills/programming/Java": "4",
    "id_1/skills/programming/Python": "5",
    "id_1/surname": "Doe",
    "id_2/age": 29,
    "id_2/languages": [
        "English",
        "Portugal",
        "Italy"
    ],
    "id_2/name": "Bob",
    "id_2/skills/programming/JavaScript": "4",
    "id_2/skills/programming/Python": "4",
    "id_2/surname": "Marley"
}


# search
# Search and return a list of items (dict, key, value, ) matching the given query.
# r = d.search("hello", in_keys=True, in_values=True, exact=False, case_sensitive=False)
data.search("Java", in_keys=True, in_values=True, exact=False, case_sensitive=False)
# output:
[({'Python': '5', 'Java': '4'}, 'Java', '4'), ({'Python': '4', 'JavaScript': '4'}, 'JavaScript', '4')]
data.search("Java", in_keys=True, in_values=True, exact=True, case_sensitive=False)
# output:
[({'Python': '5', 'Java': '4'}, 'Java', '4')]


# subset
# Return a dict subset for the given keys.
# It is possible to pass a single key or more keys (as list or *args).
# s = d.subset(["firstname", "lastname", "email"])
data["id_2"].subset(["skills"])
# output:
{'skills': {'programming': {'Python': '4', 'JavaScript': '4'}}}
data.id_2.subset(["skills"])
# output:
{'skills': {'programming': {'Python': '4', 'JavaScript': '4'}}}
