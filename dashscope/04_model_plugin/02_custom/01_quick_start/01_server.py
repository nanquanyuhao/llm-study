#!/usr/env python3
# -*- coding: UTF-8 -*-

from flask import Flask, request, send_file, make_response
import json
import random

app = Flask(__name__)

agreements = [
    "寝室公约",
    "第一条  寝室生活应建立在和谐共处，高规格、高品味的氛围之中。",
    "第二条  寝室成员应当互帮互助、互相关心、互相学习、共同提高；宽容谦让、相互尊重、以诚相待。",
    "第三条  注意安全用电，杜绝火灾隐患。寝室内严禁使用明火、违规电器、各种灶具以及其他违规物品，不得存放易爆、易燃物品，私接电源。",
    "第四条  提高防范意识，保证财产安全，做好防盗防骗工作。个人贵重物品应当妥善保管，寝室钥匙不得随意转借给他人，寝室无人或休息时应当关好门窗，关好电源，发现可疑人员应当及时报告管理员或安全保卫部门。",
    "第五条  严禁夜不归宿。晚上不能按时回寝室的，应当告知生活委员；发现室友未按时归宿寝室，应当及时联系，必要时应当报告辅导员；寝室不得留宿未经批准的外来人员。",
    "第六条  养成良好的作息习惯，每一位寝室成员都享有休息的权利和承担保证他人休息权利和义务。",
    "第七条  晚寝时间为22：30~次日6：30，在规定的休息时间之外的其他时间寝室成员的休息权利也应得到保障。休息时间可以根据各个寝室的不同情况进行适当的调整。",
    "第八条  休息时间应当保持寝室内安静，严禁上网、打牌、赌博等不良活动；关闭收音机、音响，关闭手机或调至震动，严禁五分钟以上的聊天电话；晚寝应当准时熄灯，寝室成员应当停止与作息无关的其他活动，如有紧急事务需要处理的，应征得其他成员同意，并做到不影响寝友。",
    "第九条  节假日，以上作息时间在室友协商一致的情况下可以进行适当调整。",
    "第十条  寝室成员应共同努力，营造和维护内务整洁干净、美观、高文化品味的寝室环境。",
    "第十一条  讲究公共卫生，不乱扔乱丢垃圾，不随地吐痰，不在墙壁、门窗、床椅、其它设施上乱刻乱画，保持寝室地面、天花板、墙壁和设备的清洁以及室内空气流通、清新。",
    "第十二条  讲究个人卫生，床铺每日整理，个人衣服和物品归类摆放整齐，书籍整理有序。勤洗澡，勤洗晒衣物被褥。避免影响他人卫生。",
    "第十三条  寝室实行轮流值日制，负责寝室内公共卫生工作，扫地、拖地板、倒垃圾等，保持良好状态。",
    "第十四条  寝室每周四进行大扫除，由寝室长组织，各成员无特殊情况应当积极参加。",
    "第十五条  寝室成员可以在寝室内接待亲人、朋友，做到不喧哗；其他成员应当热情礼貌。",
    "第十六条  客人来访应当遵守本公约的约定，不得影响他人的休息与日常活动。",
]

def make_json_response(data, status_code=200):
    response = make_response(json.dumps(data, ensure_ascii=False), status_code)
    response.headers["Content-Type"] = "application/json"
    return response


@app.route("/article", methods=['POST'])
def generate_sentences():
    """
        查询第几条寝室公约具体内容
    """
    index = request.get_json()['article_index']
    if index > 0 and index < len(agreements):
        agreement = agreements[index]
        return make_json_response({"article": agreement})
    else:
        data = {"error": "不存在该编号的条款。"}
        response = make_response(json.dumps(data, ensure_ascii=False), 400)
        response.headers["Content-Type"] = "application/json"
        return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)