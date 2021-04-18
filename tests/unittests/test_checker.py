from unittest import TestCase
from utils import Checker


class TestChecker(TestCase):

    def setUp(self):
        self.init_data()
        self.c = Checker(rid=184047,
                         datetime_str="2021-04-18T19:00")

    def test_init(self):
        self.assertEqual(184047, self.c.rid)
        self.assertEqual("2021-04-18T19:00", self.c.datetime_str)
        self.assertEqual(2, self.c.people)

    def test_process_json_response(self):
        actual_dict = self.c._process_json_response(self.response_json)
        self.assertEqual(self.expected_availability, actual_dict)

    def test_get_dates_and_times(self):
        self.c.availability = self.expected_availability
        expected_dates_and_times = ['2021-04-19T17:19', '2021-04-19T17:34', '2021-04-21T17:19']
        actual_dates_and_times = self.c._get_dates_and_times()
        self.assertEqual(expected_dates_and_times, actual_dates_and_times)

    def init_data(self):
        self.expected_availability = {'2021-04-18': [],
                         '2021-04-19': [{'bookableExperienceIds': [],
                                         'bookableExperiencesBySeating': {},
                                         'creditCardRequired': False,
                                         'dateTime': '2021-04-19T17:19',
                                         'hasExperiences': False,
                                         'hasOffers': False,
                                         'isMandatory': False,
                                         'isMandatoryBySeating': None,
                                         'nonBookableExperienceIds': [],
                                         'nonBookableExperiencesBySeating': {},
                                         'offerIds': [],
                                         'offset': 0,
                                         'slotAvailabilityToken': 'eyJ2IjoyLCJtIjowLCJwIjowLCJjIjo2LCJzIjowLCJuIjowfQ',
                                         'slotHash': 2671573815,
                                         'tableAttributes': ['outdoor'],
                                         'time': '5:19 pm',
                                         'type': 'standard'},
                                        {'bookableExperienceIds': [],
                                         'bookableExperiencesBySeating': {},
                                         'creditCardRequired': False,
                                         'dateTime': '2021-04-19T17:34',
                                         'hasExperiences': False,
                                         'hasOffers': False,
                                         'isMandatory': False,
                                         'isMandatoryBySeating': None,
                                         'nonBookableExperienceIds': [],
                                         'nonBookableExperiencesBySeating': {},
                                         'offerIds': [],
                                         'offset': 15,
                                         'slotAvailabilityToken': 'eyJ2IjoyLCJtIjowLCJwIjowLCJjIjo2LCJzIjowLCJuIjowfQ',
                                         'slotHash': 3345416433,
                                         'tableAttributes': ['outdoor'],
                                         'time': '5:34 pm',
                                         'type': 'standard'}
                                        ],
                         '2021-04-20': [],
                         '2021-04-21': [{'bookableExperienceIds': [],
                                         'bookableExperiencesBySeating': {},
                                         'creditCardRequired': False,
                                         'dateTime': '2021-04-21T17:19',
                                         'hasExperiences': False,
                                         'hasOffers': False,
                                         'isMandatory': False,
                                         'isMandatoryBySeating': None,
                                         'nonBookableExperienceIds': [],
                                         'nonBookableExperiencesBySeating': {},
                                         'offerIds': [],
                                         'offset': 0,
                                         'slotAvailabilityToken': 'eyJ2IjoyLCJtIjowLCJwIjowLCJjIjo2LCJzIjowLCJuIjowfQ',
                                         'slotHash': 738736766,
                                         'tableAttributes': ['outdoor'],
                                         'time': '5:19 pm',
                                         'type': 'standard'},
                                        ]}

        self.response_json = {'availability': {'2021-04-18': {'allNoTimesReasons': ['NoTimesExist'],
                                 'allowNextAvailable': True,
                                 'date': '2021-04-18',
                                 'earlyCutoff': None,
                                 'hasExperiences': False,
                                 'hasOffers': False,
                                 'maxDaysInAdvance': 181,
                                 'maxPartySize': 6,
                                 'minPartySize': 1,
                                 'offerIds': [],
                                 'reasonCode': 'NoTimesExist',
                                 'sameDayCutoff': None,
                                 'standardMessageCode': 'noTimes',
                                 'timeSlots': []},
                  '2021-04-19': {'allNoTimesReasons': [],
                                 'allowNextAvailable': True,
                                 'date': '2021-04-19',
                                 'earlyCutoff': None,
                                 'hasExperiences': False,
                                 'hasOffers': False,
                                 'maxDaysInAdvance': 181,
                                 'maxPartySize': 6,
                                 'minPartySize': 1,
                                 'offerIds': [],
                                 'sameDayCutoff': None,
                                 'timeSlots': [{'bookableExperienceIds': [],
                                                'bookableExperiencesBySeating': {},
                                                'creditCardRequired': False,
                                                'dateTime': '2021-04-19T17:19',
                                                'hasExperiences': False,
                                                'hasOffers': False,
                                                'isMandatory': False,
                                                'isMandatoryBySeating': None,
                                                'nonBookableExperienceIds': [],
                                                'nonBookableExperiencesBySeating': {},
                                                'offerIds': [],
                                                'offset': 0,
                                                'slotAvailabilityToken': 'eyJ2IjoyLCJtIjowLCJwIjowLCJjIjo2LCJzIjowLCJuIjowfQ',
                                                'slotHash': 2671573815,
                                                'tableAttributes': ['outdoor'],
                                                'time': '5:19 pm',
                                                'type': 'standard'},
                                               {'bookableExperienceIds': [],
                                                'bookableExperiencesBySeating': {},
                                                'creditCardRequired': False,
                                                'dateTime': '2021-04-19T17:34',
                                                'hasExperiences': False,
                                                'hasOffers': False,
                                                'isMandatory': False,
                                                'isMandatoryBySeating': None,
                                                'nonBookableExperienceIds': [],
                                                'nonBookableExperiencesBySeating': {},
                                                'offerIds': [],
                                                'offset': 15,
                                                'slotAvailabilityToken': 'eyJ2IjoyLCJtIjowLCJwIjowLCJjIjo2LCJzIjowLCJuIjowfQ',
                                                'slotHash': 3345416433,
                                                'tableAttributes': ['outdoor'],
                                                'time': '5:34 pm',
                                                'type': 'standard'}]},
                  '2021-04-20': {'allNoTimesReasons': ['NoTimesExist'],
                                 'allowNextAvailable': True,
                                 'date': '2021-04-20',
                                 'earlyCutoff': None,
                                 'hasExperiences': False,
                                 'hasOffers': False,
                                 'maxDaysInAdvance': 181,
                                 'maxPartySize': 6,
                                 'minPartySize': 1,
                                 'offerIds': [],
                                 'reasonCode': 'NoTimesExist',
                                 'sameDayCutoff': None,
                                 'standardMessageCode': 'noTimes',
                                 'timeSlots': []},
                  '2021-04-21': {'allNoTimesReasons': [],
                                 'allowNextAvailable': True,
                                 'date': '2021-04-21',
                                 'earlyCutoff': None,
                                 'hasExperiences': False,
                                 'hasOffers': False,
                                 'maxDaysInAdvance': 181,
                                 'maxPartySize': 6,
                                 'minPartySize': 1,
                                 'offerIds': [],
                                 'sameDayCutoff': None,
                                 'timeSlots': [{'bookableExperienceIds': [],
                                                'bookableExperiencesBySeating': {},
                                                'creditCardRequired': False,
                                                'dateTime': '2021-04-21T17:19',
                                                'hasExperiences': False,
                                                'hasOffers': False,
                                                'isMandatory': False,
                                                'isMandatoryBySeating': None,
                                                'nonBookableExperienceIds': [],
                                                'nonBookableExperiencesBySeating': {},
                                                'offerIds': [],
                                                'offset': 0,
                                                'slotAvailabilityToken': 'eyJ2IjoyLCJtIjowLCJwIjowLCJjIjo2LCJzIjowLCJuIjowfQ',
                                                'slotHash': 738736766,
                                                'tableAttributes': ['outdoor'],
                                                'time': '5:19 pm',
                                                'type': 'standard'}]},
                  'ticketedExperiences': {},
                  'waitlistStatus': {'waitlistAvailable': False}},
                  'blockedDayMessages': []}