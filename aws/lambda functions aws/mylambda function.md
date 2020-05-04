# How to read json file from s3 bucket to lambda function
- **first create md file in s3 bucket**
- **Write lambda function to read json file**
### Lambda Function
```python
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
```



### JSON File Created in s3 bucket
```json
{
	"name":"mukund",
	"college":"SM-VITA"
}

```
