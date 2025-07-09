# 📄 Aganitha Take-Home Exercise Report

## 👤 Candidate Details

- **Name**: Mukul Sapkota  
- **Candidate ID**: Direct072025  
- **Email**: mukulsapkota29@gmail.com  
- **GitHub Repo**: (https://github.com/MrSapkota/pubmed-paper-fetcher)  
- **Video Demo**: (https://drive.google.com/file/d/1iZWHCt-anc2Mx8Ytl4Lb1K9SNwFmT6_p/view?usp=sharing)  
- **LLM Chat Link**: (https://chatgpt.com/share/686e376a-3dac-800a-9934-37868e861bd2)

---

## 📌 Problem Summary

The goal was to build a command-line Python tool to fetch research papers from PubMed using a user-defined query and filter them to include only those with at least one author affiliated with a pharmaceutical or biotech company. The output is a CSV file containing detailed metadata about each paper.

---

## 🏗️ Approach & Architecture

- **Programming Language**: Python 3.10  
- **Package Management**: Poetry  
- **CLI Framework**: Typer  
- **PubMed API Used**: `esearch` for IDs, `efetch` for metadata  
- **Code Organization**:
  - `fetch.py`: API logic
  - `utils.py`: Filtering and email extraction
  - `models.py`: Typed models for structured parsing
  - `cli.py`: CLI entrypoint via Typer
- **Executable Command**: `get-papers-list`

---

## 🔍 Methodology

1. **PubMed Fetching**:
   - Used `esearch` API to search for papers by query.
   - Used `efetch` API to retrieve metadata in XML.

2. **Author Affiliation Filtering**:
   - Affiliation strings are matched against academic keywords (e.g., `university`, `school`, `hospital`) to exclude academic authors.
   - Non-academic affiliations are included if they match company indicators (e.g., `Inc.`, `Biotech`, `Therapeutics`, etc.).

3. **Data Extraction**:
   - Parsed titles, authors, publication dates, affiliations, and emails using `xml.etree.ElementTree`.

4. **CSV Generation**:
   - Only papers with at least one non-academic author are included.
   - Exported as a CSV with specified columns.

---

## 🧠 Heuristics Used

- **Academic Keywords** (to exclude):  
  `university`, `college`, `institute`, `school`, `hospital`, `labs`

- **Company Keywords** (to include):  
  `Inc.`, `Ltd.`, `LLC`, `Biotech`, `Pharma`, `Therapeutics`, `Life Sciences`

- **Email Extraction**:  
  Regular expressions were used to extract the email of the corresponding author.

---

## 🧪 Testing & Validation

- Ran queries like `"vaccine development"` and `"oncology clinical trials"` to validate filtering.
- Verified the following:
  - CSV is created correctly.
  - Only non-academic authors are included.
  - Company affiliations appear as expected.
  - Email of the corresponding author is extracted when present.

---

## 🤖 Use of LLMs (ChatGPT)

ChatGPT was used to:
- Help plan and structure the project.
- Debug XML parsing logic and refine filters.
- Refactor CLI using Typer.
- Improve error handling and logging.
- Write this `report.md` and `README.md`.

📎 [https://chatgpt.com/share/686e376a-3dac-800a-9934-37868e861bd2)

---

## 🎯 Outcome

- ✅ Fully functional CLI tool
- ✅ Heuristics applied correctly
- ✅ Output format matches specification
- ✅ Typed Python, modular design
- ✅ Submission includes GitHub, video, and LLM link

---

## ✅ Submission Checklist

- [x] GitHub Repo  
- [x] README.md with usage instructions  
- [x] `get-papers-list` command implemented  
- [x] report.md with explanation  
- [x] ChatGPT LLM conversation link  
- [x] Video walkthrough with test demo  

