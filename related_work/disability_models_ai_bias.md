# Disability Models and AI Bias

## Paper Analysis: Newman-Griffis et al. (2022)

### Citation
Newman-Griffis, D., Rauchberg, J.S., Alharbi, R., Hickman, L., & Hochheiser, H. (2022). Definition drives design: Disability models and mechanisms of bias in AI technologies. arXiv:2206.08287 [cs.AI].

### Problem
The paper addresses how bias emerges in AI applications that make decisions affecting disabled people. Current efforts to address algorithmic bias fail to understand the broader mechanisms through which bias emerges, particularly how fundamental design decisions about disability definitions create systematic bias.

### Prior Assumptions
Prior work assumes that:
- AI bias can be addressed primarily through algorithmic fixes
- Disability categories are stable and objectively definable
- Technical solutions alone can address bias in AI systems
- The definition of disability is neutral and doesn't influence system design

### Insight
**Key Innovation**: Bias in AI emerges not just from algorithms but from fundamental design decisions about how disability is conceptualized. The authors show that different models of disability (medical, social, political-relational) lead to completely different AI system designs with different bias patterns.

### Technical Approach
The paper uses a framework analysis examining three historical models of disability:
1. **Medical Model**: Disability as individual pathology requiring cure/treatment
2. **Social Model**: Disability as socially constructed barriers
3. **Political-Relational Model**: Disability as dynamic interaction between person and environment

For each model, they analyze how it influences:
- Problem formulation
- Data selection
- Technology application
- Operational design elements

### Evaluation
The paper provides qualitative analysis through case studies showing how different disability models lead to different AI design decisions. However, it lacks empirical validation of the proposed framework.

### Impact
**Relevance to Our Research**: This directly supports our Assumption 4 hypothesis that "disability categories are fixed medical conditions" is problematic. The paper shows disability is dynamically constructed through technological and social context, making genetic "correction" philosophically incoherent.

**Broader Impact**: Challenges the field to consider how fundamental conceptual frameworks, not just algorithms, create bias in AI systems.