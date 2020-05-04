import json
import boto3
mys3=boto3.client('s3')
print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    #print("value1 = " + event['key1'])
   
    bucket='vitademo'
    key='my/my.json'
    response=mys3.get_object(Bucket=bucket,Key=key)
    content=response['Body']
    jsonObject=json.loads(content.read())
    t=jsonObject['name']
    

    print("student name--->",jsonObject['name'])
    print("College Name--->",jsonObject['college'])
    return jsonObject['name']