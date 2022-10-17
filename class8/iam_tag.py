import boto3

def lambda_handler(event, context):


    client = boto3.client('iam')

    #print(dir(client))

    #Create an empty list
    USERLIST = []

    #Get list of users from AWS, and assign it to responce
    responce = client.list_users()


    for list_of_users in responce["Users"]:
        USERLIST.append(list_of_users["UserName"])
    ################################################################################

    for list_of_users in USERLIST:
        response = client.tag_user(
            UserName=list_of_users,
            Tags=[
                
                {
                    'Key': 'Team',
                    'Value': 'DevOps'
                },
                {
                    'Key': 'Dept',
                    'Value': 'IT'
                },
            ]
        )