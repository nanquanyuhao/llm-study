# 测试本地服务
# 返回信息如：{"article": "第十三条  寝室实行轮流值日制，负责寝室内公共卫生工作，扫地、拖地板、倒垃圾等，保持良好状态。"}
curl --location 'http://localhost:9000/article' \
--header 'Content-Type: application/json' \
--data '{
    "article_index": 13
}'