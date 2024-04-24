import dashscope

from search import search_relevant_news
from answer import answer_question
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == '__main__':
    dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

    question = '海南安定追尾事故，发生在哪里？原因是什么？人员伤亡情况如何？'
    context = search_relevant_news(question)
    answer = answer_question(question, context)

    print(f'question: {question}\n' f'answer: {answer}')