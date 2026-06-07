# Fargate Systems Thinking

This folder contains my systems-thinking analysis of AWS Fargate and its ecosystem (ECS and ECR).

The goal is not just to understand Fargate as a service, but to understand:

- behavioral dynamics
- container lifecycle and trust relationships
- permission propagation through ECS, ECR, and task roles
- leverage points
- misalignments
- attack paths
- and systemic security risk

These maps are part of my broader effort to develop a structured AWS security methodology focused on understanding how cloud systems behave and how compromise propagates through interconnected services.

---

## Maps

### Fargate Concept Map ✅
A visual reference showing the full Fargate ecosystem — how developers build container images, how ECR stores them, how ECS orchestrates deployment, and how Fargate runs them with task roles and metadata endpoints.

Key relationships captured:
- Developer/CI-CD builds images → stored in ECR
- ECS pulls from ECR and deploys to Fargate
- Fargate runs containers with attached task roles
- Metadata endpoint `169.254.170.2` provides temporary credentials
- VPC, Security Groups, and Private Link control network access
- Account Settings govern all features

---

### Fargate Behavioral Stock/Flow Map ✅
Focuses on:
- running tasks and services (stock)
- ECS as the controller of both inflow and outflow
- input valves: Task Definition, VPC/Security Groups, Task Role, Platform Version
- output valves: ECS Health Check, Service Auto Scaling, Platform Version Retirement
- Service Auto Scaling balancing loop with delay (B)
- Platform Version Retirement balancing loop (B)
- leverage points: Access Controls and Task/Execution categories
Questions explored:
- What controls whether a task starts or stops?
- Why does output matter as much as input?
- What feedback loops automatically manage running tasks?
- Where do misconfigurations silently expose the system?

---

### Fargate Trust / Permission Propagation Map ✅
Focuses on two trust paths — legitimate (Person/System/Service → ECS → Fargate → Task Role) and attack path (SSRF → metadata endpoint → Task Role credentials). Four leverage points: Task Role, SSRF via vulnerable app, ECR permissions, ECS control plane.

---

### Fargate Assumption Analysis
*In progress*
