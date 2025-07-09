from typing import TypedDict, List

class Paper(TypedDict):
    PubmedID: str
    Title: str
    Publication_Date: str
    Non_academic_Authors: str
    Company_Affiliations: str
    Corresponding_Email: str