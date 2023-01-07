import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError('List must contain nine numbers.')
  matrix = np.array(list).reshape((3,3))
  calculations = {}

  #Calculating mean of elements along all rows
  calculations['mean'] = [np.mean(matrix, axis = 0).tolist(), np.mean(matrix, axis = 1).tolist(), np.mean(matrix).tolist()]

  #Calculating median along all rows 
  calculations['variance'] = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix.tolist())]


  #Caculating standard deviation along all rows
  calculations['standard deviation'] = [np.std(matrix, axis = 0).tolist(), np.std(matrix, axis = 1).tolist(), np.std(matrix.tolist())]

  #calculating maximum of all individual rows
  calculations['max'] = [np.max(matrix, axis = 0).tolist(), np.max(matrix, axis = 1).tolist(), np.max(matrix.tolist())]

  #Calculating minimum of all individual rows
  calculations['min'] = [np.min(matrix, axis = 0).tolist(), np.min(matrix, axis = 1).tolist(), np.min(matrix.tolist())]

  #Calculating sum of elements of all individual rows
  calculations['sum'] = [np.sum(matrix, axis = 0).tolist(), np.sum(matrix, axis = 1).tolist(), np.sum(matrix.tolist())]



  return calculations
