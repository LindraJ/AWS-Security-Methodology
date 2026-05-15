# Lab 1: Safe Default

## Setup
- Created bucket with Block Public Access ON (all 4 boxes checked)
- Uploaded test.txt
- Tried to access via URL in incognito

## Result
Access Denied

## Learning
Block Public Access ON = explicit DENY for public access. 
This is AWS's safety net. Even with no other settings, 
the bucket is secure. Explicit DENY overrides everything.

## Formula Applied
Has explicit DENY = Access Denied 





# Lab 2: Block Public Access OFF (No Allow)

## Setup
- Turned off Block Public Access (unchecked all 4 boxes)
- Kept everything else same (no bucket policy, no public ACL)
- Tried to access test.txt via URL in incognito

## Result
Access Denied

## Learning
Block Public Access OFF alone doesn't make bucket public. 
You need at least 1 ALLOW somewhere. Without an ALLOW, 
everything is silent (implicit deny).

## Formula Applied
No explicit DENY ✓
No ALLOW ✗
Result: Silence = Implicit Deny = Access Denied ✓

## Key Insight
Turning off Block Public Access is NOT enough to create 
a vulnerability. Need "no no's + at least 1 yes" - we had 
no no's but also no yes.





# Lab 3: Bucket Policy Public (The Bug!)

## Setup
- Block Public Access: OFF
- Added bucket policy:
```json
  {
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:GetObject"
  }
```
- Object ACL: Private (silent)
- Tried to access test.txt via URL in incognito

## Result
ACCESS GRANTED - Could see file contents!

## Learning
This is what I call my "favorite gem" 💎. The `"Principal": "*"` 
gives anyone access to the bucket. The asterisk (*) means 
everyone/anonymous/public.

## Formula Applied
No explicit DENY (Block Public Access OFF) ✓
At least 1 ALLOW (bucket policy Principal "*") ✓
Result: No no's + at least 1 yes = ACCESS GRANTED = BUG! 🐛💰

## Key Insight
This is the #1 S3 bug pattern. Companies accidentally set 
Principal to "*" thinking it means something else. Even 
though Object ACL is private (silent), the bucket policy 
ALLOW grants public access.

## In Real Hunting
This is easy money. Find bucket with Block Public Access OFF 
and Principal "*" = report = $500-5K bounty.





# Lab 4: Explicit DENY Wins

## Setup
- Turned Block Public Access back ON (all 4 boxes checked)
- Kept bucket policy with `"Principal": "*"` (my favorite gem)
- Object ACL: Private
- Tried to access test.txt via URL in incognito

## Result
ACCESS DENIED

## Learning
I decided to test what would happen if I turned on Block 
Public Access with my favorite gem to see if it does anything. 
I could not access the file anymore due to the explicit DENY.

## Formula Applied
Has explicit DENY (Block Public Access ON) ✓
Has ALLOW (bucket policy Principal "*") ✓
Result: DENY WINS over ALLOW = Access Denied ✓

## Key Insight
Explicit DENY always wins. Even though the bucket policy 
says "Allow everyone", Block Public Access overrides it. 
This is the safety net - it beats everything.

## The Rule
DENY > ALLOW (always)





# Lab 5: Object ACL Public (The Forgotten Layer!)

## Setup
- Turned off Block Public Access (removed explicit DENY)
- Deleted bucket policy with my favorite gem (made it empty/silent)
- Set Object ACL to Public Read
- Tried to access test.txt via URL in incognito

## Result
ACCESS GRANTED - Could see file contents!

## Learning
I wanted to test the object ACL so I turned off the explicit 
DENY (Block Public Access) because with it ON I won't be able 
to access anything. I deleted my favorite gem bucket policy 
because from the last lab it works. I set the object ACL to 
Public Read, and I could access it because the public read ACL 
is an ALLOW so it follows the formula.

## Formula Applied
No explicit DENY (Block Public Access OFF) ✓
Bucket policy: Silent (empty) ⚪
Object ACL: Public Read (ALLOW) ✓
Result: No no's + at least 1 yes = ACCESS GRANTED = BUG! 🐛💰

## Key Insight
This is the FORGOTTEN LAYER. Companies secure bucket policy 
but forget to check individual object ACLs. Object ACLs are 
a separate layer that can grant access even when bucket policy 
is silent or restrictive.

## In Real Hunting
This is a common bug pattern. Companies think: "Bucket policy 
is secure, we're safe." But old objects from 2015-2019 still 
have public ACLs. Easy money - check object ACLs individually!




