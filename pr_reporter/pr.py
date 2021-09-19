import pandas as pd
import json
import requests
from pathlib import Path
from pr_reporter.models.pr_models import PrInfo
from jinja2 import Template
from tabulate import tabulate
import yagmail
import logging
import os
logger = logging.getLogger(__name__)
class PR(object):
    API_ENDPOINT = "https://api.github.com/repos/{owner}/{repo}/pulls"
    email_template = Path(__file__).parent/"templates"/"email_template.jinja"
    def __init__(self, pr_info: PrInfo):
        self.repo = pr_info.repo
        self.owner = pr_info.owner
        self.receiver_email = pr_info.email
        self.endpoint = PR.API_ENDPOINT.format(repo=self.repo, owner=self.owner)
        self.pr_data = None
        self.sender_email = os.getenv('sender_email')

    
    def _pull_data(self):
        headers = {
            'Accept': 'application/vnd.github.v3+json',
        }
        self.pr_data = []
        page = 1
        while True:
            logger.info(f"Fetching page {page} ...")
            params = (('state', 'all'),('page', page), ('per_page', 100))
            response = requests.get(self.endpoint, headers=headers, params=params)
            if response.status_code == 200:
                content = response.json()
                if len(content) == 0  or not self.parse(content):
                    break
                page += 1

    def send_email(self, content): 
        receiver = self.receiver_email
        if self.sender_email is None:
            logger.info("Email not configured printing to screen")
            self.print_email(content)
            return
        yag = yagmail.SMTP(self.sender_email)
        yag.send(to=receiver, subject="Weekly PR digest.", contents=content)

    def print_email(self, content):
        logger.info(f"To:{self.receiver_email}")
        logger.info(f"From:{self.sender_email}")
        logger.info(f"Subject: Weekly PR digest.")
        logger.info(f"Body:{content}")
  
    def parse(self, content):
        dates_required = ['created_at','updated_at','closed_at','merged_at']
        now = pd.to_datetime('now', utc=True)
        week_delta = pd.to_timedelta('7 days')
        for pr in content:
            is_latest = [now - pd.to_datetime(pr[date_field]) < week_delta for date_field in dates_required if pr[date_field] is not None]
            if any(is_latest):
                self.pr_data.append(pr)
            else:
                return False
        return True


    def run(self):
        self._pull_data()
        if self.pr_data:
            df = pd.DataFrame(self.pr_data)
            df['user_name'] = df['user'].apply(lambda x: x['login'])
            open_close = df.groupby(by='state')['state'].count().to_dict()
            summary_cols = ['url', 'state', 'title', 'body', 'created_at', 
                            'updated_at','closed_at','merged_at','user_name']
            summary_records = df[summary_cols].to_dict('records')
            with open(self.email_template) as file_:
                template = Template(file_.read())
            content = template.render(**{**open_close,**dict(summary_records=summary_records)})
        if self.receiver_email is None:
            self.print_email(content)
        else:
            self.send_email(content)