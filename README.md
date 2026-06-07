# AWS Security Methodology

I find complex AWS vulnerabilities others overlook by thinking in systems — analyzing misalignments between how AWS services claim to work and how they actually behave.

This isn't a course. It isn't a copied framework. It's built from scratch, one service at a time.

---

## How I Think

I draw systems maps by hand for each AWS service before I touch a tool:

- **Concept Map** — what is this service and how does it connect to its ecosystem?
- **Behavioral Stock/Flow Map** — how does the service behave over time? What flows in, what flows out, what feedback loops exist?
- **Trust/Permission Propagation Map** — what trusts what? How does authority flow? Where are the leverage points?
- **Assumption Analysis** — what does everyone assume is true? What breaks those assumptions? What's the blast radius?

This forces me to understand the system before I look for vulnerabilities in it.

**Services mapped so far:**

| Service | Concept Map | Behavioral Map | Trust/Permission Map | Assumption Analysis |
|---------|------------|---------------|---------------------|-------------------|
| [Lambda](./How-I-Think/Lambda/) | ✅ | ✅ | ✅ | ✅ |
| [S3](./How-I-Think/S3/) | ✅ | ✅ | ✅ | ✅ |
| [Fargate](./How-I-Think/Fargate/) | ✅ | ✅ | ✅ | 🔄 |

---

## How I Work

My methodology for finding AWS vulnerabilities is built around one framework: **FIND → FOCUS → FIRE**

Reconnaissance to exploitation, structured and repeatable.

→ [See the full framework](./How-I-Work/FIND-FOCUS-FIRE.md)

---

## Tools

Scanners and automation built from what the systems maps reveal. *(In progress)*

---

## Why This Exists

I manage an unknown illness that prevents me from working a normal job. Curiosity doesn't stop, so I don't stop. I'm building this in public, one service at a time, until the methodology is complete enough to find what others miss.
