import json
import math
import boto3

from time import gmtime, strftime

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('powerofmathdatabase')

now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

def lambda_handler(event, context):
    mathResult = math.pow(int(event['base']), int(event['exponent']))
    
    response = table.put_item(
        Item={
            'ID': str(mathResult),
            'LatestGreetingTime': now
        })
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Your result is ' + str(mathResult))
    }
