import requests
from config import gitlab_token

gitlab_url = 'https://gitlab.akb-it.ru/api/v4/projects/10295/issues?state=opened'


def get_info():
    try:
        authorization = f'Bearer {gitlab_token}'
        headers = {"Authorization": authorization}
        r = requests.get(gitlab_url, headers=headers)
        data = r.json()
        return(data)
    except Exception as ex:
        print(ex)


def sorting_response(get_info):
    for issue in get_info:
        iid = issue['iid']
        update_data = issue['updated_at']
        author = issue['author']['name']
        description = issue['description']
        assignee = issue['assignee']['name']
        title = issue['title']


def main():
    get_info()


print(get_info())


if __name__ == '__main__':
    main()