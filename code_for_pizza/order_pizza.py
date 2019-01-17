from github import Github
from datetime import datetime, timedelta
from dominos_test_order import order_pizza
from configparser import ConfigParser

# if you want to read the credentials from a config.ini file rather than hardcoding it.
# config = ConfigParser()
# config.read('/home/sriram/pizzapi/code_for_pizza/creds.ini')
# user_id = config['github']['user_id']
# password = config['github']['password']
# g = Github(user_id, password)

# get the github user
g = Github("username","password")
user = g.get_user()

# set the repository to what you want it to be.
repo = g.get_user().get_repo("Your-Repo")
print("last modified at",repo.last_modified)
last_updated_date = repo.updated_at
current_time = datetime.now()
diff_days = (current_time-last_updated_date).days
print("Number of days without a code checkin",diff_days)
if diff_days > 0:
    print("Sorry NO CODE NO PIZZA !!")
else:
    print("Enjoy thy offering")
    order_pizza()


