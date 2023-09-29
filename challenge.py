import os

import pandas as pd

from models.bill import Bill
from models.person import Person
from models.vote import Vote
from models.voteresult import VoteResult
from utils.utils import (read_bills, read_legislators, read_vote_results,
                         read_votes)

OUTPUT_FOLDER = 'outputs'


def legislators_count(legislators: list[Person],vote_results: list[VoteResult]) -> None:
    df = pd.DataFrame(vote_results)
    legislator_res = []
    for legislator in legislators:
        legislator_res.append(
            {
            'id': legislator.id, 'name': legislator.name,
            'num_supported_bills': df.loc[(df['legislator_id'] == legislator.id) & (df['vote_type'] == 1),'vote_type'].count(),
            'num_opposed_bills': df.loc[(df['legislator_id'] == legislator.id) & (df['vote_type'] == 2),'vote_type'].count()
            }
        )
        

    result_df = pd.DataFrame(legislator_res)
    result_df.to_csv(os.path.join(OUTPUT_FOLDER, 'legislators-support-oppose-count.csv'),index=False)

def bill_report(bills: list[Bill],votes: list[Vote],vote_results: list[VoteResult], legislators: list[Person]) -> None:
    votes_df = pd.DataFrame(votes)
    vote_results_df = pd.DataFrame(vote_results)
    legislators_df = pd.DataFrame(legislators)
    bill_report_res = []
    for bill in bills:
        sponsor_filter_names = legislators_df.loc[legislators_df['id'] == bill.sponsor_id, 'name'].values
        primary_sponsor_name = sponsor_filter_names[0] if len(sponsor_filter_names) > 0 else "Unknown"

        bill_vote_ids = votes_df.loc[votes_df['bill_id'] == bill.id,'id'].values
        support_counter = 0
        opposer_counter = 0
        for vote_id in bill_vote_ids:
            support_counter += vote_results_df.loc[(vote_results_df['vote_id'] == vote_id) & (vote_results_df['vote_type'] == 1),'vote_type'].count()
            opposer_counter += vote_results_df.loc[(vote_results_df['vote_id'] == vote_id) & (vote_results_df['vote_type'] == 2),'vote_type'].count()

        bill_report_res.append({
            'id': bill.id,
            'title': bill.title,
            'supporter_count': support_counter,
            'opposer_counter': opposer_counter,
            'primary_sponsor': primary_sponsor_name,
        })

    result_df = pd.DataFrame(bill_report_res)
    result_df.to_csv(os.path.join(OUTPUT_FOLDER, 'bills.csv'),index=False)

if __name__ == "__main__":
    legislators = read_legislators()
    bills = read_bills()
    vote_results = read_vote_results()
    votes = read_votes()

    legislators_count(legislators,vote_results)
    bill_report(bills, votes, vote_results, legislators)