"""
Copyright (2018) Chris Scuderi

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import time

from alarm_central_station_receiver.contact_id import dsc


def create_event(rtype, description, eid):
    return {
        'timestamp': time.time(),
        'type': rtype,
        'description': description,
        'id': eid,
    }


def decode(raw_events):
    decoded_events = []

    for err, code in raw_events:
        if not err:
            report_type, description = dsc.digits_to_alarmreport(code)
        else:
            report_type = 'U'
            if len(code) != 16:
                description = \
                    'Leftover Bits: %s (len %d)' % (code, len(code))
            else:
                description = \
                    'Checksum Mismatch: %s' % code

        decoded_events.append(create_event(report_type,
                                           description,
                                           code))
    return decoded_events
