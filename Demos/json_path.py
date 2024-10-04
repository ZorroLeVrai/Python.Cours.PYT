import json
from jsonpath_ng import jsonpath, parse

file_path = "Notebooks/input.json"

with open(file_path, 'r') as file:
    json_data = json.load(file)

jsonpath_expr = parse("$.menu.popup.menuitem[*].value")

#récupération des données à l'aide du jsonpath
matches = jsonpath_expr.find(json_data)

values = [match.value for match in matches]
print(values)