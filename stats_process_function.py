import objects
from config import url, port
from elasticsearch import Elasticsearch
import datetime

def pretty_print_json(res, max=10):
	i = 0
	for r in res:
		if i <= max:
			pretty_r = json.dumps(r, indent=4, sort_keys=True)
			print(pretty_r)
			i += 1
		else:
			break

def add_data(from_list, to_list):
	for item in from_list:
		to_list.append(item)
	return

def query_client_log_absolute_time(group_id: str, client_id: str, time_from, time_to) -> list:
	"""
	inputs: 
	default timezone: UTC +07:00 Indochina Time (ICT)
	time_from, time_to: timestring yyyy-mm-ddThh-mm-ss (no Z)
	e.g.: 2021-07-05T00:00:00
	"""
	es = Elasticsearch(hosts=url, port=port)
	PARAMS = {
		"size": 1000,
		"query": {
			"bool": {
				"filter": [
					{"term": {"CID": client_id}},
					{"range": {"T": {
					  "time_zone": "+07:00",
					  "gte": time_from, 
					  "lte": time_to}}}
				]
			}
		}
	}

	all_data = []
	res = es.search(body=PARAMS, index=group_id, _source=True, _source_includes=[
					'CID', 'T', 'QH', 'GID', 'QT'], scroll='1m')

	return

def query_client_logs_relative_time(group_id: str, client_id: str) -> list:
	"""
	default: relative time is (24 hours - now)
	"""
	es = Elasticsearch(hosts=url, port=port)

	PARAMS = {
		"size": 1000,
		"query": {
			"bool": {
				"filter": [
					{"term": {"CID": client_id}},
					{"range": {"T": {"gte": "now-24h", "lt": "now"}}}
				]
			}
		}
	}
	all_data = []
	res = es.search(body=PARAMS, index=group_id, _source=True, _source_includes=[
					'CID', 'T', 'QH', 'GID', 'QT'], scroll='1m')
	scroll_id = res['_scroll_id']
	scroll_size = len(res['hits']['hits'])

	while scroll_size > 0:
		add_data(res['hits']['hits'], all_data)
		res = es.scroll(scroll_id=scroll_id, scroll='1m')
		scroll_id = res['_scroll_id']
		scroll_size = len(res['hits']['hits'])

	return all_data

def query_group_logs_relative_time(group_id: str) -> list:
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
	res = es.search(body=PARAMS, index=group_id, _source=True, _source_includes=[
					'CID', 'T', 'QH', 'GID', 'QT'], scroll='1m')
	scroll_id = res['_scroll_id']
	scroll_size = len(res['hits']['hits'])

	while scroll_size > 0:
		add_data(res['hits']['hits'], all_data)
		res = es.scroll(scroll_id=scroll_id, scroll='1m')
		scroll_id = res['_scroll_id']
		scroll_size = len(res['hits']['hits'])

	return all_data

def query_workspace_logs_relative_time(group_list: list) -> list:
	"""
	Note: 
	1) group_list is a list of _index, not GID
	2) unecessary right now
	"""
	# all_data = 
	# for g_index in group_list:
	# 	g_data = query_group_logs_relative_time(url, port, g_index)
	pass

def get_time_use_one_client(group_id: str, client_id: str):
	client_logs = query_client_logs_relative_time(group_id=group_id, client_id=client_id)
	new_client = objects.Device(client_id)
	new_client.load_device_logs(client_logs)
	new_client.update_device_time_use()

	return new_client

def get_time_use_one_group(group_id: str):
	group_logs = query_group_logs_relative_time(
		url=url, port=port, group_id=group_id)
	new_group = objects.Group(group_logs, group_id)
	new_group.load_group_logs()

	# group_app_record = objects.create_empty_app_record()
	# group_cate_record = objects.create_empty_cate_record()

	for device in new_group.get_device_list().values():
		device.update_device_time_use()
		new_group.get_group_record().add_app_stats_time(device.get_record().get_app_stats_time())
		new_group.get_group_record().add_category_stats_time(device.get_record().get_category_stats_time())
	return new_group

def get_time_use_workspace(group_list: list):
	"""
	input: 
	group_list: list of _index
	"""
	new_workspace = objects.Workspace()

	for group_index in group_list:
		g_object = get_time_use_one_group(url, port, group_index)
		new_workspace.add_group_to_workspace(g_object)
		new_workspace.get_workspace_record().add_app_stats_time(g_object.get_group_record().get_app_stats_time())
		new_workspace.get_workspace_record().add_category_stats_time(g_object.get_group_record().get_category_stats_time())
	return new_workspace

if __name__ == "__main__":
# 	elk_address = "http://103.192.236.108"
	t_group = "group-visafe"
	t_client = "6v7yqf7zkeo0"
# 	t_workspace = ["group-9b1956eb-ad3b-4427-a489-34a3fd8ffcb5", "group-visafe"]
# 	port = 9200

	# I/ Absolute Time
	# time_from = 
	# time_to = 

	# II/ Relative Time
	# 1 CLIENT:
	new_client = get_time_use_one_client(t_group, t_client)
	# print(new_client.get_record().get_category_stats_time())
	print(new_client.get_record().get_app_stats_time())
	print(new_client.get_record().get_formatted_app_stats_time())

	# # 1 GROUP:
	# new_group = get_time_use_one_group(group_id=t_group)
	# print(new_group.get_group_record().get_category_stats_time())
	# print(new_group.get_group_record().get_app_stats_time())

	# # MULTIPLE GROUPS:
	# new_workspace = get_time_use_workspace(t_workspace)
	# print(new_workspace.get_workspace_record().get_category_stats_time())
	# print(new_workspace.get_workspace_record().get_app_stats_time())

