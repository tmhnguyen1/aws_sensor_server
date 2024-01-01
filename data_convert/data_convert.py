#!/usr/bin/python3
import pandas as pd
import pickle
import os
import shutil

def extract_sensor_data(input_folder, csv_output_path, pkl_output_path):
    pkl_files = []
    os.makedirs(pkl_output_path, exist_ok=True)
    os.makedirs(csv_output_path, exist_ok=True)
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.pkl'):
            pkl_files.append(os.path.join(input_folder, file_name))
    pkl_files = sorted(pkl_files)

    sensor_data = {
        'gyroscope': [],
        'accelerometer': [],
        'location': [],
        'barometer': [],
        'accelerometeruncalibrated': [],
        'annotation': [],
        'gravity': [],
        'gyroscopeuncalibrated': [],
        'magnetometer': [],
        'magnetometeruncalibrated': [],
        'matadata': [],
        'orientation': []
    }

    sensor_names = [
        'gyroscope',
        'accelerometer',
        'location',
        'barometer',
        'accelerometeruncalibrated',
        'annotation',
        'gravity',
        'gyroscopeuncalibrated',
        'magnetometer',
        'magnetometeruncalibrated',
        'matadata',
        'orientation'
    ]

    for pkl_file in pkl_files:
        try:
            with open(pkl_file, 'rb') as file:
                data = pickle.load(file)

            if isinstance(data, str):
                data = eval(data)
                
            for item in data:
                item_name = item['name']
                if item_name in sensor_names:
                    item_values = item['values']
                    time_value = item['time']
                    item_values['time'] = time_value
                    sensor_data[item_name].append(item_values)
            shutil.move(pkl_file, os.path.join(pkl_output_path, os.path.basename(pkl_file)))
        except (EOFError, pickle.UnpicklingError):
            print(f"Failed to load data from {pkl_file}")
            
    last_file = pkl_file.split("/")[-1].split(".")[0][-26:]
    print('last_file', last_file)
    os.makedirs(csv_output_path + f'/{last_file}', exist_ok=True)
    for sensor_name, sensor_values in sensor_data.items():
        sensor_df = pd.DataFrame(sensor_values)
        sensor_df.to_csv(csv_output_path + f'/{last_file}/{sensor_name.capitalize()}.csv', index=False)

    return sensor_data


if __name__ == '__main__':
    parent_input_folder = os.path.abspath(os.path.dirname(__file__)) + '/data/data_raw/'
    
    for root, dirs, files in os.walk(parent_input_folder):
        # print('root', root)
        # print(' files', files[:1])
        if len(files):
            csv_output_path = root.replace('data_raw', 'data_csv')
            pkl_output_path = root.replace('data_raw', 'data_pkl')
            print(' csv', csv_output_path)
            print(' pkl', pkl_output_path)
            extract_sensor_data(root, csv_output_path, pkl_output_path)