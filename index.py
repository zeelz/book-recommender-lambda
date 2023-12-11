# for local
from dotenv import load_dotenv
load_dotenv()


from data import books
from processor import getBooks
# import json
# import os
# import requests #available locally and as a layer
# import psycopg2 as pc #available as a layer
# import fuzzywuzzy as fz #available as a layer
# from sklearn.metrics.pairwise import cosine_similarity as cos_sim #available as a 3rd-party layer
# arn:aws:lambda:us-east-1:446751924810:layer:python-3-8-scikit-learn-0-23-1:2

# for calling 3rd-party APIs
# url = os.getenv("URL")
# res = requests.get(url)

def lambda_handler(event, context):
    # return f"Packages version: Psycopg2 {pc.__version__}, Fuzzywuzzy {fz.__version__}"
    # return res.json()

    # for accepting json payload, http apigw, rest proxy intg.
    # body = event.get("body")
    # data = json.loads(body) #encode json
    # print(data.get('searchKey'))

    # return 
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': getBooks(event["category"], books)
    }



# for local
event = {"category": "sales"}
print(lambda_handler(event, context=None))