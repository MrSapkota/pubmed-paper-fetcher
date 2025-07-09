# pubmed-paper-fetcher
Python CLI to fetch PubMed papers with non-academic authors

# PubMed Paper Fetcher – CLI Tool

This is a Python command-line tool that fetches research papers from PubMed using a user-specified query and filters them to identify papers with at least one author affiliated with a pharmaceutical or biotech company. Results are saved in a CSV format.

## 📌 Features

- ✅ Fetches papers using the PubMed API
- ✅ Applies heuristics to filter non-academic authors
- ✅ Extracts affiliations and corresponding author emails
- ✅ Outputs clean CSV with all required fields
- ✅ Command-line interface built with Typer
- ✅ Typed Python and Poetry-based environment
- ✅ Includes `--debug` mode and `--file` CSV export option

---

## 🚀 Quick Start

### 🧾 Prerequisites
- Python 3.8 or later
- Poetry (Install from: https://python-poetry.org/docs/#installation)

### 📥 Installation
Clone the repo and install dependencies:
```bash
git clone https://github.com/MrSapkota/Mukul_portfolio.git
cd Mukul_portfolio
poetry install
