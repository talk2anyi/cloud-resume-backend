import json

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitor_counter')


def lambda_handler(event, context):

    response = table.get_item(Key= {'pagename' : 'hostname'} )

    count = response["Item"]["loadcount"]
    print("Get Response = ", response)
    print( "Count = ", count)

    # increment string version of visit count
    new_count = str(int(count)+1)
    response = table.update_item(
        Key={'pagename' : 'hostname'},
        UpdateExpression='set loadcount = :c',
        ExpressionAttributeValues={':c': new_count},
        ReturnValues='UPDATED_NEW'
        )

    print("Update Response =  ", response)
    return {
        
        'body': new_count
    }
    
