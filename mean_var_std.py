import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    mean = np.mean(list)
    #print(mean)

    variance = np.var(list)
    #print(variance)

    standard_deviation = np.std(list)
    #print(standard_deviation)

    max_number = np.max(list)
    #print(max_number)

    min_number = np.min(list)
   # print(min_number)

    sum = np.sum(list)
    #print(sum)

    matrix = np.reshape(list, (3 , 3))
    #print('This is the matrix', matrix)


    calculations = {
        'mean': [np.mean(matrix, axis=0).tolist(),
            np.mean(matrix, axis=1).tolist(),
          np.mean(matrix).item()],
        'variance': [np.var(matrix, axis=0).tolist(),
            np.var(matrix, axis=1).tolist(),
          np.var(matrix).item()],
        'standard deviation': [np.std(matrix, axis=0).tolist(),
            np.std(matrix, axis=1).tolist(),
          np.std(matrix).item()],
        'max': [np.max(matrix, axis=0).tolist(),
            np.max(matrix, axis=1).tolist(),
          np.max(matrix).item()],
         'min': [np.min(matrix, axis=0).tolist(),
            np.min(matrix, axis=1).tolist(),
          np.min(matrix).item()],
        'sum': [np.sum(matrix, axis=0).tolist(),
            np.sum(matrix, axis=1).tolist(),
          np.sum(matrix).item()],


      }

    return calculations
