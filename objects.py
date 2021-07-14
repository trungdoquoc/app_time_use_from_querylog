import helpers
import re

cur_frontend_response = [
        {
            "apps": [
                {
                    "count": 0,
                    "name": "zalo"
                },
                {
                    "count": 0,
                    "name": "fb_and_messenger"
                },
                {
                    "count": 0,
                    "name": "twitter"
                },
                {
                    "count": 0,
                    "name": "instagram"
                },
                {
                    "count": 0,
                    "name": "ok"
                },
                {
                    "count": 0,
                    "name": "vk"
                },
                {
                    "count": 0,
                    "name": "reddit"
                },
                {
                    "count": 0,
                    "name": "tiktok"
                },
                {
                    "count": 0,
                    "name": "9gag"
                },
                {
                    "count": 0,
                    "name": "weibo"
                }
            ],
            "count": 0,
            "name": "social_network"
        },
        {
            "apps": [
                {
                    "count": 0,
                    "name": "epicgames"
                },
                {
                    "count": 0,
                    "name": "steam"
                },
                {
                    "count": 0,
                    "name": "origin"
                },
                {
                    "count": 0,
                    "name": "blizzard"
                },
                {
                    "count": 0,
                    "name": "leagueoflegends"
                },
                {
                    "count": 0,
                    "name": "minecraft"
                }
            ],
            "count": 0,
            "name": "game"
        },
        {
            "apps": [
                {
                    "count": 0,
                    "name": "netflix"
                },
                {
                    "count": 0,
                    "name": "hulu"
                },
                {
                    "count": 0,
                    "name": "disneyplus"
                },
                {
                    "count": 0,
                    "name": "primevideo"
                },
                {
                    "count": 0,
                    "name": "fptplay"
                },
                {
                    "count": 0,
                    "name": "galaxyplay"
                }
            ],
            "count": 0,
            "name": "movie"
        },
        {
            "apps": [
                {
                    "count": 0,
                    "name": "tinder"
                }
            ],
            "count": 0,
            "name": "dating"
        },
        {
            "apps": [
                {
                    "count": 0,
                    "name": "discord"
                },
                {
                    "count": 0,
                    "name": "viber"
                },
                {
                    "count": 0,
                    "name": "wechat"
                },
                {
                    "count": 0,
                    "name": "snapchat"
                },
                {
                    "count": 0,
                    "name": "whatsapp"
                },
                {
                    "count": 0,
                    "name": "telegram"
                },
                {
                    "count": 0,
                    "name": "skype"
                }
            ],
            "count": 0,
            "name": "messaging"
        },
        {
            "apps": [
                {
                    "count": 0,
                    "name": "vimeo"
                },
                {
                    "count": 0,
                    "name": "dailymotion"
                },
                {
                    "count": 0,
                    "name": "youtube"
                },
                {
                    "count": 0,
                    "name": "twitch"
                }
            ],
            "count": 0,
            "name": "video"
        },
        {
            "apps": [
                {
                    "count": 0,
                    "name": "spotify"
                },
                {
                    "count": 0,
                    "name": "nhaccuatui"
                },
                {
                    "count": 0,
                    "name": "zingmp3"
                },
                {
                    "count": 0,
                    "name": "soundcloud"
                }
            ],
            "count": 0,
            "name": "music"
        },
        {
            "apps": [
                {
                    "count": 0,
                    "name": "ebay"
                },
                {
                    "count": 0,
                    "name": "amazon"
                },
                {
                    "count": 0,
                    "name": "tiki"
                },
                {
                    "count": 0,
                    "name": "lazada"
                },
                {
                    "count": 0,
                    "name": "shopee"
                }
            ],
            "count": 0,
            "name": "shopping"
        }
    ]
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
    'i': 3,
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
    'category': 'movie',
    'app_type': 'full_active',
    'regex': netflix_rx, 
    'i': 2,
    'c': 10
}

fpt_play_app = {
    'name': 'fpt_play',
    'category': 'movie',
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
  'game': [], 
  'movie': [netflix_app, fpt_play_app],
  'dating': [], 
  'messaging': [viber_app, zalo_app],
  'video': [youtube_app],
  'music': [spotify_app, zingmp3_app, nhaccuatui_app, soundcloud_app],
  'shopping': [tiki_app, shopee_app, lazada_app]
}

