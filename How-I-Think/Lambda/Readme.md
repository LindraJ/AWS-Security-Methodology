# Lambda Systems Thinking

This folder contains my systems-thinking analysis of AWS Lambda.

The goal is not just to understand Lambda as a service, but to understand:

- behavioral dynamics
- trust relationships
- permission propagation
- leverage points
- misalignments
- attack paths
- and systemic security risk

These maps are part of my broader effort to develop a structured AWS security methodology focused on understanding how cloud systems behave and how compromise propagates through interconnected services.

---

## Maps

### Lambda Behavioral Stock/Flow Map
Focuses on:
- triggers
- active executions
- scaling
- throttling
- queues
- balancing/reinforcing loops
- system behavior over time

Questions explored:
- How does Lambda behave under changing conditions?
- What feedback loops exist?
- Where do delays or oscillations occur?

---

### Lambda Trust / Permission Propagation Map
Focuses on:
- trust relationships
- execution roles
- AWS resource access
- leverage points
- permission propagation
- attacker impact
- misalignment analysis

Questions explored:
- What trusts what?
- How does authority propagate?
- What assumptions are being made?
- What happens if a leverage point is compromised?

---

### Lambda Assumption Analysis
Focuses on:
- assumptions developers and operators make about Lambda
- what breaks those assumptions
- resulting attacker behavior
- blast radius and impact rating

Questions explored:
- What do people believe is true about Lambda that isn't always true?
- What happens when those beliefs are violated?
- How far can an attacker move if a single assumption fails?
