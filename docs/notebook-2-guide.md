# Context Engineering: Selecting Context
## Guide to Notebook 2

---

## Executive Summary

**The Problem:** AI systems can access vast amounts of information, but giving them *everything* is expensive and confusing.

**The Solution:** "Context Selection" — intelligently choosing *only* the relevant information for each task.

**The Impact:** Faster responses, lower costs, better accuracy, and ability to handle larger knowledge bases.

---

## What is Context Selection?

Think about a reference librarian:

| Librarian | AI System |
|-----------|-----------|
| Doesn't read the entire library when you ask | Shouldn't need all data to answer |
| Selects relevant books based on topic | Needs mechanism to select relevant context |
| Brings exactly what you need | Should retrieve only pertinent information |

**Context Selection** = choosing the right subset of information from a larger pool.

---

## The Core Challenge

Imagine an AI assistant with access to:
- 10,000 company documents
- 50,000 customer records  
- 5,000 product descriptions
- All email history (millions of messages)

**Problem:** You can't feed all this to the AI for every question. It would:
- Cost too much (more tokens = higher API bills)
- Take too long (processing delays)
- Confuse the AI (noise overwhelms signal)

**Solution:** Select only what's relevant for each specific query.

---

## Notebook 2: Selecting Context

### Strategy 1: Scratchpad Selection

**Concept:** The AI writes intermediate results to state, then reads them back later.

```
┌─────────────────────────────────────────────────────┐
│                    WORKFLOW                         │
│                                                      │
│  Step 1: Generate initial joke                       │
│          ↓ Write to state                           │
│  Step 2: Read joke from state → Improve it          │
│          ↓ Write improved version to state          │
│  Step 3: Read both → Select best one                │
└─────────────────────────────────────────────────────┘
```

**Use case:** Multi-step content creation
- Draft → Review → Revise → Finalize
- Each step reads previous work from state

---

### Strategy 2: Memory Selection

**Concept:** Store important information long-term, retrieve it when relevant.

```
┌─────────────────────────────────────────────────────┐
│                   MEMORY STORE                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │ User prefs  │  │ Past jokes  │  │ Research    │ │
│  │ "concise"   │  │ [...data...]│  │ [...data...]│ │
│  └─────────────┘  └─────────────┘  └─────────────┘ │
└─────────────────────────────────────────────────────┘
         ↓                    ↓                    ↓
    Search by key        Search by topic     Semantic search
```

**Use cases:**
- **Personalization:** Remember preferences across sessions
- **Consistency:** Avoid repeating the same mistakes
- **Learning:** Build up knowledge over time

**Example:**
```
Session 1: AI generates joke about cats
           ↓ Stored in memory
Session 2: AI reads previous joke first
           ↓ Generates different joke (avoiding repetition)
```

---

### Strategy 3: Tool Selection

**Concept:** AI has access to many tools, but should only use relevant ones.

**The tool overload problem:**
```
AI with 500 tools:
- Gets confused about which to use
- Spends tokens processing tool descriptions
- Makes wrong choices
```

**Three selection approaches:**

| Approach | Tool Count | Method | Example |
|----------|------------|--------|---------|
| **Direct binding** | < 50 | Give AI all tools, let it choose | Small dashboard |
| **Categorization** | 50-200 | Group by domain, select category | Department-specific tools |
| **Semantic search** | 200+ | Search tool descriptions | Enterprise catalog |

**Example:**

*Direct binding* (small tool set):
```
Agent with 5 tools:
- Look up order
- Process refund
- Check inventory
- Schedule delivery
- Update profile

→ AI can handle seeing all 5 at once
```

*Categorization* (medium tool set):
```
Query: "Help with my refund"
→ Select: billing_tools only

Query: "Where's my package?"
→ Select: shipping_tools only
```

*Semantic search* (large tool set):
```
Query: "Calculate monthly recurring revenue"
→ Search finds relevant tools
→ AI gets only relevant subset
```

---

### Strategy 4: Knowledge Retrieval (RAG)

**Concept:** Search a knowledge base for documents relevant to the question.

```
┌─────────────────────────────────────────────────────┐
│                    RAG FLOW                         │
│                                                      │
│  Question → Search documents                        │
│                  ↓                                  │
│              Find relevant chunks                    │
│                  ↓                                  │
│              Add to AI context                        │
│                  ↓                                  │
│              AI answers using retrieved info        │
└─────────────────────────────────────────────────────┘
```

**Value:**

| Without RAG | With RAG |
|-------------|----------|
| AI trained only on public data | AI knows your proprietary info |
| "I don't know about our products" | "Here's our product catalog..." |
| Hallucinates answers | Grounded in actual documents |

**Applications:**
- **Support:** Search knowledge base for help articles
- **Legal:** Find relevant cases and precedents
- **Research:** Retrieve papers on specific topics
- **HR:** Answer questions about policies

---

## Why This Matters

### Cost Reduction

| Scenario | Without Selection | With Selection | Savings |
|----------|-------------------|----------------|---------|
| Support query | 100,000 tokens | 5,000 tokens | 95% |
| HR question | 50,000 tokens | 3,000 tokens | 94% |

### Improved Accuracy

```
Too much context:
AI: "I found information in 12 different documents.
     Here are conflicting policies..." (confused)

Selected context:
AI: "According to our return policy (section 4.2), you have
     30 days to return items in original condition." (clear)
```

### Better Experience

```
Without selection:
User: "What's our refund policy?"
AI: [30 second delay]
AI: "Here's everything I found..." (overwhelming)

With selection:
User: "What's our refund policy?"
AI: [2 second delay]
AI: "You have 30 days for most items..." (concise)
```

---

## Key Takeaways

| Strategy | When to Use | Benefit |
|----------|-------------|--------|
| **Scratchpad selection** | Multi-step workflows | Each step builds on previous work |
| **Memory selection** | Cross-session persistence | Personalized, consistent experiences |
| **Tool selection** | Many tools available | Faster, more accurate tool use |
| **Knowledge retrieval** | Large document collections | Grounded answers from your data |

**Context Selection = giving AI the right information at the right time.**

---

## Questions for Discussion

1. **What information do our AI systems currently process that could be filtered out?**
2. **Where would tool selection improve accuracy?**
3. **What knowledge should be retrievable (RAG) vs. stored in memory?**
4. **How much could we save by selecting only relevant context?**

---

## Further Reading

- Notebook 1: Writing Context — creating the scratchpad
- Notebook 3: Compressing Context — summarizing to save space
- Notebook 4: Isolating Context — splitting complex problems
