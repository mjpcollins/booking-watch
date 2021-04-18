import requests
from config.conf import settings


class Checker:

    def __init__(self, rid, datetime_str, people=2):
        self.rid = rid
        self.datetime_str = datetime_str
        self.people = people
        self.availability = {}

    def check_availability(self):
        self._query_open_table()
        return self._get_dates_and_times()

    @staticmethod
    def _process_json_response(json_response):
        availability = json_response.get('availability', {})
        date_keys = [key for key in availability if "-" in key]
        return_dict = {}
        for date in date_keys:
            return_dict[date] = availability[date].get('timeSlots', [])
        return return_dict

    def _query_open_table(self):
        data = '{"rid":' + str(self.rid) + \
               ',"dateTime":"' + self.datetime_str + \
               '","partySize": ' + str(self.people) + '}'
        response = requests.post(url=settings['opentable_url'],
                                 headers=settings['headers'],
                                 data=data)
        self.availability = self._process_json_response(response.json())
        return self.availability

    def _get_dates_and_times(self):
        return [ts.get('dateTime') for d in self.availability for ts in self.availability[d]]
