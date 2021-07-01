from helper import extract_data_from_log, datetime_to_dmy_datetime
import re

### social_network regex:
### filter (insta & fb & mess) regex -> filter just instagram -> filter just messenger
fb_mess_insta_rx = re.compile(r"(instagram|cdninstagram|fb\.com|fb\.me|fbsbx|fbcdn|facebook)")
insta_rx = re.compile(r"(instagram|cdninstagram)")
tiktok_rx = re.compile(r"(tiktok)|(tiktokcdn)|(musical)|(snssdk\.)|(amemv\.)|(toutiao)|(ixigua)|(pstatp\.)|(ixiguavideo)|(toutiaocloud)|(bdurl\.)|(bytecdn)|(byteimg)|(ixigua)|(muscdn)|(douyin)|(tiktokv)")

### movies regex:
netflix_rx = re.compile(r"(netflix|nflxext\.|nflximg\.|nflxso\.|nflxvideo\.)")
fptp_rx = re.compile(r"(fptplay)")

### messaging regex:
viber_rx = re.compile(r"(viber|nsone\.net)")
zalo_rx = re.compile(r"(zalo|zdn\.vn|zadn\.vn|zaloapp\.)")

### video regex:
yt_rx = re.compile(r"(youtube|ytimg\.com|youtu\.be|googlevideo|youtube-nocookie|yt3\.ggpht|video\.google)")

### music regex:
sc_rx = re.compile(r"(wave\.sndcdn|soundcloud)")
spotify_rx = re.compile(r"(spotify)|(scdn\.co)")
nct_rx = re.compile(r"(nixcdn|nhaccuatui)")
zingmp3_rx = re.compile(r"(zingmp3|zplayer-trk\.zdn|zmp3\.zadn|zplayer-trk\.zdn|zmp3-static\.zadn)")

### shopping regex:
tiki_rx = re.compile(r"(tiki|tikicdn)")
shopee_rx = re.compile(r"(shopee|asia\.creativecdn)")
lazada_rx = re.compile(r"(lazada|alicdn\.com)")

fb_and_mess_app = {
    'name': 'fb_and_messenger',
    'category': 'social_network', 
    'app_type': 'full_active',
    'regex': fb_mess_insta_rx, 
    'i': 4,
    'c': 3
}

instagram_app = {
    'name': 'instagram',
    'category': 'social_network',
    'app_type': 'full_active',
    'regex': insta_rx, 
    'i': 4,
    'c': 3
}

tiktok_app = {
    'name': 'tiktok',
    'category': 'social_network',
    'app_type': 'full_active',
    'regex': tiktok_rx, 
    'i': 2,
    'c': 3    
}

netflix_app = {
    'name': 'netflix',
    'category': 'movies',
    'app_type': 'full_active',
    'regex': netflix_rx, 
    'i': 2,
    'c': 10
}

fpt_play_app = {
    'name': 'fpt_play',
    'category': 'movies',
    'app_type': 'full_active',
    'regex': fptp_rx, 
    'i': 4,
    'c': 3
}

viber_app = {
    'name': 'viber',
    'category': 'messaging',
    'app_type': 'partial_active',
    'regex': viber_rx, 
    'i': 2,
    'c': 2
}

zalo_app = {
    'name': 'zalo',
    'category': 'messaging',
    'app_type': 'partial_active',
    'regex': zalo_rx, 
    'i': 2,
    'c': 2
}

youtube_app = {
    'name': 'youtube',
    'category': 'video',
    'app_type': 'full_active',
    'regex': yt_rx, 
    'i': 1,
    'c': 9
}

spotify_app = {
    'name': 'spotify',
    'category': 'music',
    'app_type': 'passive',
    'regex': spotify_rx, 
    'i': 1,
    'c': 5
}

zingmp3_app = {
    'name': 'zingmp3',
    'category': 'music',
    'app_type': 'passive',
    'regex': zingmp3_rx, 
    'i': 3,
    'c': 4
}

