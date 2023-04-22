import numpy as np


def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  else:
    oldArr = np.array(list)
    arr = oldArr.reshape(3, 3)

    calculations = {
      "mean": [
        np.mean(arr, axis=0).tolist(),
        np.mean(arr, axis=1).tolist(),
        np.mean(oldArr)
      ],
      "variance": [
        np.var(arr, axis=0).tolist(),
        np.var(arr, axis=1).tolist(),
        np.var(oldArr)
      ],
      "standard deviation": [
        np.std(arr, axis=0).tolist(),
        np.std(arr, axis=1).tolist(),
        np.std(oldArr)
      ],
      "max": [
        np.max(arr, axis=0).tolist(),
        np.max(arr, axis=1).tolist(),
        np.max(oldArr)
      ],
      "min": [
        np.min(arr, axis=0).tolist(),
        np.min(arr, axis=1).tolist(),
        np.min(oldArr)
      ],
      "sum": [
        np.sum(arr, axis=0).tolist(),
        np.sum(arr, axis=1).tolist(),
        np.sum(oldArr)
      ]
    }

    return calculations
