import os
from dotenv import load_dotenv
from jira import JIRA

load_dotenv(override=True)

API_TOKEN = os.getenv("API_TOKEN", "ЗАПИХНИТЕ СЮДА КЛЮЧ")
JIRA_SERVER = os.getenv("JIRA_SERVER")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")

# JIRA_SERVER = os.environ.get("JIRA_SERVER") - другой вариант достать что-т из .env
# os.environ["key"] = "valeue" - Задать новое значение в envs 
jira = JIRA(
    server=JIRA_SERVER,
    basic_auth=(JIRA_USERNAME,API_TOKEN))

# print(jira.myself())
# print(jira.projects())
# print(jira.issue_types())

jira_issue = jira.create_issue(
    {
    "project": {"key": "SIGMA"},
    "summary":"Задача Теста Сигм",
    "description": "ОЧень крутая задача для очень крутых сигм",
    "issuetype": {"id":"10009"}
    })
jira.add_attachment(jira_issue.key,"komar.png")