import boto3
import json
import generateReport

def configSettings():
     # 1. Read the config
    with open("config.json") as f:
        config = json.load(f)
    return config

def getRoleSession(profile, arn, nameSession):

    # 2. Sign in wth sso
    session = boto3.Session(profile_name=profile)
    sts = session.client("sts")

    # 3. Assume the audit role
    response = sts.assume_role(RoleArn=arn, RoleSessionName=nameSession)

    # 4. Put on the role's badge
    creds = response["Credentials"]
    roleSession = boto3.Session(
        aws_access_key_id=creds["AccessKeyId"],
        aws_secret_access_key=creds["SecretAccessKey"],
        aws_session_token=creds["SessionToken"],
    )
    return roleSession


if __name__ == "__main__":
    config = configSettings()
    
    myProfile = config["connection"]["profileName"]
    roleARN = config["connection"]["roleArn"]
    sessionName = config["connection"]["sessionName"]
    
    roleSession = getRoleSession(myProfile, roleARN, sessionName)
    identity = roleSession.client("sts").get_caller_identity()
    
    rows = generateReport.credReport(roleSession)
    for row in rows:
        print(row["user"], row["mfa_active"])