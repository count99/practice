import time

now = time.time()
def get_data():
    with open (r'C:\Users\may\Documents\practice_data.txt', 'r', encoding='utf-8') as files:
        results = [line.strip('\n').strip('"').split('","') for line in files.readlines()]
        files.close()
    data_keys = ('bid', 'uid', 'username', 'v_class', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid', 'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_bid', 'location', 'rt_mid', 'mid', 'lat', 'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links', 'rt_hashtags', 'rt_ats', 'v_url', 'rt_v_url')
    total_dict = {}
    for i in range(35):
        temp_list = []
        for j in results:
            temp_list.append(j[i])
        total_dict[data_keys[i]] = temp_list
    return total_dict

def count_element(lis):
    d={}
    for i in set(lis):
        d[i]=lis.count(i)
    return d

def max_key_by_max_values(dict1):
    a = max(dict1.values())
    for i in dict1:
        if dict1[i] == a:
            return i
        
from_dict = get_data()
users = from_dict['username']
# Answer 1
len(users)
assert type(len(users)) == int
# Answer 2
assert type(users) == list
# Answer 3
times = from_dict['created_at']
time201211 = []
hours = []
days = []
for i in range(len(times)):
    get_strp = time.strptime(times[i], "%Y-%m-%d %H:%M:%S")
    hours.append(get_strp[3])
    temp_day = "%s-%s-%s" % (get_strp[0],get_strp[1],get_strp[2])
    days.append(temp_day)
    if (2012 == get_strp[0]) and (11 == get_strp[1]):
        time201211.append(temp_day)
# answer 3
len(time201211)
assert type(len(time201211)) == int 
# answer 4
assert type(time201211) == list 
# answer 5
per_hour = set(hours)
count_hours = [hours.count(x) for x in per_hour]
most_post_hour = count_hours.index(max(count_hours))
# answer 6
count_per_day_posted = {}
for i, j in enumerate(days):
    if j not in count_per_day_posted:
        count_per_day_posted[j] = [users[i]]
    else:
        count_per_day_posted[j].append(users[i])
max_post_user ={}
for i in count_per_day_posted:
    max_post_user[i]=max(count_per_day_posted[i])
# answer 7
               





















print ('Running time¡G %s'%(time.time() - now))