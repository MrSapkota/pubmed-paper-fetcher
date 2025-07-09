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


---

### 🧪 Run the Program

Use this command to fetch papers from PubMed:

```bash
poetry run get-papers-list "your pubmed query" -f output.csv




---

### ⚙️ Add the **CLI Options Section**
```markdown
---

### ⚙️ Command-Line Options

| Option | Description                    |
|--------|--------------------------------|
| `-h`, `--help`  | Show help message       |
| `-d`, `--debug` | Print debug information |
| `-f`, `--file`  | Save output to CSV file |


---

## 🧠 Filtering Heuristics

To detect non-academic authors, we apply keyword-based filtering.

### Excluded (academic) affiliations:
- `university`, `institute`, `college`, `school`, `hospital`, `labs`

### Included (company) keywords:
- `Inc.`, `Ltd.`, `LLC`, `Biotech`, `Pharma`, `Therapeutics`, `Life Sciences`

If any author has a non-academic affiliation, the paper is included in the output.


---

## 📤 Output Format

The tool creates a CSV with the following columns:

| Column | Description |
|--------|-------------|
| PubmedID | Unique paper identifier |
| Title | Title of the paper |
| Publication Date | Date the paper was published |
| Non-academic Author(s) | Author names from pharma/biotech |
| Company Affiliation(s) | Extracted pharma/biotech affiliations |
| Corresponding Author Email | Email of the corresponding author (if available) |


---

## 📁 Project Structure

Mukul_portfolio/
├── pubmed_paper_fetcher/
│ ├── fetch.py
│ ├── utils.py
│ ├── models.py
├── cli.py
├── get_papers_list.py
├── pyproject.toml
├── README.md
├── report.md

## 🤖 LLM Assistance

ChatGPT was used throughout the project to:

- Plan architecture
- Debug API requests and response parsing
- Refine filtering heuristics
- Design CLI commands with Typer

👉 [View LLM conversation](https://chatgpt.com/share/686e376a-3dac-800a-9934-37868e861bd2)

## 📽️ Video Demonstration

A video walkthrough is included with this submission. It demonstrates:

- Code structure
- How the CLI is used
- Output verification with example results

[🔗 Video Link](https://drive.google.com/file/d/1iZWHCt-anc2Mx8Ytl4Lb1K9SNwFmT6_p/view?usp=sharing)


## 👨‍💻 Author

**Mukul Sapkota**  
📧 mukulsapkota29@gmail.com  
🌐 [LinkedIn](https://linkedin.com/in/mukul-sapkota-8250481b4)
