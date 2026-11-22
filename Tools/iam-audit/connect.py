import boto3
import json

with open("config.json") as f:
    config = json.load(f)

myProfile = config["connection"]["profileName"]
roleARN = config["connection"]["roleArn"]
sessionName = config["connection"]["sessionName"]




session = boto3.Session(profile_name=myProfile)
sts = session.client("sts")

response = sts.assume_role(
    RoleArn=roleARN,
    RoleSessionName=sessionName
)
creds = response["Credentials"]
roleSession = boto3.Session(
    aws_access_key_id=creds["AccessKeyId"],
    aws_secret_access_key=creds["SecretAccessKey"],
    aws_session_token=creds["SessionToken"],
)
print(response["AssumedRoleUser"]["Arn"])

stsRole = roleSession.client("sts")

identity = stsRole.get_caller_identity()

print(identity["Arn"])