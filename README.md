# latest-pr-reporter

Using Github api to retrieve summary of all opened, closed and in progress PR in the last week

## Using email functionality

Before running the run.py run the below script with the gmail to use for sending the email.

```python
import yagmail
yagmail.register('mygmailusername', 'mygmailpassword')
```

Set the email in the environment variable

```shell
export sender_email=mygmailusername
```

## Running the script

```shell
usage: run.py [-h] [--email str] [--repo str] [--owner str]

optional arguments:
-h, --help   show this help message and exit
--email str  Receiver email
--repo str   git repo
--owner str  owner of the git repo
```
