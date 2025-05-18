# Technology Stack

This document outlines the planned technology stack for the AI Crypto Trading Agent.

## Core Components

*   **Programming Language**: Python
*   **Containerization**: Docker

## Data Acquisition

*   **Web Scraping**:
    *   Playwright (for dynamic websites, using `mcp_playwright-mcp_*` tools)
    *   Exa AI tools (`mcp_exa_web_search_exa`, `mcp_exa_crawling` for targeted search and crawling)
    *   Standard Python libraries (Requests/BeautifulSoup for simpler static sites)
*   **News APIs**: (To be researched - e.g., CryptoCompare News API, NewsAPI.org, or custom scraping if necessary)

## Data Storage & Management

*   **Knowledge Graph**: `mcp_servers_*` tools for creating, populating, and querying a knowledge graph. This will store entities (assets, news, events) and their relationships.
*   **Local Database**: (Optional, for extensive logs, historical price data not in KG - e.g., SQLite)

## AI & Decision Making

*   **Natural Language Processing (NLP)**:
    *   Libraries like NLTK, spaCy, or Hugging Face Transformers (for sentiment analysis, named entity recognition from news).
*   **Decision Engine**:
    *   `mcp_clear-thought_decisionframework`: To structure and make trading decisions.
    *   `mcp_clear-thought_sequentialthinking`: To define the agent's operational logic.
    *   `mcp_clear-thought_metacognitivemonitoring`: For the agent to self-assess its decision confidence.
    *   `mcp_clear-thought_scientificmethod`: Potentially for designing and testing trading hypotheses.
*   **Machine Learning Libraries**: (Optional, for advanced predictive modeling - e.g., Scikit-learn, TensorFlow/PyTorch).

## Trading Execution

*   **Exchange APIs**: Client libraries for exchanges (e.g., Binance, Kraken, Coinbase Pro via `ccxt` or official libraries).
    *   *User will be responsible for secure API key management and direct implementation of trading calls.*
    *   `mcp_context7-mcp_get-library-docs` can be used to fetch documentation for these libraries.

## Development & Operations

*   **Version Control**: Git & GitHub
*   **Dependency Management**: `requirements.txt` (Python)
*   **Local Interaction**: `mcp_desktop-commander_*` tools for file operations and command execution during development.
