import tensorflow as tf
import numpy as np
import os


class Classifier(tf.keras.Model):
    def __init__(self): # 32, 32, 3
        super().__init__()

        af = 'relu'

        self.mlayers = [
            tf.keras.layers.Conv2D(filters=8, kernel_size=(3, 3), padding='same', activation=af),
            tf.keras.layers.MaxPool2D(pool_size=(2, 2)), # 16, 16
            tf.keras.layers.Conv2D(filters=12, kernel_size=(3, 3), padding='same', activation=af),
            tf.keras.layers.MaxPool2D(pool_size=(2, 2)), # 8, 8
            tf.keras.layers.Conv2D(filters=16, kernel_size=(3, 3), padding='same', activation=af),
            tf.keras.layers.MaxPool2D(pool_size=(2, 2)), # 4, 4
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(256, activation=af),
            tf.keras.layers.Dense(128, activation=af),
            tf.keras.layers.Dense(10, activation='softmax')
        ]

        self.lossf = tf.keras.losses.SparseCategoricalCrossentropy()
        self(tf.zeros(shape=(1, 32, 32, 3), dtype=tf.dtypes.float32))

    def call(self, x):
        for i in range(len(self.mlayers)):
            x = self.mlayers[i](x)
        return x
    
    @tf.function(jit_compile=True)
    def fitstep(self, X, Y):
        with tf.GradientTape() as tape:
            out = self(X)
            loss = self.lossf(Y, out)

        g = tape.gradient(loss, self.trainable_variables)
        self.opt.apply_gradients(zip(g, self.trainable_variables))
        return loss
    
    def fit(self, dataset:tf.data.Dataset, batch_size:int, lr:float, epochs:int):
        self.opt = tf.keras.optimizers.Adam(lr)

        dataset = dataset.shuffle(buffer_size=10000)
        dataset = dataset.map(lambda x: {'id': x['id'], 'image': tf.cast(x['image'], tf.dtypes.float32), 'label': x['label']})
        totalnb = tf.data.Dataset.cardinality(dataset).numpy()//batch_size

        for ep in range(1, epochs+1, 1):
            for nbatch, batch in enumerate(dataset.batch(batch_size)):
                print(f'Epoca: {ep}/{epochs} - Lote: {nbatch+1}/{totalnb} - Loss: {self.fitstep(batch["image"], batch["label"])}')
            print()