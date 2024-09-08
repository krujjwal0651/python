from http.client import responses

import boto3

def create_iam_user(username):

    iam = boto3.client('iam')
    response = iam.create_user(UserName=username)

    print(response)

create_iam_user("uttam56")


