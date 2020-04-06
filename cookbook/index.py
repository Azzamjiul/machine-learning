import numpy as np
from sklearn.preprocessing import LabelBinarizer, MultiLabelBinarizer

feature = np.array([
    ['Texas'],['California'],['Texas'],['Delaware'],['Texas']
])

one_hot = LabelBinarizer()

print(one_hot.fit_transform(feature))