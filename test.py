import sqlprocessing
import config
import vkontakt
import telegram
import json
from io import StringIO


data = "Alexey Chukhryaev\n\nSome text written here\n\t>>> Some guy\n\n\t>>> Some useless text"
#data = str(data)
#print(json.load(StringIO(data)))

print(data)



#   {'error': {'error_code': 113, 'error_msg': 'Invalid user id', 'request_params': [{'key': 'oauth', 'value': '1'}, {'key': 'method', 'value': 'users.get'}, {'key': 'user_ids', 'value': '42401354400'}, {'key': 'v', 'value': '5.92'}]}}
#   {'response': [{'id': 424013544, 'first_name': 'Ren', 'last_name': 'Koike', 'is_closed': False, 'can_access_closed': True}]}



#[{'update_id': 11150166, 'message': {'message_id': 59, 'from': {'id': 205396228, 'is_bot': False, 'first_name': '.', 'username': 'getter_setter', 'language_code': 'en'}, 'chat': {'id': -349716291, 'title': 'Группа 9', 'type': 'group', 'all_members_are_administrators': False}, 'date': 1548747692, 'text': 'Hhhhjd'}}]

#[{'update_id': 11150167, 'message': {'message_id': 60, 'from': {'id': 205396228, 'is_bot': False, 'first_name': '.', 'username': 'getter_setter', 'language_code': 'en'}, 'chat': {'id': -349716291, 'title': 'Группа 9', 'type': 'group', 'all_members_are_administrators': False}, 'date': 1548747996, 'text': 'Bhhhhz'}}]

#[{'update_id': 11150168, 'message': {'message_id': 61, 'from': {'id': 205396228, 'is_bot': False, 'first_name': '.', 'username': 'getter_setter', 'language_code': 'en'}, 'chat': {'id': -349716291, 'title': 'Группа 9', 'type': 'group', 'all_members_are_administrators': False}, 'date': 1548748002, 'photo': [{'file_id': 'AgADAgADWaoxG3g9gEqUERKv8eJHobL59A4ABHZV7s6mVVDdVlQEAAEC', 'file_size': 1285, 'width': 90, 'height': 45}, {'file_id': 'AgADAgADWaoxG3g9gEqUERKv8eJHobL59A4ABCjoe2Hq5DeQV1QEAAEC', 'file_size': 13461, 'width': 320, 'height': 160}, {'file_id': 'AgADAgADWaoxG3g9gEqUERKv8eJHobL59A4ABATXYjx-bO4WWFQEAAEC', 'file_size': 51725, 'width': 800, 'height': 400}, {'file_id': 'AgADAgADWaoxG3g9gEqUERKv8eJHobL59A4ABKfSUIvXAdbaVVQEAAEC', 'file_size': 81369, 'width': 1280, 'height': 640}]}}]

#[{'update_id': 11150169, 'message': {'message_id': 62, 'from': {'id': 205396228, 'is_bot': False, 'first_name': '.', 'username': 'getter_setter', 'language_code': 'en'}, 'chat': {'id': -349716291, 'title': 'Группа 9', 'type': 'group', 'all_members_are_administrators': False}, 'date': 1548748005, 'voice': {'duration': 2, 'mime_type': 'audio/ogg', 'file_id': 'AwADAgADkAIAAng9gEpHYTdHxWOOpwI', 'file_size': 4968}}}]

#[{'update_id': 11150170, 'message': {'message_id': 63, 'from': {'id': 205396228, 'is_bot': False, 'first_name': '.', 'username': 'getter_setter', 'language_code': 'en'}, 'chat': {'id': -349716291, 'title': 'Группа 9', 'type': 'group', 'all_members_are_administrators': False}, 'date': 1548748010, 'reply_to_message': {'message_id': 60, 'from': {'id': 205396228, 'is_bot': False, 'first_name': '.', 'username': 'getter_setter', 'language_code': 'en'}, 'chat': {'id': -349716291, 'title': 'Группа 9', 'type': 'group', 'all_members_are_administrators': False}, 'date': 1548747996, 'text': 'Bhhhhz'}, 'text': 'Hh'}}]

#[{'update_id': 11150171, 'message': {'message_id': 64, 'from': {'id': 205396228, 'is_bot': False, 'first_name': '.', 'username': 'getter_setter', 'language_code': 'en'}, 'chat': {'id': -349716291, 'title': 'Группа 9', 'type': 'group', 'all_members_are_administrators': False}, 'date': 1548748018, 'text': 'Sjjsnej'}}]

#[{'update_id': 11150172, 'message': {'message_id': 65, 'from': {'id': 205396228, 'is_bot': False, 'first_name': '.', 'username': 'getter_setter', 'language_code': 'en'}, 'chat': {'id': -349716291, 'title': 'Группа 9', 'type': 'group', 'all_members_are_administrators': False}, 'date': 1548748019, 'forward_from': {'id': 205396228, 'is_bot': False, 'first_name': '.', 'username': 'getter_setter', 'language_code': 'en'}, 'forward_date': 1548747624, 'text': 'Uehe'}}]




