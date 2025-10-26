# 🧠 AI Agentic Frameworks & Libraries

This page collects the most relevant **agentic frameworks** across **JVM**, **Python**, and **Go** ecosystems — useful for building LLM-powered coding assistants, multi-agent systems, and autonomous workflows.

##  Agentic Frameworks

### ☕ JVM (Java / Kotlin)

| Framework                                                             | Description / Highlights                                                                                                       | Suitable for Coding Agent? | GitHub Stars |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------- | ------------- |
| **[LangChain4j](https://github.com/langchain4j/langchain4j)**         | Java/Kotlin implementation of LangChain. Provides chains, tools, retrievers, memory, and function calling.                     | ✅ Excellent                | 9.4k          |
| **[Spring AI](https://github.com/spring-projects/spring-ai)**         | Official Spring framework for integrating LLMs into Java apps. Supports OpenAI, Anthropic, Mistral, Ollama, and vector stores. | ✅ Excellent                | 7k            |
| **[Embabel](https://github.com/embabel/embabel-agent)**               | JVM-native agentic flows framework (Java/Kotlin) for authoring agent workflows with goals, actions, planning.                  | ✅ Excellent                | 2.8k          |
| **[Agent Development Kit (ADK)](https://github.com/google/adk-java)** | *Google*’s code-first agent framework for Java (and Python). Multi-agent orchestration, tools, workflow definitions.           | ✅ Excellent                | 773           |
| **[Koog](https://github.com/JetBrains/koog)**                         | Koog is a Kotlin-based framework designed to build and run AI agents entirely in idiomatic Kotlin.                             |                            | 3.3k          |

### 🐍 Python

| Framework                                                               | Description / Highlights                                                                    | Suitable for Coding Agent?      | GitHub Stars          |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------- | ---------------------- |
| **[OpenAI Agents SDK](https://github.com/openai/openai-agents-python)** | Official SDK for building multi-step reasoning agents with tool calling, memory, and loops. | ✅ Excellent                     | (stars not found)      |
| **[Anthropic APIs](https://docs.anthropic.com/)**                       | Native Claude agent capabilities — tool use + computer use.                                 | ✅ Excellent low-level API layer | (stars not applicable) |
| **[LangChain](https://python.langchain.com/)**                          | Modular LLM framework (chains, tools, memory, planners).                                    | ✅ Excellent                     | (stars not found)      |
| **[CrewAI](https://github.com/joaomdmoura/crewAI)**                     | Multi-agent orchestration with roles and collaboration.                                     | ✅ Excellent                     | (stars not found)      |
| **[AutoGen (Microsoft)](https://github.com/microsoft/autogen)**         | Multi-agent message-passing framework (Dev, Reviewer, Tester roles).                        | ✅ Excellent                     | (stars not found)      |
| **[LlamaIndex](https://gpt-index.readthedocs.io/)**                     | Context & retrieval-first agentic framework, integrates with tools and chat.                | ⚙️ Good                         | (stars not found)      |
| **[Aider](https://github.com/Aider-AI/aider)**                          | CLI coding agent editing repos using GPT/Claude + git diffs.                                | ✅ Excellent                     | (stars not found)      |

### 🦫 Go (Golang)

| Framework / Project                                             | Description / Highlights                                                                                      | Suitable for Coding Agent? | GitHub Stars    |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | -------------------------- | ----------------- |
| **[Agent SDK Go](https://github.com/Ingenimax/agent-sdk-go)**   | Full-featured Go SDK for agents: multi-LLM (OpenAI, Anthropic, Gemini), tool integration, structured outputs. | ✅ Excellent                | ~278              |
| **[Plandex](https://github.com/plandex-ai/plandex)**            | Go-based **coding agent** for large codebases; supports diffs, sandboxed edits, and multiple model backends.  | ✅ Excellent                | (stars not found) |
| **[Go-Calque](https://github.com/calque‐ai/go-calque)**         | Idiomatic Go agent framework: streaming-first, supports LLMs, tools, memory, concurrency.                     | ✅ Excellent                | (stars not found) |
| **[AgentKit](https://agentkit.tech/docs/intro)**                | Toolkit for LLM agents in Go: abstracts providers, manages conversations, tools, streaming.                   | ✅ Good                     | (stars not found) |
| **[Goated Agents](https://github.com/bcanfield/goated-agents)** | Chain-of-thought and tool orchestration in Go, lightweight and extensible.                                    | ⚙️ Good                    | (stars not found) |
| **[Go OpenAI SDK](https://github.com/sashabaranov/go-openai)**  | Popular Go client for OpenAI APIs with tool-calling and streaming; good base for custom agents.               | ⚙️ Good foundation         | (stars not found) |

### ⚡ Quick Comparison Summary

| Language              | Best Mature Frameworks                        | Learning Curve   | Ideal Use Case                                                                | Ecosystem Maturity    |
| --------------------- | --------------------------------------------- | ---------------- | ----------------------------------------------------------------------------- | --------------------- |
| **Python**            | LangChain, CrewAI, AutoGen, OpenAI Agents SDK | 🟢 Easy → Medium | Building sophisticated multi-tool or multi-agent coding assistants            | 🟢 Very Mature        |
| **JVM (Java/Kotlin)** | LangChain4j, Spring AI, Embabel, ADK, Koog    | 🟠 Medium → Hard | Enterprise or backend AI services; integrating AI into Spring or Quarkus apps | 🟠 Growing Fast       |
| **Go (Golang)**       | Go-Calque, Agent SDK Go, Plandex              | 🟢 Easy → Medium | CLI-based or service-oriented code assistants; high performance tools         | 🟡 Emerging but solid |


## 🧰 Open-Source Coding Agents Comparison

| Tool                                                      | Language Support | GitHub Repository                                                       |
| --------------------------------------------------------- | ---------------- | ----------------------------------------------------------------------- |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | TypeScript       | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| [Codex CLI](https://github.com/openai/codex)              | Rust             | [openai/codex](https://github.com/openai/codex)                         |
| [Aider](https://github.com/Aider-AI/aider)                | Python           | [Aider-AI/aider](https://github.com/Aider-AI/aider)                     |
| [Plandex](https://github.com/plandex-ai/plandex)          | Go               | [plandex-ai/plandex](https://github.com/plandex-ai/plandex)             |
| [OpenCode](https://github.com/opencode-ai/opencode)       | Go, JavaScript   | [opencode-ai/opencode](https://github.com/opencode-ai/opencode)         |
| [Open-Codex](https://github.com/codingmoh/open-codex)     | Go               | [codingmoh/open-codex](https://github.com/codingmoh/open-codex)         |
