import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model

# 生成随机梯度数据
def generate_gradients(num_samples, num_features):
    return np.random.rand(num_samples, num_features)

# 自编码器梯度降维
def autoencoder_gradient_reduction(gradients, encoding_dim):
    input_dim = gradients.shape[1]
    input_layer = Input(shape=(input_dim,))
    encoded = Dense(encoding_dim, activation='relu')(input_layer)
    decoded = Dense(input_dim, activation='linear')(encoded)
    autoencoder = Model(input_layer, decoded)
    autoencoder.compile(optimizer='adam', loss='mean_squared_error')
    autoencoder.fit(gradients, gradients, epochs=50, batch_size=32, shuffle=True, verbose=0)
    encoder = Model(input_layer, encoded)
    reduced_gradients = encoder.predict(gradients)
    return reduced_gradients, encoder

# 生成梯度数据
num_samples = 1000
num_features = 50
gradients = generate_gradients(num_samples, num_features)

# 梯度降维
encoding_dim = 10
reduced_gradients, encoder = autoencoder_gradient_reduction(gradients, encoding_dim)

# 打印降维结果和编码器摘要
print("降维后的梯度数据：")
print(reduced_gradients)
print("\n编码器摘要：")
encoder.summary()
