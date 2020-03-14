from keras.engine.saving import load_model

from preprocessing.preprocessing import input_data_test_set, target_data_test_set, label_list

if __name__ == '__main__':
    model = load_model('model.h5')
    test_acc, test_loss = model.evaluate(input_data_test_set, target_data_test_set, batch_size=128, verbose=0)
    predicts = model.predict(input_data_test_set)
    print(test_acc, test_loss)


    for i in predicts:
        index = 0
        for k in i:
            predict_max = max(i)
            if k != predict_max:
                index += 1
            else:
                break
        print('result:' + label_list[index], 'predict:' + str(max(i)))

