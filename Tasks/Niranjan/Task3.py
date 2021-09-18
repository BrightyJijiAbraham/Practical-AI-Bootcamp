# -*- coding: utf-8 -*-
"""practicalAI-Niranjan-Task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/itsniranjan/Practical-AI-Bootcamp/blob/main/Tasks/Niranjan/practicalAI_Niranjan_Task1.ipynb
"""

!pip install tensorflow_text

import tensorflow as tf

#import tensorflow_text
import tensorflow_text as tf_text

directory_url = 'https://storage.googleapis.com/download.tensorflow.org/data/illiad/'
file_names = ['cowper.txt', 'derby.txt', 'butler.txt']

file_paths = [
    tf.keras.utils.get_file(file_name, directory_url + file_name)
    for file_name in file_names
]

dataset = tf.data.TextLineDataset(file_paths)

#convert to utf8

dataset_utf8=map(lambda str:tf_text.normalize_utf8(str), dataset)

for data in dataset_utf8:
  print(data.numpy())