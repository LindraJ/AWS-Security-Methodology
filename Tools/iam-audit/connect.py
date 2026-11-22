import boto3
import json


def getRoleSession():
    # 1. Read the config
    with open("config.json") as f:
        config = json.load(f)

    myProfile = config["connection"]["profileName"]
    roleARN = config["connection"]["roleArn"]
    sessionName = config["connection"]["sessionName"]

    # 2. Sign in wth sso
    session = boto3.Session(profile_name=myProfile)
    sts = session.client("sts")

    # 3. Assume the audit role
    response = sts.assume_role(
        RoleArn=roleARN,
        RoleSessionName=sessionName
    )

    # 4. Put on the role's badge
    creds = response["Credentials"]
    roleSession = boto3.Session(
        aws_access_key_id=creds["AccessKeyId"],
        aws_secret_access_key=creds["SecretAccessKey"],
        aws_session_token=creds["SessionToken"],
    )
    return roleSession


if __name__ == "__main__":
    roleSession = getRoleSession()
    identity = roleSession.client("sts").get_caller_identity()
    print("Running as:", identity["Arn"])