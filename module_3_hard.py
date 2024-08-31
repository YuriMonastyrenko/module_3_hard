data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_structure):
    answer = 0
    if isinstance(data_structure, dict):
        for key, item in data_structure.items():
            answer += calculate_structure_sum(key)
            answer += calculate_structure_sum(item)
    elif isinstance(data_structure, (list, tuple, set)):
        for i in data_structure:
            answer += calculate_structure_sum(i)
    elif isinstance(data_structure, str):
        answer += len(data_structure)
    elif isinstance(data_structure, int):
        answer += data_structure
    return answer
result = calculate_structure_sum(data_structure)
print(result)
