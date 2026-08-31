# 📚 ResearchFlow AI

## AI-Powered Research Assistant for Scientific Literature

ResearchFlow AI is an AI-assisted research workspace designed to help students, researchers, and academics understand scientific literature faster.

Users can upload research papers, extract their content, generate structured summaries, ask questions about papers, and compare research findings.

---

## ✨ Features

### 📄 Research Paper Upload

Upload scientific papers in PDF format and automatically extract readable text.

### 🧠 Structured Research Summaries

ResearchFlow organizes papers into:

- Executive Summary
- Key Findings
- Methodology
- Limitations
- Future Research

### 💬 Ask the Paper

Users can ask natural-language questions about an uploaded research paper.

### 🔬 Paper Comparison

Compare two papers based on:

- Research objectives
- Methodology
- Findings
- Limitations

---

## 🏗️ Architecture

```text
             Research Paper
                    │
                    ▼
               PDF Parser
                    │
                    ▼
             Extracted Text
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       Summary      Q&A    Comparison
          │         │         │
          └─────────┼─────────┘
                    ▼
              ResearchFlow
                   UI
