# 🧠 AI Agent Frameworks & Coding Agents

This page collects the most relevant **agentic frameworks** across **Python**, **JavaScript/TypeScript**, **Go**, and **JVM** ecosystems — useful for building LLM-powered coding assistants, multi-agent systems, and autonomous workflows.

## Agent Frameworks

### Python

| Framework | Description / Highlights | License | GitHub Stars |
| ----------| ------------------------ | ------- | ------------ |
| **[LangChain](https://github.com/langchain-ai/langchain)** | Modular LLM framework (chains, tools, memory, planners). The agent engineering platform. | MIT | 137k |
| ~~**[AutoGen (Microsoft)](https://github.com/microsoft/autogen)**~~ | ~~Multi-agent message-passing framework.~~ ⚠️ Now in **maintenance mode** — new projects should use [Microsoft Agent Framework](https://github.com/microsoft/agent-framework). | MIT | ~~58.1k~~ |
| **[CrewAI](https://github.com/crewAIInc/crewAI)** | Multi-agent orchestration with roles and collaboration. Standalone, no LangChain dependency. | MIT | 51.5k |
| **[LlamaIndex](https://github.com/run-llama/llama_index)** | Context & retrieval-first agentic framework, integrates with tools and chat. | MIT | 49.4k |
| **[Aider](https://github.com/Aider-AI/aider)** | CLI coding agent editing repos using GPT/Claude + git diffs. | Apache-2.0 | 44.8k |
| **[LangGraph](https://github.com/langchain-ai/langgraph)** | Stateful graph-based agent orchestration. Durable execution, human-in-the-loop. | MIT | 32.1k |
| **[smolagents](https://github.com/huggingface/smolagents)** | HuggingFace's minimal code-first agent library. `CodeAgent` writes actions as Python, runs in sandboxed envs (E2B, Modal, Docker). | Apache-2.0 | 27.3k |
| **[OpenAI Agents SDK](https://github.com/openai/openai-agents-python)** | Official SDK for building multi-step reasoning agents with tool calling, memory, and loops. | MIT | 26.3k |
| **[Google ADK Python](https://github.com/google/adk-python)** | Google’s code-first Python agent framework. Multi-agent orchestration, evals, deployment. Gemini-optimized, model-agnostic. | Apache-2.0 | 19.6k |
| **[PydanticAI](https://github.com/pydantic/pydantic-ai)** | FastAPI-inspired agent framework by the Pydantic team. Fully type-safe, model-agnostic, with dependency injection and graph support. | MIT | 17.1k |
| **[Anthropic APIs](https://docs.anthropic.com/)** | Native Claude agent capabilities — tool use + computer use. | Proprietary | (not applicable) |

### JavaScript / TypeScript (JS/TS)

| Framework | Description / Highlights | License | GitHub Stars |
| --------- | ------------------------ | ------- | ------------ |
| **[Vercel AI SDK](https://github.com/vercel/ai)** | Provider-agnostic TypeScript SDK from the Next.js team. Streaming UI, structured outputs, agentic loops. | Apache-2.0 | 24.2k |
| **[Mastra](https://github.com/mastra-ai/mastra)** | TypeScript-native agent framework by the Gatsby team. Agents, graph-based workflows, RAG, evals, human-in-the-loop, MCP server authoring, and observability out of the box. | Apache-2.0 | 23.9k |
| **[ElizaOS](https://github.com/elizaOS/eliza)** | Multi-agent runtime with rich plugin ecosystem. Built for social/conversational agents. | MIT | 18.4k |
| **[LangChain.js](https://github.com/langchain-ai/langchainjs)** | JS/TS agent platform. Chains, tools, memory, retrievers. Runs anywhere JS runs. | MIT | 17.7k |
| **[OpenAI Agents SDK JS](https://github.com/openai/openai-agents-js)** | Official OpenAI TypeScript SDK. Agents, handoffs, guardrails, tracing, voice agents. | MIT | 3k |
| **[LangGraph.js](https://github.com/langchain-ai/langgraphjs)** | Low-level stateful agent orchestration for TypeScript. Graph-based workflows, human-in-the-loop, long-term memory. JS counterpart to Python LangGraph. | MIT | 2.9k |

### Go (Golang)

| Framework | Description / Highlights | License | GitHub Stars |
| --------- | ------------------------ | ------- | ------------ |
| **[Go OpenAI SDK](https://github.com/sashabaranov/go-openai)** | Popular Go client for OpenAI APIs — chat, completions, tools, streaming, DALL·E, Whisper. Good foundation for building custom Go agents. | MIT | 10.7k |
| **[LangChain Go](https://github.com/tmc/langchaingo)** | Go implementation of LangChain. Chains, agents, tools, memory, retrievers, and 20+ LLM provider integrations. | MIT | 9.2k |
| **[Genkit Go](https://github.com/genkit-ai/genkit)** | Google’s production-ready Go AI framework. Flows, tool calling, RAG, structured outputs, multi-provider. | Apache-2.0 | 5.9k |

### JVM (Java / Kotlin)

| Framework | Description / Highlights | License | GitHub Stars |
| --------- | ------------------------ | ------- | ------------ |
| **[LangChain4j](https://github.com/langchain4j/langchain4j)** | Idiomatic Java LLM library (not a LangChain port). Unified API over 20+ providers, 30+ vector stores, MCP, RAG, agents; integrates with Spring Boot, Quarkus, Helidon. | Apache-2.0 | 12k |
| **[Spring AI](https://github.com/spring-projects/spring-ai)** | Official Spring framework for integrating LLMs into Java apps. Supports OpenAI, Anthropic, Mistral, Ollama, and vector stores. | Apache-2.0 | 8.7k |
| **[Koog](https://github.com/JetBrains/koog)** | Kotlin Multiplatform agent framework by JetBrains. Idiomatic Kotlin DSL + Java API, Spring Boot/Ktor integration, MCP, cross-platform (JVM, JS, iOS, Android). | Apache-2.0 | 4.2k |
| **[Embabel](https://github.com/embabel/embabel-agent)** | JVM-native agentic flows framework (Java/Kotlin). Dynamic GOAP planning, goal/action/condition model, Spring-based. By the creator of Spring. | Apache-2.0 | 3.4k |
| **[ADK Java](https://github.com/google/adk-java)** | Google's code-first Java agent framework. Multi-agent orchestration, tools, workflow definitions. Java counterpart to ADK Python. | Apache-2.0 | 1.6k |


## OSS Coding Agents

| Tool | Language | Description / Highlights | License | GitHub Stars |
| ---- | -------- | ------------------------ | ------- | ------------ |
| **[OpenCode](https://github.com/anomalyco/opencode)** | TypeScript | Terminal-based AI coding agent from SST. Fast TUI with support for Claude, GPT-4o, Gemini, and more. | MIT | 161k |
| **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** | TypeScript | Google’s open-source terminal AI agent. Brings Gemini’s large context window and multimodal capabilities to the command line. | Apache-2.0 | 104k |
| **[Codex CLI](https://github.com/openai/codex)** | Rust | OpenAI’s lightweight open-source CLI coding agent. Runs in a sandboxed environment, applies diffs, and executes shell commands. | Apache-2.0 | 82.8k |
| **[Pi](https://github.com/earendil-works/pi)** | TypeScript | Minimal self-extensible terminal coding harness. TypeScript plugin ecosystem, session branching, context compaction. | MIT | 49.7k |
| **[Aider](https://github.com/Aider-AI/aider)** | Python | CLI coding agent that edits repos via GPT/Claude + git diffs. Strong pair-programming workflow, supports 100+ LLMs. | Apache-2.0 | 44.8k |
| **[Crush](https://github.com/charmbracelet/crush)** | Go | Charmbracelet’s terminal-based AI coding assistant with a polished TUI. Supports Claude, OpenAI, and local models. | MIT | 24.3k |
| **[Plandex](https://github.com/plandex-ai/plandex)** | Go | AI coding engine for large, multi-step tasks. Plans and implements changes across many files with rollback support. | AGPL-3.0 | 15.4k |