# Lab 6: Timeline Bug (Old Objects Stay Vulnerable!)

## Setup
- Kept setup from Lab 5 (Block Public Access OFF, no bucket policy)
- test.txt: Had Public Read ACL (from Lab 5)
- Created test2.txt: Default Private ACL (new upload)
- Tried to access both files via URL in incognito

## Result
- test.txt: ACCESS GRANTED ✓
- test2.txt: ACCESS DENIED ✗

## Learning
I took Lab 5 a step further. I made a second file with no 
public read ACL, and I could only access the test.txt file 
and not the test2.txt file.

## Formula Applied
**For test.txt (old object):**
- No explicit DENY ✓
- Object ACL: Public Read (ALLOW) ✓
- Result: ACCESS GRANTED = BUG! 🐛

**For test2.txt (new object):**
- No explicit DENY ✓
- Object ACL: Private (silent) ⚪
- Result: No ALLOW = ACCESS DENIED ✓

## Key Insight - Timeline Bug Pattern
Same bucket, different objects, different permissions! 
This is exactly what happens in real companies:
- 2015: Upload objects with public ACL ✓
- 2020: "Secure" bucket with new policy ✓
- 2024: Old objects STILL have public ACLs ✗

Companies think they're secure but forgot to check old objects. 
Bucket policies don't retroactively change object ACLs!

## In Real Hunting
Check individual objects, especially old ones. Companies miss 
this constantly. 9-year-old vulnerabilities still exist!




# Lab 7: Context-Dependent Evaluation

## Setup
Same as Lab 6 - two objects in one bucket

## Observation
- Bucket-level settings apply to ALL objects ✓
- Object ACLs are PER OBJECT ✓
- Must check each object individually ✓

## Learning
This proves context-dependent evaluation. The bucket doesn't 
have one single permission state. Each object is evaluated 
in its own context:
- test.txt context: Public ACL = accessible ✓
- test2.txt context: Private ACL = denied ✗

## Key Insight
When hunting bugs, can't just check bucket-level. Must check 
individual objects because same bucket ≠ same permissions.

## What I learned from Day 2
User Context, Bucket Context, Object Context - seen in reality!








# External Testing: Real-World Bug Hunting Skills

## Why External Testing
When it comes to bug bounties I will more than likely be on 
the outside looking in. I won't have AWS console access to the 
company's account. So I did some practice testing from the 
outside using AWS CLI.

## Tools Used
- AWS CLI
- Command Prompt (Windows)
- No AWS account credentials needed (`--no-sign-request`)

## Test Target
flaws.cloud (legal training bucket by Scott Piper)

## What I Did

### Step 1: List Bucket Contents
```bash
aws s3 ls s3://flaws.cloud --no-sign-request
```

**Result:** Found public bucket! Listed all files including:
- hint1.html
- hint2.html  
- secret-dd02c7c.html ← Interesting!
- And more...

### Step 2: Download Secret File
```bash
aws s3 cp s3://flaws.cloud/secret-dd02c7c.html . --no-sign-request
```

**Result:** Successfully downloaded the file to my computer!

## Formula Applied
From outside (no console access):
- No explicit DENY (Block Public Access OFF) ✓
- At least 1 ALLOW (bucket policy or ACL) ✓
- Result: Could list and download = VULNERABLE 🐛

## FIND-FOCUS-FIRE in Action
- **FIND:** Listed bucket, found files (reconnaissance) 🔍
- **FOCUS:** Identified secret file (analysis) 🎯
- **FIRE:** Downloaded and accessed it (exploitation) 🔥

## Key Commands Learned
- `aws s3 ls` = list bucket contents
- `aws s3 cp` = copy/download files
- `--no-sign-request` = anonymous access (no credentials)
- `.` = current directory

## Real-World Application
This is exactly how I'll hunt bugs:
1. Find bucket names (recon)
2. Test if public (`aws s3 ls --no-sign-request`)
3. Look for sensitive files
4. Document findings
5. Report to company = $$$ 💰

## Additional Testing
Also tested level3 bucket and found authenticated users 
vulnerability - learned that "Any Authenticated AWS User" 
is NOT the same as "my users only". It means ANY AWS 
customer = still vulnerable!

## What I'm Ready For
- External enumeration ✓
- Anonymous testing ✓
- Finding public buckets ✓
- Documenting proof ✓
- Real bug hunting 🎯💰
