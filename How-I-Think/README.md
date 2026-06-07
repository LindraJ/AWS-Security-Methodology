# How I Think

This folder contains my systems-thinking analysis of AWS services.

The goal is not just to understand each service, but to understand:

- behavioral dynamics
- trust relationships
- permission propagation
- leverage points
- misalignments
- attack paths
- and systemic security risk

These maps are part of my broader effort to develop a structured AWS security methodology focused on understanding how cloud systems behave and how compromise propagates through interconnected services.

---

## Services Analyzed

| Service | Concept Map | Behavioral Map | Trust/Permission Map | Assumption Analysis |
|---------|------------|---------------|---------------------|-------------------|
| [Lambda](./Lambda/) | ✅ | ✅ | ✅ | ✅ |
| [S3](./S3/) | ✅ | ✅ | ✅ | ✅ |
| [Fargate](./Fargate/) | ✅ | ✅ | ✅ | ✅ |

---

## The Four Maps

Every service gets the same four maps:

**1. Concept Map**
The full ecosystem before analysis. What connects to what? How does the service fit into the broader AWS landscape?

**2. Behavioral Stock/Flow Map**
How does the service behave over time? What flows in, what flows out, what feedback loops control the system?

**3. Trust/Permission Propagation Map**
What trusts what? How does authority flow? Where are the leverage points and what happens if one is compromised?

**4. Assumption Analysis**
What does everyone assume is true? What breaks those assumptions? What's the blast radius when they fail?

---

## Key Concepts Practiced

- Systems thinking
- Security architecture reasoning
- Leverage-point analysis
- Misalignment detection
- Blast-radius analysis
- Behavioral feedback loops
- Trust-boundary analysis

---

## Current Goal

Map every major AWS service using the same four-map framework — building a methodology for finding what others miss by understanding how systems actually behave, not how they're assumed to behave.
