# Context Engineering with LangGraph

Strategies for managing AI context: **write, select, compress, and isolate**.

## Overview

AI systems have limited "working memory" (context windows). When tasks get complex, they forget important information, costs explode, and accuracy suffers.

**Context Engineering** is the art and science of filling the context window with just the right information at each step.

> "Context engineering is the delicate art and science of filling the context window with just the right information for the next step." — Andrej Karpathy

## What You'll Learn

| Strategy | Problem | Solution |
|----------|---------|----------|
| **Write** | AI forgets between steps | State objects & memory stores |
| **Select** | Too much irrelevant data | Tool & memory selection |
| **Compress** | Conversations hit limits | Summarization techniques |
| **Isolate** | One AI can't do everything | Multi-agent systems |

## Quickstart

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) package manager
- OpenAI API key

### Installation

```bash
# Clone the repository
git clone https://github.com/anguyenbus/context_engineering
cd context_engineering

# Create virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv sync
```

### Configuration

Create a `.env` file in the project root:

```bash
OPENAI_API_KEY=your-openai-api-key
```

## Notebooks

```
context_engineering/
├── 1_write_context.ipynb      # State, checkpointing, long-term memory
├── 2_select_context.ipynb     # Memory retrieval, tool selection, RAG
├── 3_compress_context.ipynb   # Summarization, token optimization
└── 4_isolate_context.ipynb    # Multi-agent systems, sandboxing
```

### 1. Write Context

Saving information outside the context window to help an agent perform a task.

**Topics:**
- State objects for multi-step workflows
- Checkpointing for fault tolerance
- Long-term memory with InMemoryStore

**Key Takeaway:** Give AI a scratchpad to write down intermediate results.

### 2. Select Context

Pulling relevant information into the context window.

**Topics:**
- Memory selection (namespace-based retrieval)
- Tool selection strategies (direct, categorization, semantic search)
- RAG for knowledge retrieval

**Key Takeaway:** Choose only what's relevant — 95% cost reduction possible.

### 3. Compress Context

Retaining only the tokens required to perform a task.

**Topics:**
- Conversation summarization (115k → 60k tokens demonstrated)
- Tool output compression
- Message trimming strategies

**Key Takeaway:** Summarize periodically for longer conversations.

### 4. Isolate Context

Splitting up context to handle complex tasks.

**Topics:**
- Multi-agent systems with supervisor pattern
- Specialized agents (research, math, writing)
- Sandbox execution for safety

**Key Takeaway:** Specialized agents outperform generalists by 90%.

## Documentation

Detailed guides for each notebook are available in the `docs/` folder:

- [Overview Guide](docs/overview-guide.md) — Complete context engineering overview
- [Notebook 1 Guide](docs/notebook-1-guide.md) — Writing Context
- [Notebook 2 Guide](docs/notebook-2-guide.md) — Selecting Context
- [Notebook 3 Guide](docs/notebook-3-guide.md) — Compressing Context
- [Notebook 4 Guide](docs/notebook-4-guide.md) — Isolating Context

## Dependencies

This project uses:

| Package | Version | Purpose |
|---------|---------|---------|
| langgraph | >=1.0.10 | Agent orchestration |
| langchain | >=0.3.0 | Core LangChain functionality |
| langchain-core | >=1.0.0 | Core abstractions |
| langchain-openai | >=0.2.0 | OpenAI integration |
| langchain-anthropic | >=0.3.0 | Anthropic integration |

See [pyproject.toml](pyproject.toml) for full dependencies.

## Compatibility Notes

**Not included** (incompatible with LangGraph 1.x):
- `langgraph-bigtool` — Use native tool selection instead
- `langchain-sandbox` — Use subprocess-based sandboxing instead

## Background

As LLMs become more like operating systems, the context window is the RAM — limited working memory that must be carefully managed.

According to [Cognition](https://cognition.ai/blog/dont-build-multi-agents):

> "Context engineering" is effectively the #1 job of engineers building AI agents.

## Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Anthropic: Building a Multi-Agent Research System](https://www.anthropic.com/engineering/built-multi-agent-research-system)
- [Context Window Management](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html)

## License

MIT
