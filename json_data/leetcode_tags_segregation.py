import json
import pandas as pd

json_file = open('leetcode_data.json')

question_data = json.load(json_file)
all_questions = []
final_tags_set = set()
leetcode_string = "https://leetcode.com/problems/"
for question in question_data["data"]["topicTag"]["questions"]:
    out_tags = []
    false_tags = False
    false_tags_ar = ['divide-and-conquer', 'tree', 'dynamic-programming', 'graph', 'greedy', 'bit-manipulation',
                     'binary-indexed-tree', 'matrix', ]
    for i in question["topicTags"]:
        if i["slug"] in false_tags_ar:
            false_tags = True
            break
        out_tags.append(i["slug"])
    final_tags_set.update(out_tags)
    if not false_tags:
        q_stats = json.loads(question["stats"])
        all_tags = question["topicTags"]
        each_qn_dict = {
            "title": question["title"],
            "tags": out_tags,
            "status": question["status"],
            "acceptanceRate": q_stats["acRate"],
            "totalSubmission": q_stats["totalSubmission"],
            "totalAccepted": q_stats["totalAccepted"],
            "titleSlug": f'{leetcode_string}{question["titleSlug"]}/',
        }
        all_questions.append(each_qn_dict)

pandas_dataframe = pd.DataFrame(all_questions)
file_name = 'tag_data_analysis.xlsx'
pandas_dataframe.to_excel(file_name)
print("final_tags_set", final_tags_set)
