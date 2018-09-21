from handlers.base import BaseHandler
from aws.dynamo import DynamoHandler
import json
import tornado.escape
from cloudaux.aws.sts import boto3_cached_conn as boto3_cached_conn


class GetUserHandler(BaseHandler):

    def get(self, group=None):
        user = DynamoHandler().get_requests_by_user("nag")
        resource = boto3_cached_conn(
                'dynamodb',
                service_type='resource')
        print (resource)
        table = resource.Table("pet")
        if not group:
            response = table.scan()
            #response = table.get_item(Key={"par": "test"})
            self.write("Response {} ".format(json.dumps(response["Items"], indent=1)))
        else:
            print(group)
            print("00000")
            response = table.get_item(Key={"par": group})
            print(response)
            if response.get('Item', None):
                print(dir(response))
                self.write(" Response  {} ".format(json.dumps(response["Item"],indent=1)))
            else:
                self.write("User :{}  Not found".format(group))

    def post(self):
         data = tornado.escape.json_decode(self.request.body)
         print(data)
         if data.get("par"):
             self.write(data)
             resource = boto3_cached_conn('dynamodb',service_type='resource')
             print(resource)
             table = resource.Table("pet")
             table.put_item(Item=data)

