Lab 01: AWS Organizations and an SCP Guardrail

Date: October 3, 2026 Maps to: SAA-C03 Task 1.1 (Design secure access to AWS resources)

Knowledge: access controls and management across multiple accounts
Skill: designing a security strategy for multiple AWS accounts (Control Tower, service control policies)
Also touched: security best practices for root and IAM users (MFA), cross-account access by role

Account IDs, the organization ID, and the policy ID are replaced with placeholders.

Goal

Build a small multi-account environment and prove that a service control policy (SCP) stops an account administrator from turning off audit logging.

Core idea

The account is the wall. A rule that lives inside an account can be deleted by whoever controls that account. An SCP lives at the organization level, so the accounts it restricts can't change or remove it.

What I built
Root
├── management account          (runs the organization, no workloads)
└── Sandbox (OU)
    ├── security                (member account)
    └── workload                (member account)

SCP "DenyCloudTrailTampering" attached to: Sandbox
Steps
1. Secured the management account
Turned on MFA for the root user.
Created an IAM group Admins with the AdministratorAccess policy.
Created an admin IAM user, added it to Admins, and turned on MFA for it.
Signed out of root and did everything else as the admin user.

Why: root in the management account is the most powerful login in the whole organization, so it is locked down and kept for the few tasks that need it. Permissions go on the group, not the user.

2. Created the organization
AWS Organizations > Create an organization (all features enabled).
Verified the email AWS sent.
Result: a Root with my account under it, labeled as the management account.
3. Created the OU and member accounts
Created an OU named Sandbox under Root.
Created two member accounts, security and workload, each with its own email address and the default role name OrganizationAccountAccessRole.
Moved both accounts into Sandbox.
Left the management account directly under Root. It does the governing and is not one of the governed accounts.
4. Created and attached the SCP
Policies > Service control policies > Enable.
Created a policy named DenyCloudTrailTampering:
json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyCloudTrailTampering",
      "Effect": "Deny",
      "Action": [
        "cloudtrail:StopLogging",
        "cloudtrail:DeleteTrail"
      ],
      "Resource": "*"
    }
  ]
}
Attached it to the Sandbox OU.
Left the default FullAWSAccess policy attached. SCPs only limit and never grant, so removing it would block everything in those accounts.

Reading the policy:

"Effect": "Deny" is an explicit deny, which beats any allow.
"Action" lists the two blocked actions: stopping logging and deleting a trail.
"Resource": "*" applies it to every trail.
5. Tested it
From the management account, used Switch role to enter the workload account with OrganizationAccountAccessRole (full admin in that account).
Opened CloudShell and ran:
aws cloudtrail stop-logging --name test-trail
Predictions before the test
Question	Prediction	Result
Can the workload account's own admin stop CloudTrail logging?	No	Confirmed
Can I, after switching into workload from the management account?	No	Confirmed
Can I stop logging in the management account itself?	Yes	Not tested (would mean stopping a real trail). SCPs don't apply to the management account
Result
aws: [ERROR]: An error occurred (AccessDeniedException) when calling the
StopLogging operation: User:
arn:aws:sts::<WORKLOAD_ACCOUNT_ID>:assumed-role/OrganizationAccountAccessRole/<ADMIN_USER>
is not authorized to perform: cloudtrail:StopLogging on resource:
arn:aws:cloudtrail:us-east-1:<WORKLOAD_ACCOUNT_ID>:trail/test-trail
with an explicit deny in a service control policy:
arn:aws:organizations::<MANAGEMENT_ACCOUNT_ID>:policy/<ORG_ID>/service_control_policy/<POLICY_ID>
What each part shows
Part of the message	What it shows
sts::<WORKLOAD_ACCOUNT_ID>:assumed-role/OrganizationAccountAccessRole/<ADMIN_USER>	I was acting as an assumed role inside the workload account. STS issued temporary credentials. This is cross-account access by role
not authorized to perform: cloudtrail:StopLogging	The action the policy blocks
with an explicit deny in a service control policy	The reason: an explicit deny beat full admin permissions
organizations::<MANAGEMENT_ACCOUNT_ID>:policy/...	The policy lives in the management account, not in the workload account, so nobody in workload can delete it
What this proves
An SCP binds everyone in a member account, including a role with full admin access.
Switching in from the management account gives no exemption. Once inside the member account, the guardrail applies.
The policy is stored outside the account it restricts. That is the reason it can't be removed from inside.
Stopping audit logging is the first thing an attacker does to hide their tracks. This guardrail keeps the logs on through a mistake, insider abuse, or a compromised admin.
Shared responsibility: my side of the line
AWS runs the Organizations service and enforces the policy.
The customer decides the account structure, writes the SCPs, attaches them to the right OUs, and protects the management account.
What to check in a client review
Does the management account hold workloads, or have many users? It should have neither.
Do root users have MFA?
Are there SCPs protecting logging and security tooling (CloudTrail, Config, GuardDuty)?
Are SCPs attached at the OU level so new accounts inherit them?
Is FullAWSAccess still attached where intended?
Client pitch

"People make mistakes, and sometimes attackers get in, and no company can fully prevent either. What we can do is set guardrails above your accounts, so that even with full access, certain actions (like switching off your security logging) simply can't happen."

Notes and lessons
"Security groups" (network firewall rules in EC2/VPC) and "User groups" (IAM) are different things. The admin group is an IAM user group.
The default security group in a VPC can't be deleted. Best practice is to remove its rules and not use it (Task 1.2).
Regional services are only visible in the Region the console is set to. A leftover storage volume in another Region showed up on the bill but not in the console until the Region was switched. EC2 Global View lists resources across all Regions.
Member accounts are easy to create and take about 90 days to fully close.
