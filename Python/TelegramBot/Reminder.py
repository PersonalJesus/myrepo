import asyncio
import json
import requests
from aiogram import Bot, Dispatcher, executor
import os

GITLAB_TOKEN = os.getenv('GITLAB_TOKEN')
GITLAB_URL_OPENED = os.getenv('GITLAB_URL_OPENED')
CHANNEL_ID = os.getenv('CHANNEL_ID')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
hash_request = 0


def check_hash(request):  # check old and new request hash
    global hash_request
    if hash(str(request)) == hash_request:
        return True
    else:
        hash_request = hash(str(request))
        return False


def get_info_opened():  # get all opened issues
    try:
        authorization = f'Bearer {GITLAB_TOKEN}'
        headers = {"Authorization": authorization}
        r = requests.get(GITLAB_URL_OPENED, headers=headers)
        data = r.json()
        return data
    except Exception as ex:
        print(ex)


def sorting_opened_response(opened_issues):  # sorting opened issues
    new_dict = {}
    for issue in opened_issues:
        iid = issue['iid']
        updated_at = issue['updated_at']
        author = issue['author']['name']
        description = issue['description']
        web_url = issue['web_url']
        try:
            assignee = issue['assignee']['name']
        except:
            assignee = "Nobody was assigned"
        title = issue['title']
        new_dict[str(iid)] = {
            "updated_at": updated_at,
            "author": author,
            "description": description,
            "assignee": assignee,
            "title": title,
            "web_url": web_url
        }
    return new_dict


def creating_file(new_dict):
    with open("new_dict.json", "w", encoding='utf-8') as file:
        json.dump(new_dict, file, indent=4, ensure_ascii=False)


def check_issues_update(fresh_dict): # check some updated with old and new issues
    updated_issues_iid = []
    with open("new_dict.json", encoding='utf-8') as file:
        opened_dict = json.load(file)

        similar_values = set(fresh_dict.keys()) & set(list(opened_dict.keys()))
        for sim_iid in similar_values:
            if hash(opened_dict[sim_iid]["updated_at"]) != hash(fresh_dict[sim_iid]["updated_at"]):
                updated_issues_iid.append(sim_iid)

    return updated_issues_iid


def check_new_and_closed_issues(fresh_dict): # check new and closed issues
    added_issues_iid = []
    closed_issues_iid = []
    with open("new_dict.json", encoding='utf-8') as file:
        opened_dict = json.load(file)

        diff_values = set(fresh_dict.keys()) ^ set(list(opened_dict.keys()))

        for diff_iid in diff_values:
            if not diff_iid in opened_dict.keys():
                added_issues_iid.append(diff_iid)
            else:
                closed_issues_iid.append(diff_iid)

    return added_issues_iid, closed_issues_iid


async def send_periodic(time_sleep):
    while True:
        await asyncio.sleep(time_sleep)
        fresh_data = sorting_opened_response(get_info_opened())

        if check_hash(fresh_data):
            continue
        else:
            with open("new_dict.json", encoding='utf-8', errors='ignore') as file:
                old_dict = json.load(file)

            added_iid, closed_iid = check_new_and_closed_issues(fresh_data)
            updated_iid = check_issues_update(fresh_data)
            for upd_id in updated_iid:
                issue = f"{'Issue: ' + fresh_data[upd_id]['title'] + ' was changed'}\n" \
                        f"{'Issue url: ' + old_dict[upd_id]['web_url']}"
                await bot.send_message(CHANNEL_ID, issue)

            for add_id in added_iid:
                issue = f"{'Author: ' + fresh_data[add_id]['author']}\n" \
                        f"{'Assigned to: ' + fresh_data[add_id]['assignee']}\n" \
                        f"{'Title: ' + fresh_data[add_id]['title']}\n" \
                        f"{'Issue url: ' + fresh_data[add_id]['web_url']}\n" \
                        f"{'Description: ' + fresh_data[add_id]['description']}"
                await bot.send_message(CHANNEL_ID, issue)

            for close_id in closed_iid:
                issue = f"{'Issue: ' + old_dict[close_id]['title'] + ' was closed'}\n" \
                        f"{'Issue url: ' + old_dict[close_id]['web_url']}"
                await bot.send_message(CHANNEL_ID, issue)

            creating_file(fresh_data)


def main():
    loop = asyncio.get_event_loop()
    loop.create_task(send_periodic(100))

    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
