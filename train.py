import keras
import matplotlib.pyplot as plt
from model.dCNN_model import build_model
from preprocessing.preprocessing import input_data_train_set, target_data_train_set

if __name__ == '__main__':
    model = build_model()
    model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta(),
                  metrics=['accuracy'])

    history = model.fit(input_data_train_set, target_data_train_set, nb_epoch=12, batch_size=128)
    model.save("model.h5")

    print(history.history)
    plt.plot(history.history['accuracy'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train'], loc='upper left')
    plt.show()

    # 绘制训练 & 验证的损失值
    plt.plot(history.history['loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train'], loc='upper left')
    plt.show()