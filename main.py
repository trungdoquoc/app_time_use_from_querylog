from fastapi import FastAPI
import stats_process_function as spf

app = FastAPI()

@app.get("api/v1/client-stats")
def get_client_time_use(group_id: str, client_id: str):
    new_client = spf.get_time_use_one_client(group_id, client_id)
    client_cate_use = new_client.get_record().get_category_stats_time()
    client_app_use = new_client.get_record().get_formatted_app_stats_time()
    return {"client_category_use": client_cate_use, "client_app_use": client_app_use}


@app.get("api/v1/group-stats")
def get_group_time_use(group_id: str):
    new_group = spf.get_time_use_one_group(group_id)
    group_cate_use = new_group.get_group_record().get_category_stats_time()
    group_app_use = new_group.get_group_record().get_formatted_app_stats_time()
    return {"group_category_use": group_cate_use, "group_app_use": group_app_use}


