import json
'''
squad = 0 # 分隊
platoon = 0 # 小隊
company = 0 # 中隊
battalion = 0 # 大隊
regiment = 0 # 連隊
division = 0 # 師団
'''

json_file = open('team1.json','r',encoding="utf-8")
json_load = json.load(json_file)
print("{}".format(json.dumps(json_load,indent=4,ensure_ascii=False))) # json風の出力
print(json_load['division1']['司令部']) # 要素を絞る方法
#print(json_load)
# jsonにデータを追加

# jsonに追加する関数
def insert():
    return null

# jsonから削除する関数