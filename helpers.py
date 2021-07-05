import json
import pytz
import re
import dateutil.parser
from datetime import datetime, timedelta

def datetime_to_dmy_datetime(datetime_obj):
    """
    GOAL: Set a datetime object's hour, min, seconds = 0 
    """
    dt = datetime_obj.replace(hour = 0, minute = 0, second = 0)
    return dt

def datetime_to_dmy_string(datetime_obj):
    """
    GOAL: Convert a datetime object to dd/mm/YYYY string
    """
    return datetime_obj.strftime('%d-%m-%Y')

def datetime_hour_to_hour_format(datetime_obj):
    """
    GOAL: Convert a datetime object's hour to hh:00 string
    """
    return datetime_obj.strftime('%H:00')

def timestring_to_datetime(time_string, vn_tz = True):
    """
    GOAL: Convert ISO 8601 time string to 
    datetime object.
    (UPDATE: if vn_tz == False, convert time_string to UTC 
             else, convert to local Vietnam timezone)
    input: ISO 8601 time string
    return: datetime() object
    """
    utc_tz = pytz.utc
    vn_tz = pytz.timezone('Asia/Ho_Chi_Minh')
    dt = dateutil.parser.parse(time_string)
    utc_dt = dt.astimezone(utc_tz).replace(microsecond = 0)
    
    if vn_tz == False:
        return utc_dt
    
    else: #convert to Vietnam timezone
        return utc_dt.astimezone(vn_tz)

def convert_hhmm_to_interval(datetime_obj):
    """
    GOAL: Given a datetime object, return its
    interval in the 24-hr day.
    e.g.: 14:48 -> 888
    """
    interval = datetime_obj.hour * 60 + datetime_obj.minute
    return interval

def extract_data_from_log(json_object: dict) -> dict:
    """
    GOAL: Process 1 parsed json_object, 
    input: a json object
    returns: querylog dict to insert
    """
    json_object = json_object['_source']
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


def get_insta_and_fb_query_using_rx(querylog_list):
    """
    GOAL: filter app from a specific date's querylog_list using the app's regex
    input: a list of dict.
    return: a tuple(insta, fb)
    """
    fb_and_insta_query = []
    insta_query = []
    fb_query = []
    for log in querylog_list:
        if fb_and_insta_rx.search(log['website_request']) != None:
            if insta_rx.search(log['website_request']) != None:
                insta_query.append(log)
            else: 
                fb_query.append(log)
    return (insta_query, fb_query)

def get_num_rq_by_interval(json_list):
    """
    GOAL: Given a json_list *sorted by day*, return a dict
    {key: interval, value: number of request in the interval}
    NOTE: The input json_list is filtered by category/app/website type.
    input: a json list
    returns: a dict
    """
    rq_amount_each_interval = {}

    for i in json_list:
        try:
            rq_amount_each_interval[i['interval']] += 1
        except:
            rq_amount_each_interval[i['interval']] = 0
            rq_amount_each_interval[i['interval']] += 1

    return rq_amount_each_interval

def get_delta_between_interval(interval_dict):
    """
    GOAL: from the filtered dict {interval: # of fb requests}, return list2 ONLY:
    ==> list 2): delta_in_min(list1[i], list1[i-1]). Always has 1 element less than len(list1)
    input: guarantee a list with >= 2 elements 
    
    --> min of len(list1) == 1 AND min of len(list2) == 1 (== 1 is when len(list1)==1 and list2's only element with be 1 minutes)
    """
    delta_interval = []
    itv = list(interval_dict.keys())
    
    for i in range(1, len(itv)):
        delta = itv[i] - itv[i-1]
        delta_interval.append(delta)
    return delta_interval

def filter_intensity_by_threshold(app_rq_per_interval, threshold_type):
    filtered_app_rq = {}
    for i in app_rq_per_interval:
        if app_rq_per_interval[i] >= threshold_type:
            filtered_app_rq[i] = app_rq_per_interval[i]
    return filtered_app_rq

# ULTIMATE FUNCTION: From dict {interval: # of request} of a single day, get time use app
def get_app_use_time(app_rq_per_interval, ctn_threshold):
    """
    GOAL: from a dict {interval: # of request} in a day,
    calculate time spent on app.
    input: a dict of {interval: # of request}
    output: int (total time using facebook per day)
    """
    total_app_time = 0
    ### NEW: Filter by intensity is done before this function

    if len(app_rq_per_interval) == 0:
        return total_app_time
    
    elif len(app_rq_per_interval) == 1:
        return 1
    
    else:
        # Filter interval range by continuity threshold
        delta_interval = get_delta_between_interval(app_rq_per_interval)
        if len(delta_interval) == 1:
            if delta_interval[0] <= ctn_threshold:
                total_app_time += delta_interval[0] + 1
            else:
                total_app_time = 2
            return total_app_time
        else:
            helper_count = 0
            for i in delta_interval:
                if i <= ctn_threshold:
                    helper_count += i
                else: 
                    helper_count += 1

            total_app_time = helper_count + 1
            return total_app_time

def insert_app_use_to_interval(app_name, from_dict, to_dict):
    for i in from_dict:
        try:
            to_dict[i].append(app_name)
        except:
            to_dict[i] = []
            to_dict[i].append(app_name)
    return 