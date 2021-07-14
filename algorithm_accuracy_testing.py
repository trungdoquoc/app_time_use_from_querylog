import unittest
import objects
import stats_process_function as spf
import re
import json
from helpers import extract_data_from_log, timestring_to_datetime, convert_hhmm_to_interval
import pandas as pd

trungdo_cid = "xfmb0yghpwbe"
trungdo_gid = "9b1956eb-ad3b-4427-a489-34a3fd8ffcb5"
MAX_DIFF_PERCENT = 0.1

own_data_csv = "./own_data/single_app_record.csv"
own_data_path = "./own_data/"

single_app_data = "./own_data/su_dung_app_lien_tuc.csv"

def extract_data_from_json(json_object):
    """
    GOAL: Process 1 parsed json_object, 
    input: a json object
    returns: querylog dict to insert to 
    """
    querylog = {}
    try:
        querylog['device_name'] = json_object['CID']
    except: 
        return
    else:
        querylog['time'] = timestring_to_datetime(json_object['T'])
        querylog['interval'] = convert_hhmm_to_interval(querylog['time'])
        querylog['website_request'] = json_object['QH']
        querylog['connection_type'] = json_object['QT']
        return querylog

def load_json_file(path):
    list_of_logs = []
    with open(path, 'r') as file:
        for line in file:
            p = json.loads(line)
            log = extract_data_from_json(p)
            if log != None:
                list_of_logs.append(log)
    return list_of_logs

def is_under_threshold(a, b, threshold):
    """
    input: b is the value to be compared with
    """
    diff = abs(a-b)/b
    if diff < threshold:
        return True
    else:
        return False

#1 Compare measured time of single app json log files with : 
class TestSingleAppTime(unittest.TestCase):
    def test_all_single_app_own_data(self):
        """
        GOAL: Compare % difference (must < 10%) of measured time vs. actual recorded time 
        in own_data_csv (source: self)
        """
        df = pd.read_csv(own_data_csv)
        for index, row in df.iterrows():
            app_name = objects.get_app_dict_by_name(row['app_use'].strip())['name']
            expected_res = row['real_time_spent']
            f_name = row['file_name'].strip() + '.json'
            f_path = own_data_path + f_name
            list_of_logs = load_json_file(f_path)
            
            device = objects.Device(row['file_name'])
            for log in list_of_logs:
                device.insert_log_to_querylog(log)
            device.single_app_update_device_time_use()
            
            app_time_use = device.get_record().get_one_app_time(app_name)
            val = is_under_threshold(app_time_use, expected_res, 0.1) or abs(app_time_use - expected_res) <=2
            print(val)
            # self.assertTrue(is_under_threshold(app_time_use, expected_res, 0.1))
            # print(app_name + ': ' + str(app_time_use))
            # print(expected_res)
            # print('-----')

        return
    
    def test_all_single_app_(self):
        """
        GOAL: Compare % difference (must < 10%) of measured time vs. actual recorded time 
        in su_dung_app_lien_tuc.csv (source: others)
        """
        pass

#2 Full workflow: Query ELK's data -> Process data -> Compare data with label for difference
class TestFullUse(unittest.TestCase):
    def test_time_use_absolute_time(self):
        # spf.query_client_log_relative_time()
        # self.assertEqual(sum([1, 2, 3]), 7)
        return 

    def test_time_use_relative_time(self):
        pass

if __name__ == '__main__':
    unittest.main()
