import sqlprocessing
import config
import vkontakt
import telegram
import json
import workerAPI
import time



dataBase = sqlprocessing.sqlproc(config.db_host, config.db_user, config.db_password, config.db_name)
vk_bot = vkontakt.bot(config.vk_token)
tg_bot = telegram.bot(config.tg_token)
worker = workerAPI.worker()

while True:
    time.sleep(1)
    work = dataBase.fetch_all("events")
    for i in range(len(work)):
        work_source = work[i][2]
        print(work_source)
        if (work_source == 1):
            updates = json.dumps(work[i][1])
            #updates = work[i][1]
            print(len(updates))
            for j in range(len(updates)):
                update = updates[j]
                if update['type'][0] == 'message_new':
                    msgObject = update["object"]
                    if str(msgObject).find("action") != -1:
                        worker.actionExecuting(msgObject)
                    else:
                        if str(msgObject["text"]).find("/update", 0, 7) != -1:
                            worker.linkTelegramChat(msgObject)
                        else:
                            worker.msgExecuting(msgObject)
                else:
                    print(update)

        elif(work_source == 0):
            print(type(work[i][1]))
            print(work[i][1])
            updates = json.loads(work[i][1])
            #updates = simplejson.loads(updates)
            updates = updates["result"]
            print(len(updates))
            for j in range(len(updates)):
                update = updates[j]
                print(update)
                data = worker.tg_processing_event(update)
                dataBase.addMessage("messages", data[0], data[1], data[2], "", "", 0, data[8])
        else:
            print("source_error")

        dataBase.delete_row_by_id("events" ,work[i][0])

#    elif str(update)


#        {'ts': '88', 'updates': [{'type': 'message_new',
#                                  'object': {'date': 1548531008, 'from_id': 424013544, 'id': 0, 'out': 0,
#                                             'peer_id': 2000000001, 'text': '', 'conversation_message_id': 85,
#                                             'action': {'type': 'chat_invite_user', 'member_id': -177210709},
#                                             'fwd_messages': [], 'important': False, 'random_id': 0, 'attachments': [],
#                                             'is_hidden': False}, 'group_id': 177210709}]}
#        {'ts': '89', 'updates': [{'type': 'message_new',
#                                  'object': {'date': 1548531024, 'from_id': 424013544, 'id': 0, 'out': 0,
#                                             'peer_id': 2000000001, 'text': 'ыфа', 'conversation_message_id': 86,
#                                             'fwd_messages': [], 'important': False, 'random_id': 0, 'attachments': [],
#                                             'is_hidden': False}, 'group_id': 177210709}]}
#        {'ts': '89', 'updates': []}
#       {'ts': '117', 'updates': [{'type': 'message_new',
#                               'object': {'date': 1548576745, 'from_id': 424013544, 'id': 0, 'out': 0,
#                                          'peer_id': 2000000001, 'text': 'f', 'conversation_message_id': 115,
#                                          'fwd_messages': [], 'important': False, 'random_id': 0, 'attachments': [],
#                                          'is_hidden': False}, 'group_id': 177210709}, {'type': 'message_new',
#                                                                                        'object': {'date': 1548576757,
#                                                                                                   'from_id': 424013544,
#                                                                                                   'id': 0, 'out': 0,
#                                                                                                   'peer_id': 2000000001,
#                                                                                                   'text': 'f',
#                                                                                                   'conversation_message_id': 116,
#                                                                                                   'fwd_messages': [],
#                                                                                                   'important': False,
#                                                                                                   'random_id': 0,
#                                                                                                   'attachments': [],
#                                                                                                   'is_hidden': False},
#                                                                                        'group_id': 177210709}]}



#   TG DATA

#   [0] first_name
#   [1] last_name
#   [2] text
#   [3] data.append({"forward_msg":None})
#   [4] data.append({"photo":None})
#   [5] data.append({"file":None})
#   [6] data.append({"voice":None})
#   [7] data.append({"music":None})
#   [8] data.append({"chat_id":chat_id})