nhaccuatui_app = {
    'name': 'nhaccuatui',
    'category': 'music',
    'app_type': 'passive',
    'regex': nct_rx, 
    'i': 2,
    'c': 7
}

soundcloud_app = {
    'name': 'soundcloud',
    'category': 'music',
    'app_type': 'passive',
    'regex': sc_rx, 
    'i': 2,
    'c': 3
}

tiki_app = {
    'name': 'tiki',
    'category': 'shopping',
    'app_type': 'full_active',
    'regex': tiki_rx, 
    'i': 2,
    'c': 3
}

shopee_app = {
    'name': 'shopee',
    'category': 'shopping',
    'app_type': 'full_active',
    'regex': shopee_rx, 
    'i': 2,
    'c': 3
}

lazada_app = {
    'name': 'lazada',
    'category': 'shopping',
    'app_type': 'full_active',
    'regex': lazada_rx, 
    'i': 2,
    'c': 3
}

category_map_app = {
  'social_network': [fb_and_mess_app, instagram_app, tiktok_app],
  'movies': [netflix_app, fpt_play_app],
  'messaging': [viber_app, zalo_app],
  'video': [youtube_app],
  'music': [spotify_app, zingmp3_app, nhaccuatui_app, soundcloud_app],
  'shopping': [tiki_app, shopee_app, lazada_app]
}

category_app_mapping = {
  'social_network': ['fb_and_messenger', 'instagram', 'tiktok'],
  'movies': ['netflix', 'fpt_play'],
  'messaging': ['viber', 'zalo'],
  'video': ['youtube'],
  'music': ['spotify', 'zingmp3', 'nhaccuatui', 'soundcloud'],
  'shopping': ['tiki', 'shoppe', 'lazada']
}

def get_app_dict_by_name(app_name):
    for cat in category_map_app:
        for app in category_map_app[cat]:
            if  app_name == app['name'] :
                return app
    raise Exception('missing app dict for ' + app_name)

def create_empty_app_record():
    app_record = {}
    for cate in category_map_app:
        for app in category_map_app[cate]:
            app_record[app['name']] = 0
    app_record['other'] = 0
    return app_record

def create_empty_cate_record():
    cate_record = {}
    for cate in category_map_app:
        cate_record[cate] = 0
    cate_record['other'] = 0
    return cate_record

# class Workspace:
#     """
#     """
#     def __init__(self):
#         self.list_of_groups = {}

class Group:
    """
    A Group() object has # attributes: 
    #) group_name: string (GID)
    #) device_list: dict of Device() object
    #) group_logs: list of dict{logs}
    """
    #TODO: add group_name or group_id
    def __init__(self, group_logs):
        self.device_list = {}
        self.group_logs = group_logs
        self.group_record = Record()
    
    def get_device_list(self):
        return self.device_list
    
    def get_group_name(self):
        return

    def get_all_device_name(self):
        return list(self.device_list.keys())
    
    def get_group_logs(self):
        return self.group_logs

    def set_group_logs(self, group_logs):
        self.group_logs = group_logs
        return

    def set_group_name(self, new_name):
        self.group_name = new_name
        return
    
    def empty_group_logs(self):
        return self.group_logs.clear()

    def load_group_logs(self):
        for log in self.group_logs:
            extracted_log = extract_data_from_log(log)
            if extracted_log != None:
                d_name = extracted_log['device_name']
                if d_name in self.device_list:
                    self.device_list[d_name].insert_log_to_querylog(extracted_log)
                else:
                    new_device = Device(d_name)
                    new_device.insert_log_to_querylog(extracted_log)
                    self.device_list[d_name] = new_device
        self.empty_group_logs()
        return

    def get_group_record(self):
        return self.group_record

