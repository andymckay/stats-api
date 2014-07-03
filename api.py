import pprint
import os
import urllib

import marketplace


marketplace.client.URLS['settings.mine'] = '/account/settings/mine/'
marketplace.client.URLS['stats.apps_added_by_package'] = '/stats/global/apps_added_by_package/?%s'


class Client(object):

    def __init__(self):
        for setting in ['CONSUMER_KEY', 'CONSUMER_SECRET']:
            if not os.environ.get(setting):
                raise ValueError('%s is not set in the environment' % setting)

        self.client = marketplace.Client(domain='marketplace.firefox.com',
            protocol='https',
            consumer_key=os.environ['CONSUMER_KEY'],
            consumer_secret=os.environ['CONSUMER_SECRET'])


    def get(self, url, data=None):
        target = self.client.url(url)
        if data:
            data = urllib.urlencode(data)
            target = target % data
        return self.client.conn.fetch('GET', target)


def dump(result):
    pprint.pprint(result.json())


if __name__ == '__main__':
    c = Client()
    dump(c.get('settings.mine'))
    dump(c.get('stats.apps_added_by_package', {
        'start': '2014-01-01',
        'end': '2014-01-03',
        'interval': 'day'}))
