# Human-in-the-Loop Benchmarking of Heterogeneous LLMs for Automated Competency Assessment in Secondary Level Mathematics

- Source: arxiv
- ID: http://arxiv.org/abs/2604.26607v1
- DOI: 명시되지 않음
- Published: 2026-04-29T12:36:19Z
- Authors: Jatin Bhusal, Nancy Mahatha, Aayush Acharya, Raunak Regmi
- Categories: cs.AI, cs.CY, cs.SE
- Link: https://arxiv.org/abs/2604.26607v1
- PDF: https://arxiv.org/pdf/2604.26607v1
- Keyword Score: 8

## Abstract
As Competency-Based Education (CBE) is gaining traction around the world, the shift from marks-based assessment to qualitative competency mapping is a manual challenge for educators. This paper tackles the bottleneck issue by suggesting a "Human-in-the-Loop" benchmarking framework to assess the effectiveness of multiple LLMs in automating secondary-level mathematics assessment. Based on the Grade 10 Optional Mathematics curriculum in Nepal, we created a multi-dimensional rubric for four topics and four cross-cutting competencies: Comprehension, Knowledge, Operational Fluency, and Behavior and Correlation.   The multi-provider ensemble, consisted of open-weight models -- Eagle (Llama 3.1-8B) and Orion (Llama 3.3-70B) -- and proprietary frontier models Nova (Gemini 2.5 Flash) and Lyra (Gemini 3 Pro), was benchmarked against a ground truth defined by two senior mathematics faculty members (kappa_w = 0.8652). The findings show a marked "Architecture-compatibility gap". Although the Gemini-based Mixture-of-Experts (Sparse MoE) models achieved "Fair Agreement" (kappa_w ~ 0.38), the larger Orion (70B) model exhibited "No Agreement" (kappa_w = -0.0261), suggesting that architectural compliance with instruction constraints outweighs the scale of raw parameters in rubric-constrained tasks. We conclude that while LLMs are not yet suitable for autonomous certification, they provide high-value assistive support for preliminary evidence extraction within a "Human-in-the-Loop" framework.

## OpenAI Review
(OpenAI review failed: 429 Client Error: Too Many Requests for url: https://api.openai.com/v1/chat/completions)
