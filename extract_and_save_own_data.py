import objects
import helpers
import json

save_folder = "./own_data"

def format_json_log(json_log, session_name):
    querylog = {}
    querylog['CID'] = session_name
    querylog['T'] = json_log['T']
    querylog['QH'] = json_log['QH']
    querylog['QT'] = json_log['QT']
    querylog['interval'] = helpers.convert_hhmm_to_interval(helpers.datetime_to_dmy_datetime(json_log['T']))
    return querylog

def is_json_in_time_range(json_log, time_from, time_to):
    date_from = helpers.datetime_to_dmy_datetime(time_from)
    date_to = helpers.datetime_to_dmy_datetime(time_to)
    interval_from = helpers.convert_hhmm_to_interval(time_from)
    interval_to = helpers.convert_hhmm_to_interval(time_to)
    
    json_dt = helpers.datetime_to_dmy_datetime(json_log['T'])
    date = helpers.datetime_to_dmy_datetime(json_dt)
    json_log['interval'] = helpers.convert_hhmm_to_interval(json_dt)

    if date >= date_from and date <= date_to:
        if json_log['interval'] >= interval_from and json_log['interval'] <= interval_to:
            return True
    else:
        return False


def extract_and_save_data_from_json(input_file, session_name, time_from, time_to):
    """
    GOAL: Extract all json logs within the given time range, 
    then write into new json file.
    input: 
        input_file: (str) original json file
        output_file_name: (str) name for output file
        time_from: (datetime obj) y,m,d,h,min
        time_to: (datetime obj) y,m,d,h,min
    returns: None
    """
    
    # 1) Open from_file and to_file
    dest_path = save_folder + session_name + ".json"
    with open(input_file, "r") as from_file, open(dest_path, "w") as to_file:
        for line in from_file:
            p = json.loads(line)
            if is_json_in_time_range(p, time_from, time_to)==True:
                formatted_p = format_json_log(p, session_name)
                to_file.write(json.dumps(formatted_p))
                to_file.write("\n")
    return

if __name__ == "__main__":
    pass