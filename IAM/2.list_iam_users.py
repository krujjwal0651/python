import boto3

def list_iam_users():
    iam = boto3.client("iam")

    paginator = iam.get_paginator('list_users')

    for response in paginator.paginate():
        for user in response['Users']:
            username = user['UserName']
            ARN = user['Arn']
            print(f"UserNamer : {username}, ARN : {ARN}")

list_iam_users()

# Below is the code to print whole output from paginator and
# to understand why we are using for loop for printing only few fields

# iam = boto3.client("iam")
#
# paginator = iam.get_paginator('list_users')
#
# all_pages = paginator.paginate().build_full_result()
#
# print(all_pages)