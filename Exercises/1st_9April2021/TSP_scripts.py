import numpy as np


def sample_n_points(n:int, dims=2, x_min=0, x_max=1):
    x = np.random.uniform(x_min, x_max, (n, dims))
    return x


def compute_distance_matrix(points: np.ndarray):
    n, d = points.shape
    return np.linalg.norm(points - points.reshape(n, 1, d), axis=2)


def concatenate_to_all_lists(lists: list, element):
    for i in range(len(lists)):
        lists[i].append(element)

def all_subsets_of_n_elements(elements:list, n:int):
    if n == 1:
        return [[e] for e in elements]
    else:
        subsets = []
        for i in range(len(elements)):
            subset = all_subsets_of_n_elements(elements[i+1:], n-1)
            concatenate_to_all_lists(subset, elements[i])
            subsets.extend(subset)
            
        return subsets


def all_permutations(elements:list):
    if len(elements) == 1:
        return [elements]
    else:
        subsets = []
        for i in range(len(elements)):
            remaining_elements = elements.copy()
            remaining_elements.pop(i)
            subset = all_permutations(remaining_elements)
            concatenate_to_all_lists(subset, elements[i])
            subsets.extend(subset)
            
        return subsets


def get_path_length(D, path):
    length = 0
    for i in range(len(path) - 1):
        length += D[path[i], path[i+1]]
    return length + D[path[-1], path[0]]


def get_all_paths_lengths(D, paths):
    return [get_path_length(D, path) for path in paths]