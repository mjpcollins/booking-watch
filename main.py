import json
import base64
import datetime
from utils import Checker, Alert
from config.conf import r_lookup


def main(event, context):
    print(event)
    print(context)
    data = json.loads(base64.b64decode(event['data']).decode('utf-8'))
    opentable_data = data['opentable']
    date = (datetime.datetime.now() + datetime.timedelta(days=opentable_data['daysLookAhead']))
    date_str = date.strftime("%Y-%m-%dT%H:%M")
    rid = opentable_data['rid']
    people = opentable_data['people']
    checker = Checker(rid=rid,
                      datetime_str=date_str,
                      people=people)
    availability = checker.check_availability()
    if availability:
        dates_available = ", ".join(availability)
        r_name = r_lookup.get(rid, "<unknown>")
        message = f'There are dates available at {r_name} ({rid}) for {people} people: {dates_available}'
        print(message)
        alert_data = data['alert']
        alert = Alert(auth_token=alert_data['auth_token'],
                      account_sid=alert_data['account_sid'],
                      phone_number=alert_data['phone_number'])
        sent_message = alert.send_alert(message=message,
                                        messaging_service_sid=alert_data['messaging_service_sid'])
        print(sent_message)
    else:
        print("No dates currently available.")


if __name__ == '__main__':
    data = {'opentable': {'rid': 138306,
                          'daysLookAhead': 90,
                          'people': 2},
            'alert': {'auth_token': '',
                      'account_sid': '',
                      'phone_number': '',
                      'messaging_service_sid': ''}}
    pubsub_data = base64.b64encode(json.dumps(data).encode('utf-8'))
    event = {'data': pubsub_data}
    main(event, {})
