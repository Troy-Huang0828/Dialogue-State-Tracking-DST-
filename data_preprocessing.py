import json
import os
from tqdm import tqdm

#
# #train schema
# test_seen_list=os.listdir("./data/train")
# services_list=[]
# # path="./data/train/dialogues_001.json"
# for path in tqdm(test_seen_list):
#     with open("./data/train/"+path, "r", encoding='utf-8') as f:
#
#         data=json.load(f)
#         #找大 services
#         for i in range(len(data)):
#             for service in data[i]["services"]:
#                 if service not in services_list:
#                     services_list.append(service)
#         # 找小 service
#         for i in range(len(data)):
#             for j in range(len(data[i]["turns"])):
#                 for k in range(len(data[i]["turns"][j]["frames"])):
#                     # print(data[i]["turns"][j]["frames"][k]["service"])
#                     if data[i]["turns"][j]["frames"][k]["service"] not in services_list:
#                         services_list.append(data[i]["turns"][j]["frames"][k]["service"])
# print(services_list)
#
#
#
# with open("./data/schema.json", "r", encoding='utf-8') as f:
#     data = json.load(f)
#     for i in range(len(data)):
#         if data[i]['service_name'] in services_list:
#             print(data[i]['service_name'])
#         # print(data[i]['service_name'])




dir_list=os.listdir("./data/test")
print(dir_list)
for dir in dir_list:
    with open("./data/test/"+dir, 'r') as f:

        data=json.load(f)
        for i in range(len(data)):
            for j in range(len(data[i]['turns'])):
                data[i]['turns'][j]["frames"]=[]


        with open("./data/test1/"+dir, 'w') as f:
            json.dump(data, f, indent=2)




