import pprint
import os

import marketplace


marketplace.client.URLS['settings.mine'] = '/account/settings/mine/'


def settings():
    for setting in ['CONSUMER_KEY', 'CONSUMER_SECRET']:
        if not os.environ.get(setting):
            raise ValueError('%s is not set in the environment' % setting)

    client = marketplace.Client(domain='marketplace.firefox.com',
                                protocol='https',
                                consumer_key=os.environ['CONSUMER_KEY'],
                                consumer_secret=os.environ['CONSUMER_SECRET'])
    result = client.conn.fetch('GET', client.url('settings.mine'))
    print result.status_code
    pprint.print(result.json())


if __name__ == '__main__':
    settings()
