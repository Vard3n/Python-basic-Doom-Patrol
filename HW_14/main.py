import argparse
import json


def create_file():
    file = open("userinfo.json", 'w')
    file.write(json.dumps([]))
    file.close()
    return open("userinfo.json", 'r')


def add_user(users):
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="username", required=True)
    parser.add_argument("-e", "--email", help="email", required=True)
    parser.add_argument("-s", "--status", help="status", required=True)
    args = parser.parse_args()

    try:
        users['username'] = args.username
        users['email'] = args.email
        users['status'] = args.status
    except IndexError:
        raise Exception('Wrong information added')


def user_check(user_data, user):
    for users in user_data:
        if user['username'] == users['username'] or user['email'] == users['email']:
            return True

    return False


def user_add(user):
    try:
        read_file = open('userinfo.json', 'r')
    except FileNotFoundError:
        read_file = create_file()
    finally:
        pass

    try:
        user_data = json.loads(read_file.read())
    except ValueError:
        with open('userinfo.json', 'w') as file:
            file.write(json.dumps([]))
        user_data = []
    finally:
        pass

    read_file.close()

    if not user_check(user_data, user):
        user_data.append(user)
        with open('userinfo.json', 'w', -1) as file:
            file.write(json.dumps(user_data, indent=3, sort_keys=True))
    else:
        raise ("User with this username or email already exist!")


if __name__ == "__main__":
    new_user = {}
    add_user(new_user)
    user_add(new_user)