current_frontend = {
  'social_network': ['facebook','twitter','instagram','reddit','tiktok','9gag','weibo'],
  'game': ['epicgames','steam','origin','blizzard','leagueoflegends','minecraft'],
  'movies': ['netflix','fpt_play','hulu','disneyplus','primevideo','galaxyplay'],
  'dating': ['tinder'],
  'messaging': ['zalo','discord','viber','wechat','snapchat','whatsapp','telegram','skype'],
  'video': ['vimeo','dailymotion','youtube','twitch'],
  'music': ['spotify', 'zingmp3', 'nhaccuatui', 'soundcloud'],
  'shopping': ['ebay', 'amazaon', 'tiki', 'shoppe', 'lazada']
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

class Workspace:
    """
    A Workspace() object has # attributes: 
    #) group_list: dict{group_id: Group() objects belong to the Workspace}
    #) workspace_record: a Record() object
    """
    def __init__(self):
        self.group_list = {}
        self.workspace_record = Record()

    def add_group_to_workspace(self, group_object):
        self.group_list[group_object.get_group_id()] = group_object
        return 
        
    def get_workspace_record(self):
        return self.workspace_record

class Group:
    """
    A Group() object has # attributes: 
    #) group_id: string (_index)
    #) device_list: dict of Device() object
    #) group_logs: list of dict{logs}
    #) group_record: a Record() object
    """
    def __init__(self, group_logs, group_id):
        self.group_id = group_id
        self.device_list = {}
        self.group_logs = group_logs
        self.group_record = Record()
    
    def get_device_list(self):
        return self.device_list
    
    def get_group_id(self):
        return self.group_id

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
            extracted_log = helpers.extract_data_from_log(log)
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
            dmy = helpers.datetime_to_dmy_datetime(log['time'])
            try:
                self.querylog_by_date[dmy].append(log)
            except:
                self.querylog_by_date[dmy] = []
                self.querylog_by_date[dmy].append(log)
        else:
            raise Exception("Mismatch device_name")
        return

    def load_device_logs(self, list_of_logs):
        for log in list_of_logs:
            extracted_log = helpers.extract_data_from_log(log)
            if extracted_log != None:
                self.insert_log_to_querylog(extracted_log)
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

    def get_insta_and_fb_query_using_rx(self, querylog_list):
        """
        GOAL: filter app from a specific date's querylog_list using the app's regex
        input: a list of dict.
        return: a tuple(insta, fb)
        """
        fb_and_insta_query = []
        insta_query = []
        fb_query = []
        for log in querylog_list:
            if fb_mess_insta_rx.search(log['website_request']) != None:
                if insta_rx.search(log['website_request']) != None:
                    insta_query.append(log)
                else: 
                    fb_query.append(log)
        return (insta_query, fb_query)

    def update_device_time_use(self):
        """
        GOAL: After loaded device's log data, process date-sorted log data -> update into self.record()
        input: Device object
        returns: None
        """
        device_app_record = create_empty_app_record()
        device_cate_record = create_empty_cate_record()
        for date in self.get_querylog_by_date():
            """
            1) for a given day, what apps are used during each interval?
            e.g.: interval_all_app = {129:['fb_and_messenger', 'shopee]
                                        130:['fb_and_messenger', 'instagram'],...}
            """
            interval_all_app = {}
            insta_query = self.get_insta_and_fb_query_using_rx(self.get_querylog_by_date()[date])[0]
            fb_mess_query = self.get_insta_and_fb_query_using_rx(self.get_querylog_by_date()[date])[1]
            for cate in category_map_app:
                for app in category_map_app[cate]:
                    if app['name'] == "instagram":
                        app_request = insta_query
                    elif app['name'] == "fb_and_messenger":
                        app_request = fb_mess_query
                    else:
                        app_request = self.get_app_query_using_rx(self.get_querylog_by_date()[date], rx_use=app['regex'])
                    app_interval = helpers.get_num_rq_by_interval(app_request)
                    f_app_interval = dict(sorted(helpers.filter_intensity_by_threshold(app_interval, app['i']).items()))
                    helpers.insert_app_use_to_interval(app['name'], f_app_interval, interval_all_app)
            interval_all_app = dict(sorted(interval_all_app.items()))

            """
            2) for each app, what is the use ratio of the app in each interval? 
            e.g.: ratio_app_res = {'instagram': {130: 0.5, 131: 1.0, 132: 0.33}, 
                                        "shopee': {129: 0.5},...}
            """
            ratio_app_res = {}
            for cate in category_map_app:
                for app in category_map_app[cate]:
                    ratio_app_res[app['name']] = {}

            for app in ratio_app_res:
                for interval in interval_all_app:
                    if app in interval_all_app[interval]:
                        val = 1/(len(interval_all_app[interval]))
                        ratio_app_res[app][interval] = val

            """
            3) for each app, calculate actual time use (in regards of maybe multiple apps are used in one interval)
            e.g.: 
            """
            for app in ratio_app_res:
                app_object = get_app_dict_by_name(app)
                app_time = helpers.get_app_use_time(
                        ratio_app_res[app], ctn_threshold=app_object['c'])
                for itv in ratio_app_res[app]:
                    t = ratio_app_res[app][itv]
                    if t < 1:
                        app_time = app_time - (1-t)

                device_app_record[app_object['name']] += app_time
                device_cate_record[app_object['category']] += app_time

        self.get_record().update_app_stats_time(device_app_record)
        self.get_record().update_category_stats_time(device_cate_record)

        return

    def single_app_update_device_time_use(self):
        """
        GOAL: After loaded device's log data, process date-sorted log data -> update into self.record()
        input: Device object
        returns: None
        """
        device_app_record = create_empty_app_record()
        device_cate_record = create_empty_cate_record()
        for date in self.get_querylog_by_date():
            """
            1) for a given day, what apps are used during each interval?
            e.g.: interval_all_app = {129:['fb_and_messenger', 'shopee]
                                        130:['fb_and_messenger', 'instagram'],...}
            """
            interval_all_app = {}
            insta_query = self.get_insta_and_fb_query_using_rx(self.get_querylog_by_date()[date])[0]
            fb_mess_query = self.get_insta_and_fb_query_using_rx(self.get_querylog_by_date()[date])[1]
            for cate in category_map_app:
                for app in category_map_app[cate]:
                    if app['name'] == "instagram":
                        app_request = insta_query
                    elif app['name'] == "fb_and_messenger":
                        app_request = fb_mess_query
                    else:
                        app_request = self.get_app_query_using_rx(self.get_querylog_by_date()[date], rx_use=app['regex'])
                    app_interval = helpers.get_num_rq_by_interval(app_request)
                    f_app_interval = dict(sorted(helpers.filter_intensity_by_threshold(app_interval, app['i']).items()))
                    helpers.insert_app_use_to_interval(app['name'], f_app_interval, interval_all_app)
            interval_all_app = dict(sorted(interval_all_app.items()))

            """
            2) for each app, what is the use ratio of the app in each interval? 
            e.g.: ratio_app_res = {'instagram': {130: 0.5, 131: 1.0, 132: 0.33}, 
                                        "shopee': {129: 0.5},...}
            """
            ratio_app_res = {}
            for cate in category_map_app:
                for app in category_map_app[cate]:
                    ratio_app_res[app['name']] = {}

            for app in ratio_app_res:
                for interval in interval_all_app:
                    if app in interval_all_app[interval]:
                        val = 1/(len(interval_all_app[interval]))
                        ratio_app_res[app][interval] = val

            """
            3) for each app, calculate actual time use (in regards of maybe multiple apps are used in one interval)
            e.g.: 
            """
            for app in ratio_app_res:
                app_object = get_app_dict_by_name(app)
                app_time = helpers.get_app_use_time(ratio_app_res[app], ctn_threshold=app_object['c'])

                device_app_record[app_object['name']] += app_time
                device_cate_record[app_object['category']] += app_time

        self.get_record().update_app_stats_time(device_app_record)
        self.get_record().update_category_stats_time(device_cate_record)

        return


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

    def get_one_app_time(self, app_name):
        return self.app_stats_time[app_name]

    def get_one_category_time(self, cate_name):
        return self.category_stats_time[cate_name]

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

    def get_formatted_category_stats_time(self):
        og_cate_stats = self.category_stats_time()
        new_formatted_response = cur_frontend_response
        # for app in og_cate_stats:
            
        return

    def get_formatted_app_stats_time(self):
        og_app_stats = self.get_app_stats_time()
        new_formatted_response = cur_frontend_response
        for i in new_formatted_response:
            for j in i['apps']:
                if j['name'] in og_app_stats:
                    j['count'] = og_app_stats[j['name']]
        return new_formatted_response

# if __name__ == "__main__":
#     t_record = Device("tdq")
#     print(create_empty_app_record())
#     print(create_empty_cate_record())