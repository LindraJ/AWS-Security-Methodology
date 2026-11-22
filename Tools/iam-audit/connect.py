import boto3
import json
import time


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
    response = sts.assume_role(RoleArn=roleARN, RoleSessionName=sessionName)

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
    iamConnection = roleSession.client("iam")
    generateCredReport = iamConnection.generate_credential_report()
    retries = 1

    while generateCredReport["State"] != "COMPLETE" and retries <= 3:
        time.sleep(120)
        generateCredReport = iamConnection.generate_credential_report()
        retries += 1

    if generateCredReport["State"] == "COMPLETE":
        credReport = iamConnection.get_credential_report()
        print(credReport["Content"].decode("utf-8"))
    else:
        print("Report not ready after 3 tries.")
