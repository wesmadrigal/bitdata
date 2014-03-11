#!/usr/bin/env python
import urllib2
import json
import sys


class BitData(object):
    
    def __init__(self, access_token):
        self._token = access_token
        self._requests = 0
        self._request_session = 0

    def high_value(self, limit=2):
        api = 'https://api-ssl.bitly.com/v3/highvalue?access_token={0}&limit={1}'
        try:
            req = urllib2.Request(api.format(self._token, limit))
            resp = urllib2.urlopen(req)
            if resp.code not in range(200,300):
                raise BitDataException("High Value Error")
            
        except urllib2.URLError:
            sys.exit(1)

        return json.loads(resp.read())


    def search(self, term):
        api = 'https://api-ssl.bitly.com/v3/search?access_token={0}&phrase={1}'
        try:
            req = urllib2.Request(api.format(self._token, term))
            resp = urllib2.urlopen(req)
            if resp.code not in range(200,300):
                raise BitDataException("Search Error")
    
        except urllib2.URLError:
            print "urllib2 error"
            sys.exit(1)

        return json.loads(resp.read())


    def bursting_phrases(self):
        api = 'https://api-ssl.bitly.com/v3/realtime/bursting_phrases?access_token={0}'
        try:
            req = urllib2.Request(api.format(self._token))
            resp = urllib2.urlopen(req)
            if resp.code not in range(200,300):
                raise BitDataException("Bursting Phrases Error")
  
        except urllib2.URLError:
            print "urllib2 error"
            sys.exit(1)

        return json.loads(resp.read())


    def hot_phrases(self):
        api = 'https://api-ssl.bitly.com/v3/realtime/hot_phrases?access_token={0}'
        try:
            req = urllib2.Request(api.format(self._token))
            resp = urllib2.urlopen(req)
            if resp.code not in range(200,300):
                raise BitDataException("Hot Phrases Error")
     
        except urllib2.URLError:
            print "urllib2 error"
            sys.exit(1)
     
        return json.loads(resp.read())


    def clickrate(self, phrase):
        api = 'https://api-ssl.bitly.com/v3/realtime/clickrate?access_token={0}&phrase={1}'
        try:
            req = urllib2.Request(api.format(self._token))
            resp = urllib2.urlopen(req)
            if resp.code not in range(200,300):
                raise BitDataException("Clickrate Error")

        except urllib2.URLError:
            print "urllib2 error"
            sys.exit(1)

        return json.loads(resp.read())


    def link_info(self, link):
        api = 'https://api-ssl.bitly.com/v3/link/info?access_token={0}&link={1}'
        try:
            req = urllib2.Request(api.format(self._token, link))
            resp = urllib2.urlopen(req)
            if resp.code not in range(200,300):
                raise BitDataException("Link Info Error")

        except urllib2.URLError:
            print "urllib2 error"
            sys.exit(1)

        return json.loads(resp.read())


    def link_content(self, link):
        api = 'https://api-ssl.bitly.com/v3/link/content?access_token={0}&link={1}'
        try:
            req = urllib2.Request(api.format(self._token, link))
            resp = urllib2.urlopen(req)
            if resp.code not in range(200,300):
                raise BitDataException("Link Content Error")
    
        except urllib2.URLError:
            print "urllib2 error"
            sys.exit(1)

        return json.loads(resp.read())


    def link_category(self, link):
        api = 'https://api-ssl.bitly.com/v3/link/category?access_token={0}&link={1}'
        try:
            req = urllib2.Request(api.format(self._token, link))
            resp = urllib2.urlopen(req)
            if resp.code not in range(200,300):
                raise BitDataException("Link Category Error")
    
        except urllib2.URLError:
            print "urllib2 error"
            sys.exit(1)

        return json.loads(resp.read())        


    def link_location(self, link):
        api = 'https://api-ssl.bitly.com/v3/link/location?access_token={0}&link={1}'
        try:
            req = urllib2.Request(api.format(self._token, link))
            resp = urllib2.urlopen(req)
            if resp.code not in range(200,300):
                raise BitDataException("Link Location Error")
    
        except urllib2.URLError:
            print "urllib2 error"
            sys.exit(1)

        return json.loads(resp.read())


    def link_language(self, link):
        api = 'https://api-ssl.bitly.com/v3/link/language?access_token={0}&link={1}'
        try:
            req = urllib2.Request(api.format(self._token, link))
            resp = urllib2.urlopen(req)
            if resp.code not in range(200,300):
                raise BitDataException("Link Language Error")
    
        except urllib2.URLError:
            print "urllib2 error"
            sys.exit(1)

        return json.loads(resp.read())


    """
    Retrieves the top phrase, uri, visitor count, and content
    from the bursting_content API endpoint and builds
    a hashtable with the aforementioned data
    """
    def top_bursting_content(self):
        bursting = self.bursting_phrases()
        data = {}

        try:
            top_link = bursting['data']['phrases'][0]['urls'][0]
            visitors = top_link['visitors']
            uri = top_link['aggregate_url']
            phrase = bursting['data']['phrases'][0]['phrase'] 
        except KeyError:
            raise BitDataException("API returned bad data")
            sys.exit(1)

        content = self.link_content(uri)
        data['visitors'] = visitors
        data['uri'] = uri
        data['content'] = content['data']['content']
        data['phrase'] = phrase
  
        return data


    """
    Retrieves the top phrase, uri, visitor count, and content
    from the hot_phrases API endpoint and builds
    a hashtable with the aformentioned data
    """
    def top_hot_content(self):
        hot = self.hot_phrases()
        data = {}

        try:
            phrase = hot['data']['phrases'][0]['phrase']
            top_link = hot['data']['phrases'][0]['urls'][0]['aggregate_url']
            visitor_count = hot['data']['phrases'][0]['urls'][0]['visitors']

        except KeyError:
            raise BitDataException("Top Hot Content Error: API returned bad data")
            sys.exit(1)

        content = self.link_content(top_link)
        data['visitors'] = visitor_count
        data['uri'] = top_link
        data['content'] = content['data']['content']
        data['phrase'] = phrase

        return data


class BitDataException(Exception):
    pass    
