import numpy as np
 

time = np.arange(0, 100, 1)
values = np.sin(0.1 * time) + 0.1 * np.random.randn(100)


print(values[:10])


seq_length = 10  # Length of input sequences
X, y = [], []

for i in range(len(values) - seq_length):
    seq = values[i:i + seq_length]
    label = values[i + seq_length]
    print('sq',seq,'lab',values[i + seq_length])
    print(label)
    X.append(seq)
    y.append(label)

X = np.array(X)
y = np.array(y)





