from tkinter.filedialog import test
import requests
import helper
import object
from elasticsearch import Elasticsearch
import re


def pretty_print_json(res, max=10):
    i = 0
    for r in res:
        if i <= max:
            pretty_r = json.dumps(r, indent=4, sort_keys=True)
            print(pretty_r)
            i += 1
        else:
            break

# def get_one_group_stats_v1(url: str, group_id: str, time_range: str) -> tuple:
    # URL = url
    # PARAMS = {
    #     "query": {
    #         "range": {
    #             "T": {
    #                 "gte": "now-1d/d",
    #                 "lte": "now/d"
    #             }
    #         }
    #     }
    # }
    # HEADER = {'Content-Type': 'application/json',
    #           'Accept': "application/json"}
    # r = requests.post(url=URL + "/" + group_id + "/_search",
    #                   data=json.dumps(PARAMS), headers=HEADER)
    # # res = json.dumps(r.json(), indent=4, sort_keys=True)
    # res = r.json()['hits']['hits']
    # for r in res:
    #     pretty_r = json.dumps(r.json(), indent=4, sort_keys=True)
    #     print(pretty_r)
    # print(len(res))
    # return

def add_data(from_list, to_list):
    for item in from_list:
        to_list.append(item)
    return

def query_group_logs_relative_time(url: str, port: int, group_id: str) -> list:
    es = Elasticsearch(hosts=url, port=port)

    PARAMS = {
      "size": 1000, 
      "query": {
        "range": {
          "T": {
            "gte": "now-168h",
            "lt": "now"
          }
        }
      }
    }

    all_data = []
    res = es.search(body=PARAMS, index=group_id, _source=True, _source_includes=['CID', 'T', 'QH', 'GID', 'QT'], scroll='1m')
    scroll_id = res['_scroll_id']
    scroll_size = len(res['hits']['hits'])
    
    while scroll_size > 0:
        add_data(res['hits']['hits'], all_data)
        res = es.scroll(scroll_id=scroll_id, scroll = '1m')
        scroll_id = res['_scroll_id']
        scroll_size = len(res['hits']['hits'])

    return all_data

def get_time_use_one_group(url: str, port: int, group_id: str):
  group_logs = query_group_logs_relative_time(url=url, port=port, group_id=group_id)
  new_group = object.Group(group_logs)
  new_group.load_group_logs()

  group_app_record = object.create_empty_app_record()
  group_cate_record = object.create_empty_cate_record()

  for device in new_group.get_device_list().values():
    device_app_record = object.create_empty_app_record()
    device_cate_record = object.create_empty_cate_record()
    for date in device.get_querylog_by_date():

      """
      1) for a given day, what apps are used during each interval?
      e.g.: interval_all_app = {129:['fb_and_messenger', 'shopee]
                                130:['fb_and_messenger', 'instagram'],...}
      """
      interval_all_app = {}
      for cate in object.category_map_app:
        for app in object.category_map_app[cate]:
          app_request = device.get_app_query_using_rx(device.get_querylog_by_date()[date], rx_use = app['regex'])
          app_interval = helper.get_num_rq_by_interval(app_request)
          f_app_interval = dict(sorted(helper.filter_intensity_by_threshold(app_interval, app['i']).items()))
          helper.insert_app_use_to_interval(app['name'], f_app_interval, interval_all_app)
      interval_all_app = dict(sorted(interval_all_app.items()))
      
      """
      2) for each app, what is the use ratio of the app in each interval? 
      e.g.: ratio_app_res = {'instagram': {130: 0.5, 131: 1.0, 132: 0.33}, 
                                "shopee': {129: 0.5},...}
      """
      ratio_app_res = {}
      for cate in object.category_map_app:
        for app in object.category_map_app[cate]:
          ratio_app_res[app['name']] = {}
          for interval in interval_all_app:
            if app['name'] in interval_all_app[interval]:
              val = 1/(len(interval_all_app[interval]))
              ratio_app_res[app['name']][interval] = val

      """
      3) for each app, calculate actual time use (in regards of maybe multiple apps are used in one interval)
      e.g.: 
      """
      for app in ratio_app_res:
        app_object = object.get_app_dict_by_name(app)
        app_time = helper.get_app_use_time(ratio_app_res[app], ctn_threshold=app_object['c'])
        for itv in ratio_app_res[app]:
          t = ratio_app_res[app][itv]
          if t < 1:
            app_time = app_time - (1-t)

        device_app_record[app_object['name']] += app_time
        device_cate_record[app_object['category']] += app_time
        group_app_record[app_object['name']] += app_time
        group_cate_record[app_object['category']] += app_time

    device.get_record().update_app_stats_time(device_app_record)
    device.get_record().update_category_stats_time(device_cate_record)
    
    new_group.get_group_record().update_app_stats_time(group_app_record)
    new_group.get_group_record().update_category_stats_time(group_cate_record)
      
  return new_group

def get_time_use_multiple_groups(url: str, port: int, groups_list: list):
  return 

if __name__ == "__main__":
  elk_address = "http://103.192.236.108"
  test_group = "group-visafe"
  port = 9200
  
  # get_time_use_one_group(elk_address, port, test_group)
  new_group = get_time_use_one_group(url=elk_address, port = port, group_id=test_group)
  print(new_group.get_group_record().get_category_stats_time())
  print(new_group.get_group_record().get_app_stats_time())

