import os

import pandas as pd

from models.bill import Bill
from models.person import Person
from models.vote import Vote
from models.voteresult import VoteResult

INPUT_FOLDER = 'inputs'

def read_legislators(csv_filename:str = "legislators.csv") -> list[Person]:
    legislators_df = pd.read_csv(os.path.join(INPUT_FOLDER,csv_filename))
    legislators: list[Person] = []
    for col in legislators_df.columns:
        legislators_df.rename(columns={col:col.lower().replace(" ", "_")}, inplace=True)

    for _,person in legislators_df.iterrows():
        legislators.append(Person(**person))

    return legislators

def read_bills(csv_filename:str = "bills.csv") ->  list[Bill]:
    bills_df = pd.read_csv(os.path.join(INPUT_FOLDER,csv_filename))
    bills: list[Bill] = []
    for col in bills_df.columns:
        bills_df.rename(columns={col:col.lower().replace(" ", "_")}, inplace=True)

    for _,bill in bills_df.iterrows():
        bills.append(Bill(**bill))

    return bills

def read_vote_results(csv_filename:str = "vote_results.csv") -> list[VoteResult]:
    vote_results_df = pd.read_csv(os.path.join(INPUT_FOLDER,csv_filename))
    vote_results: list[VoteResult] = []
    for col in vote_results_df.columns:
        vote_results_df.rename(columns={col:col.lower().replace(" ", "_")}, inplace=True)

    for _,vote_result in vote_results_df.iterrows():
        vote_results.append(VoteResult(**vote_result))

    return vote_results

def read_votes(csv_filename:str = "votes.csv") -> list[Vote]:
    votes_df = pd.read_csv(os.path.join(INPUT_FOLDER,csv_filename))
    votes: list[Vote] = []
    for col in votes_df.columns:
        votes_df.rename(columns={col:col.lower().replace(" ", "_")}, inplace=True)

    for _,vote in votes_df.iterrows():
        votes.append(Vote(**vote))

    return votes