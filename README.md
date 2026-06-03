# 💰 Advanced Hybrid RAG Financial Intelligence Engine

### 🚀 Financial Intelligence Powered by Hybrid RAG & Fine-Tuned LLMs
*Comparing Retrieval-Augmented Generation (RAG) and Fine-Tuned Large Language Models for Financial Question Answering*

---

## 📖 Overview

Financial reports contain critical business insights, but extracting meaningful information from lengthy annual reports, financial statements, and corporate disclosures can be time-consuming and challenging. 

This project explores two advanced architectural approaches for financial document intelligence:

### 🔍 Hybrid RAG Pipeline
* **Semantic Retrieval:** Uses deep vector embeddings to capture conceptual meaning.
* **Keyword-Based Search:** Integrates traditional sparse BM25 matching for exact terms and precise figures.
* **Cross-Encoder Reranking:** Computes deep attention-based relevance scores to maximize context quality.
* **Grounded Generation:** Enforces strict context-awareness to drastically minimize hallucinations.

### 🧠 Fine-Tuned LLM
* **Llama 3 8B Base:** Adapted specifically for the nuances of financial domain terminology.
* **QLoRA Fine-Tuning:** Parameter-efficient training designed to minimize VRAM footprints.
* **Unsloth Acceleration:** Leverages highly optimized compute kernels to accelerate training phases.
* **Quantized Deployment:** Packaged for resource-efficient execution on cost-effective hardware.

The primary objective of this project was to benchmark both methodologies, evaluating their accuracy, resource footprint, and overall operational reliability when answering complex financial queries.

---

## ✨ Key Features

### 🔎 Hybrid RAG Architecture
* ✅ Automated end-to-end document ingestion pipeline
* ✅ Intelligent, semantic-aware text chunking strategies
* ✅ Production-grade Weaviate vector database integration
* ✅ Dual-channel hybrid retrieval engine (Dense + Sparse)
* ✅ Cross-Encoder secondary reranking layer
* ✅ Deterministic context-aware response generation

### 🧠 Fine-Tuned Language Model
* ✅ Llama 3 8B domain-specific fine-tuning
* ✅ QLoRA parameter-efficient training execution
* ✅ Unsloth compilation for accelerated training cycles
* ✅ Deep financial domain linguistic specialization
* ✅ Native support for low-bit quantized deployment

### 📊 Evaluation Framework
* ✅ Direct Hybrid RAG vs. Fine-Tuned LLM benchmarking
* ✅ Deterministic accuracy evaluation matrices
* ✅ Granular retrieval and context-window quality assessments
* ✅ Comparative response quality analysis
* ✅ End-to-end token latency and Time-To-First-Token (TTFT) measurements
* ✅ Hallucination rate and variance comparison

### 💻 Interactive User Interface
* ✅ Streamlit-powered analytical dashboard
* ✅ Multi-source financial document querying interface
* ✅ On-the-fly AI-generated comparative insights
* ✅ Side-by-side model response inspection workspace
* ✅ Highly intuitive, user-friendly data workflows

---

## 🛠️ Tech Stack

### 🤖 Artificial Intelligence & Machine Learning
| Technology | Purpose |
| :--- | :--- |
| **Python** | Core Application Development |
| **Llama 3 8B** | Foundational Base Language Model |
| **QLoRA** | Parameter-Efficient Fine-Tuning Framework |
| **Unsloth** | Accelerated Compute Training Framework |
| **Hugging Face Transformers** | Model Lifecycle & Weight Management |
| **Sentence Transformers** | Dense Embedding Token Vectorization |

### 🔍 Retrieval & Search
| Technology | Purpose |
| :--- | :--- |
| **Weaviate** | Enterprise-Grade Vector Database Engine |
| **Hybrid Search** | Combined Sparse (BM25) and Dense Retrieval Channels |
| **Dense Retrieval** | Semantic Vector Search Execution |
| **Sparse Retrieval** | Precision-Based Keyword Token Matching |
| **Cross-Encoder** | Deep Neural Relevance Reranking Layer |

### ⚙️ Backend & Processing
* Python
* Pandas
* NumPy

### 🎨 Frontend
* Streamlit

---

## 🏗️ System Architecture

```text
📄 Financial Report
          │
          ▼
📥 Document Ingestion
          │
          ▼
✂️ Text Chunking
          │
          ▼
🧩 Embedding Generation
          │
          ▼
🗄️ Weaviate Vector Database
          │
          ▼
🔍 Hybrid Retrieval (Semantic + Keyword Search)
          │
          ▼
🎯 Cross Encoder Reranking
          │
          ▼
📚 Context Construction
          │
          ▼
🤖 LLM Response Generation
