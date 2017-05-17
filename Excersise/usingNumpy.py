import numpy as np

def split_inputs_by_category(givenArray, condition):
  return [givenArray[condition], givenArray[~condition]]

X = np.array([[1, -0.8, 0.832],
    [1, 0.3571, 0.85090],
    [1, -0.75, -0.74343],
    [1, -0.3, 0.12545],
    [1, 0.83465567, 0.62434554],
    [1, -0.02, 0.9200034354],
    [1, 0.104365545, -0.3243566757],
    [1, 0.00007143, 0.073278437e3]])
y = np.array([0, 0, 0, 0, 1, 1, 1,1])
x_neg,x_pos  = split_inputs_by_category(X, y[:, ] == 0)
print (x_neg)
print (x_pos)