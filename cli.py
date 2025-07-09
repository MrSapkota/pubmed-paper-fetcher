import click
from pubmed_paper_fetcher.fetch import get_pubmed_ids, fetch_paper_details, save_to_csv


@click.command()
@click.argument("query")
@click.option("-f", "--file", type=str, help="Filename to save CSV")
@click.option("-d", "--debug", is_flag=True, help="Enable debug output")
@click.option("-m", "--max", "max_results", type=int, default=10, help="Max number of results to fetch")
def main(query: str, file: str, debug: bool, max_results: int):
    if debug:
        print(f"Query: {query}")
        print("Fetching PubMed IDs...")

    ids = get_pubmed_ids(query, max_results)
    
    if debug:
        print(f"Found {len(ids)} IDs: {ids}")
        print("Fetching details...")

    papers = fetch_paper_details(ids)

    if debug:
        print(f"Filtered papers: {papers}")

    if file:
        save_to_csv(papers, file)
    else:
        print(papers)
