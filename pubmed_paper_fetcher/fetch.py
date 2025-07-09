from typing import List, Dict
import requests
import xml.etree.ElementTree as ET
import pandas as pd

from .utils import is_non_academic, extract_email


def get_pubmed_ids(query: str, max_results: int = 10) -> List[str]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["esearchresult"]["idlist"]


def fetch_paper_details(pubmed_ids: List[str]) -> List[Dict]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml"
    }
    response = requests.get(url, params=params)
    root = ET.fromstring(response.text)

    papers = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        pub_date = article.findtext(".//PubDate/Year") or "Unknown"

        non_academic_authors = []
        company_affiliations = []
        corresponding_email = "N/A"

        for author in article.findall(".//Author"):
            affiliation = author.findtext(".//AffiliationInfo/Affiliation")
            name_parts = [
                author.findtext("ForeName") or "",
                author.findtext("LastName") or ""
            ]
            full_name = " ".join(name_parts).strip()

            if affiliation and is_non_academic(affiliation):
                non_academic_authors.append(full_name)
                company_affiliations.append(affiliation)

                email = extract_email(affiliation)
                if email and corresponding_email == "N/A":
                    corresponding_email = email

        if non_academic_authors:
            papers.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": pub_date,
                "Non-academic Author(s)": "; ".join(non_academic_authors),
                "Company Affiliation(s)": "; ".join(company_affiliations),
                "Corresponding Author Email": corresponding_email
            })

    return papers


def save_to_csv(papers: List[Dict], filename: str = "output.csv"):
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)
    print(f"✅ Saved {len(df)} papers to {filename}")
