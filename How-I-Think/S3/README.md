# S3 Systems Thinking

This folder contains my systems-thinking analysis of AWS S3.

The goal is not just to understand S3 as a service, but to understand:

- behavioral dynamics
- access control layers
- trust relationships
- permission propagation
- leverage points
- misalignments
- attack paths
- and systemic security risk

These maps are part of my broader effort to develop a structured AWS security methodology focused on understanding how cloud systems behave and how compromise propagates through interconnected services.

---

## Maps

### S3 Behavioral Stock/Flow Map
Focuses on:
- PUT/GET/DELETE request flows
- objects stored in buckets (stock)
- access control valves (IAM, Bucket Policy, Block Public Access, Object ACL)
- lifecycle policy feedback loops
- versioning feedback loops
- system behavior over time

Questions explored:
- What controls whether objects flow in or out?
- Why does the output side have more protection than the input side?
- What feedback loops automatically manage the stock?
- Where do misconfigurations silently open the flow?

---

### S3 Trust / Permission Propagation Map
Focuses on:
- three principal types (IAM User/Role, AWS Services, Anonymous/Public)
- trust mechanisms per principal
- how authority flows to the bucket and objects
- leverage points at each trust layer
- attacker impact per leverage point
- the forgotten layer (Object ACL)

Questions explored:
- What trusts what?
- How does each principal type reach the bucket?
- What assumptions are being made at each layer?
- What happens if a leverage point is compromised?

---

### S3 Assumption Analysis
Focuses on:
- assumptions developers and operators make about S3 access control
- what breaks those assumptions
- resulting attacker behavior
- blast radius and impact rating

Questions explored:
- What do people believe is true about S3 that isn't always true?
- What happens when Block Public Access is off but no policy exists?
- How does the timeline bug expose old objects?
- How far can an attacker move if a single assumption fails?
