import tensorflow as tf
import numpy as np
import pandas as pd
from utils.data_processing import *

"""
Модель: 
inputs = tf.keras.layers.Input(10)
x = tf.keras.layers.Dense(128, kernel_initializer=tf.keras.initializers.HeUniform())(inputs)
x = tf.keras.layers.Dense(64, kernel_initializer=tf.keras.initializers.HeUniform(), activation='relu')(x)
x = tf.keras.layers.Dense(64, kernel_initializer=tf.keras.initializers.HeUniform(), activation='relu')(x)
x = tf.keras.layers.Dense(32, kernel_initializer=tf.keras.initializers.HeUniform(), activation='relu')(x)
out = tf.keras.layers.Dense(1, kernel_initializer=tf.keras.initializers.HeUniform())(x)
model = tf.keras.Model(inputs, out)
"""


def read_model_h5(h5_path):
    """
    Чтение сохраненной модели
    :param h5_path: путь до h5 файла модели
    :return: tf.keras.model
    """
    return tf.keras.models.load_model(h5_path)


def read_normalized_test_data(test_data_path):
    """
    Чтение тестовых данных в pandas (только нормализованные от 0 до 1)
    :param test_data_path: путь до csv файла
    :return: x_data, y_data: list, x_data - список входных данных, y_data - список выходных данных
    """
    test_df = pd.read_csv(test_data_path, delimiter=";")
    return convert_df_to_list(test_df)


def read_second_normalized_data(test_data_path):
    """
    Чтение тестовых данных из второго пункта в pandas (только нормализованные от 0 до 1)
    :param test_data_path: путь до csv файла
    :return: x_data, y_data: list, x_data - список входных данных, y_data - список выходных данных
    """
    test_df = pd.read_csv(test_data_path, delimiter=";")
    return convert_second_df_to_list(test_df)


def run_predictions(input_data, model):
    """
    предсказание на тестовых данных
    :param input_data: лист входных данных
    :param model: tf.keras.model
    :return: список предсказаний
    """
    return model.predict(input_data)


def print_predicted_and_true_data(predicted, true):
    """
    Просто вывод 2 чисел: предсказанное и истинное
    :param predicted: лист с предсказанными значениями
    :param true: лист с истинными значениями
    """
    for i in range(len(true)):
        print("Predicted: " + str(np.round(predicted[i][0] * (8.82 - 0.0) + 0.0, 2)) + "; True: " + str(
            np.round(true[i] * (8.82 - 0.0) + 0.0, 2)))


def predictions_processing(predicted):
    """
    немного преобразований предскеазанных данных:
    1) Приведение к значениям от 0 до 1
    2) Округление до 2 знаков
    :param predicted: лист с предсказанными значениями
    :return: лист с преобразованными значениями предсказанных величин
    """
    return np.clip(predicted, 0.0, 1.0)


def MAE(predicted, true):
    err_sum = 0
    for i in range(len(true)):
        pred_val = np.round(predicted[i][0] * (8.82 - 0.0) + 0.0, 2)
        true_val = np.round(true[i] * (8.82 - 0.0) + 0.0, 2)
        err_sum += np.abs(pred_val - true_val)
    print("MAE: " + str(np.round((err_sum / len(true)), 4)))


if __name__ == "__main__":
    h5_model = read_model_h5("test_second_normalized.h5")
    # x_data, y_data = read_normalized_test_data("data/splitted/cropped/cropped_csv/test_normalized.csv") # - первый пункт
    x_data, y_data = read_second_normalized_data("data/splitted/cropped/cropped_csv/test_second_normalized.csv")  # - второй
    prediction_result = run_predictions(x_data, h5_model)
    processed_result = predictions_processing(prediction_result)
    print_predicted_and_true_data(processed_result, y_data)
    MAE(processed_result, y_data)
