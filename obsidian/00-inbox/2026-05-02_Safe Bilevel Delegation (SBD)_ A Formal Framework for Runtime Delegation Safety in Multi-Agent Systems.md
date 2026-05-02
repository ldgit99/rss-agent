# Safe Bilevel Delegation (SBD): A Formal Framework for Runtime Delegation Safety in Multi-Agent Systems

- Source: arxiv
- ID: http://arxiv.org/abs/2604.27358v1
- DOI: 명시되지 않음
- Published: 2026-04-30T03:15:05Z
- Authors: Yuan Sun
- Categories: cs.AI
- Link: https://arxiv.org/abs/2604.27358v1
- PDF: https://arxiv.org/pdf/2604.27358v1
- Keyword Score: 6

## Abstract
As large language model (LLM) agents are deployed in high-stakes environments, the question of how safely to delegate subtasks to specialized sub-agents becomes critical. Existing work addresses multi-agent architecture selection at design time or provides broad empirical guidelines, but neither provides a runtime mechanism that dynamically adjusts the safety-efficiency trade-off as task context changes during execution.   We propose Safe Bilevel Delegation (SBD), a formal framework for runtime delegation safety in hierarchical multi-agent systems. SBD formulates task delegation as a bilevel optimization problem: an outer meta-weight network phi learns context-dependent safety-efficiency weights lambda(s) in [0,1]; an inner loop optimizes the delegation policy pi subject to a probabilistic safety constraint P(safe) >= 1-delta. The continuous delegation degree alpha in [0, 1] controls how much decision authority is transferred to each sub-agent, interpolating smoothly between full human override (alpha=0) and fully autonomous execution (alpha=1).   We establish three theoretical results: (1) Safety Monotonicity--higher outer safety weight produces a weakly safer inner policy; (2) Inner Policy Convergence--projected gradient descent on the inner problem converges linearly under standard smoothness assumptions; (3) an Accountability Propagation bound that distributes responsibility across multi-hop delegation chains with a provable per-agent ceiling. We instantiate SBD in three high-stakes domains--medical AI (MIMIC-III), financial risk control (S and P 500), and educational agent supervision (ASSISTments)--specifying datasets, safety constraint sets, baselines, and evaluation protocols. This manuscript presents the formal framework and theoretical results in full; empirical validation following the protocols described herein is planned and will be reported in a forthcoming revision.

## OpenAI Review
(OpenAI review failed: 429 Client Error: Too Many Requests for url: https://api.openai.com/v1/chat/completions)
