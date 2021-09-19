# latest-pr-reporter

Using Github api to retrieve summary of all opened, closed and in progress PR in the last week

## Create a virtual environment using miniconda 

Download miniconda from [Miniconda](https://docs.conda.io/en/latest/miniconda.html) for your OS.

```shell
conda create -n git_pr python=3.8
```

### Activating the virtual environment

```shell
conda activate git_pr
```

## Installing dependencies

```shell
pip install -r requirements.txt
```

## Using email functionality

Before running the run.py run the below script to configure the sender email.

```python
import yagmail
yagmail.register('mygmailusername', 'mygmailpassword')
```

Set the email in the environment variable before running the run.py

```shell
export sender_email=mygmailusername
```

## Running the script

```shell
usage: 

python run.py [-h] [--email str] [--repo str] [--owner str]

optional arguments:
-h, --help   show this help message and exit
--email str  Receiver email
--repo str   git repo
--owner str  owner of the git repo
```

## Sample output
```
Hi,

Please find below the last week pull request summary of the repo :

Total number of PR's created/updated/closed last week 57

1. 20 PR's were updated/created.
2. 37 PR's were closed.

Detailed summary is given below:



1. DOC - Ensure TheilSenRegressor passes numpydoc validation (open)

Raised by: EricEllwanger

Body:

#### Reference Issues/PRs
References #20308

#### What does this implement/fix? Explain your changes.
Changes to sklearn/linear_model/_theil_sen.py:
Reordered Docstring section for TheilSenRegressor
Add 'See Also' section for TheilSenRegressor
Added period to parameter 'random_state' description in TheilSenRegressor
Added description to 'Returns' section of TheilsonRegressor.fit

Removed TheilSenRegressor from DOCSTRING_IGNORE_LIST


#### Any other comments?



Created at : 2021-09-19T12:14:19Z
Updated at : 2021-09-19T12:14:44Z
Merged at : None
Closed at : None

url: https://api.github.com/repos/scikit-learn/scikit-learn/pulls/21087


2. Sparse data input option for Quantile Regressor (open)

Raised by: venkyyuvy

Body:


#### Reference Issues/PRs:
partially addresses #20132.



#### What does this implement/fix? Explain your changes.


#### Any other comments?





Created at : 2021-09-19T11:14:58Z
Updated at : 2021-09-19T14:12:02Z
Merged at : None
Closed at : None

url: https://api.github.com/repos/scikit-learn/scikit-learn/pulls/21086

....

56. DOC add contributors to whats_new 1.0 and more fixes (closed)

Raised by: adrinjalali

Body:
This adds the list of contributors to the end of the file.

@glemaitre

Created at : 2021-09-10T10:41:35Z
Updated at : 2021-09-14T08:58:58Z
Merged at : 2021-09-13T09:52:28Z
Closed at : 2021-09-13T09:52:28Z

url: https://api.github.com/repos/scikit-learn/scikit-learn/pulls/21009


57. PRs to include in 1.0.rc2 (closed)

Raised by: adrinjalali

Body:
This is the list of PRs to be included in the 1.0.RC2, another PR will change the version on the branch. **This should not be squashed**.

cc @glemaitre @ogrisel

Created at : 2021-09-10T10:33:19Z
Updated at : 2021-09-14T11:28:32Z
Merged at : 2021-09-14T11:28:03Z
Closed at : 2021-09-14T11:28:03Z

url: https://api.github.com/repos/scikit-learn/scikit-learn/pulls/21008


Thanks.
```
