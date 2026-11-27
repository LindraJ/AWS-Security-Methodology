import time
import csv

def credReport(session):
    
    iamConnection = session.client("iam")
    generateCredReport = iamConnection.generate_credential_report()
    retries = 1
    

    while generateCredReport["State"] != "COMPLETE" and retries <= 3:
        time.sleep(120)
        generateCredReport = iamConnection.generate_credential_report()
        retries += 1

    if generateCredReport["State"] == "COMPLETE":
        credReport = iamConnection.get_credential_report()
        rawCredReport = credReport["Content"]
        textCredReport = rawCredReport.decode("utf-8")
        credReportLines = textCredReport.splitlines()
        returnedCredReport = csv.DictReader(credReportLines)
        return list(returnedCredReport)
    else:
        print("Report not ready after 3 tries.")
        return[]