class Device:
    """
    A Device() object has # attributes:
    1) device_name: string (CID)
    2) group_id = string (GID)
    2) querylog_by_date: a dict of log dicts:
         key: datetime object(year, month, day)
         value: [list of logs {
            key0: device_name: string (CID)
            key1: time: datetime object (T)
            key2: group_id: string (GID)
            key4: website_request: string (QH)
            key5: connection_type: string (QT)}] #after data are extracted, delete after ### days.
            }
    3) record: a Record() object
    """
    def __init__(self, name):
        self.device_name = name
#         self.group_id = gid
        self.querylog_by_date = {}
        self.interval_by_date = {}
        self.record = Record()

    def get_device_name(self):
        return self.device_name
    
    def get_group_id(self):
        return self.group_id
    
    def get_querylog_by_date(self):
        return self.querylog_by_date

    def get_record(self):
        return self.record

    def insert_log_to_querylog(self, log):
        if self.device_name == log['device_name']:
            dmy = datetime_to_dmy_datetime(log['time'])
            try:
                self.querylog_by_date[dmy].append(log)
            except:
                self.querylog_by_date[dmy] = []
                self.querylog_by_date[dmy].append(log)
        else:
            raise Exception("Mismatch device_name")
        return

    def get_app_query_using_rx(self, querylog_list, rx_use):
        """
        GOAL: filter app from a specific date's querylog_list using the app's regex
        input: a list of dict.
        return: a list of dict
        """
        app_query = []
        for log in querylog_list:
            if rx_use.search(log['website_request']) != None:
                app_query.append(log)
        return app_query


class Record:
    """
    A Record() object has # attributes: 
    1) category_stats_percent: dict:
        key: category name (str)
        value: percentage out of 24hr (0 <= int <= 100)

    e.g.: {'social_network': 45, 
           'movies': 12, ...}

    2) app_stats_percent: dict:
        key: app name (str)
        value: percentage out of 24hr (0 <= int <= 100)

    e.g.: {'fb_and_messenger': 40, 'instagram' = 32, ...}
    """
    def __init__(self):
        self.app_stats_percent = {}
        self.category_stats_percent = {}
        
        self.app_stats_time = {}
        self.category_stats_time = {}
        
        for cate in category_map_app:
            self.category_stats_percent[cate] = 0
            self.category_stats_time[cate] = 0
        self.category_stats_percent['other'] = 0
        self.category_stats_time['other'] = 0
        
        for cate in category_map_app:
            for app in category_map_app[cate]:
                self.app_stats_percent[app['name']] = 0
                self.app_stats_time[app['name']] = 0
        self.app_stats_percent['other'] = 0
        self.app_stats_time['other'] = 0

    def get_category_stats_percent(self):
        return self.category_stats_percent

    def get_app_stats_percent(self):
        return self.app_stats_percent
    
    def get_category_stats_time(self):
        return self.category_stats_time

    def get_app_stats_time(self):
        return self.app_stats_time

    def set_one_category_percent(self, that_category, value):
        self.category_stats_percent[that_category] = value
        return 

    def set_one_app_percent(self, that_app, value):
        self.app_stats_percent[that_app] = value
        return
    
    def set_one_category_time(self, that_category, value):
        self.category_stats_time[that_category] = value
        return 

    def set_one_app_time(self, that_app, value):
        self.app_stats_time[that_app] = value
        return

    def update_app_stats_time(self, from_dict):
        self.app_stats_time = from_dict
        return

    def update_category_stats_time(self, from_dict):
        self.category_stats_time = from_dict
        return

    def add_category_stats_time(self, from_dict):
        for k in from_dict:
            self.category_stats_time[k] += from_dict[k]
        return 

    def add_app_stats_time(self, from_dict):
        for k in from_dict:
            self.app_stats_time[k] += from_dict[k]
        return


# if __name__ == "__main__":
#     t_record = Device("tdq")
#     print(create_empty_app_record())
#     print(create_empty_cate_record())