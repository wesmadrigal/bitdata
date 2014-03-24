#!/usr/bin/env python
import urllib2
import json
import sys


class BitData(object):
    
    def __init__(self, access_token):
        self._token = access_token
        self._requests = 0
        self._request_session = 0

    """
    Section 1:
        interface for bit.ly link shortening
        and unshortening functionality
    """

    def expand(self, short_url):
        """ Returns the canonical expanded version of a bit.ly short url """

        api = 'https://api-ssl.bitly.com/v3/expand?shortUrl={0}&access_token={1}'
        try:
            req = urllib2.Request(api.format(short_url, self._token))
            resp = urllib2.urlopen(req)
            if resp.code not in range(200,300):
                raise BitDataException("Link Expansion Error")
        
        except urllib2.URLError:
            sys.exit(1)

        return json.loads(resp.read())

    def info(self, short_url):
        """ Returns some basic info on a bit.ly short url """

        api = 'https://api-ssl.bitly.com/v3/info?shortUrl={0}&access_token={1}'
        try:
            req = urllib2.Request(api.format(short_url, self._token))
            resp = urllib2.urlopen(req)
            if resp.code not in range(200,300):
                raise BitDataException("Link Info Error")
 
        except urllib2.URLError:
            sys.exit(0)
        
        return json.loads(resp.read())

    
    def lookup_link(self, link):
        """ Returns bit.ly short url for the parameterized link if it exists """

        api = 'https://api-ssl.bitly.com/v3/link/lookup?access_token={0}&url={1}' 
        try:
            req = urllib2.Request(api.format(self._token, link))
            resp = urllib2.urlopen(req)
            if resp.code not in range(200,300):
                raise BitDataException("Link Lookup Error")
            
        except urllib2.URLError:
            sys.exit(1)

        return json.loads(resp.read())


    def shorten(self, link, domain=None):
        """ Returns shortened url """

        api = 'https://api-ssl.bitly.com/v3/shorten?access_token={0}&longUrl={1}'
        if domain:
            api += '&domain={2}'

        try:
            formatted = api.format(self._token, link) if not domain else api.format(self._token, link, domain)
            req = urllib2.Request(formatted)
            resp = urllib2.urlopen(req)
            if resp.code not in range(200,300):
                raise BitDataException("Shorten Link Error")
         
        except urllib2.URLError:
            sys.exit(1)

        return json.loads(resp.read())   


    def link_edit(self, edit_fields, edits, link):
        """
        Arguments

        edit_fields -- list
        edits       -- list
        link        -- string

        Returns affirmation json
        """

        api = 'https://api-ssl.bitly.com/v3/user/link_edit?access_token={0}&edit={1}&{2}&link={3}'
        try:
            fields = ','.join(edit_fields)
            edits = [ 
                      '{0}={1}'.format(edit_fields[i], edits[i].replace(' ', '+'))
                      for i in range(len(edits))
                    ]
            edits = '&'.join(edits)
            formatted = api.format(self._token, fields, edits, link)
            req = urllib2.Request(formatted)
            resp = urllib2.urlopen(req)
            if resp.code not in range(200,300):
                raise BitDataException("Link Edit Error")
     
        except urllib2.URLError:
            sys.exit(1)

        return json.loads(resp.read())
             
                    
    def user_link_lookup(self, link):
        """ Returns bit.ly short url(s) from a canonical url """

        api = 'https://api-ssl.bitly.com/v3/user/link_lookup?access_token={0}&url={1}' 
        try:
            req = urllib2.Request(api.format(self._token, link))
            resp = urllib2.urlopen(req)
            if resp.code not in range(200, 300):
                raise BitDataException("User Link Lookup Error")

        except urllib2.URLError:
            sys.exit(1)

        return json.loads(resp.read())


    def user_link_save(self, link):
        """ Returns json containing 1 if first request for save 0 if not """

        api = 'https://api-ssl.bitly.com/v3/user/link_save?access_token={0}&longUrl={1}' 
        try:
            req = urllib2.Request(api.format(self._token, link))
            resp = urllib2.urlopen(req)
            if resp.code not in range(200, 300):
                raise BitDataException("User Link Save Error")

        except urllib2.URLError:
            sys.exit(1)

        return json.loads(resp.read())

   
    """
    Section 2:
        bit.lys data APIs
    """

    def high_value(self, limit=2):
        """ Returns a specified number of "high-value" bitly links that are popular across bitly at this particular moment. """

        api = 'https://api-ssl.bitly.com/v3/highvalue?access_token={0}&limit={1}'
        try:
            req = urllib2.Request(api.format(self._token, limit))
            resp = urllib2.urlopen(req)
            if resp.code not in range(200,300):
                raise BitDataException("High Value Error")
            
        except urllib2.URLError:
            sys.exit(1)

        return json.loads(resp.read())


    def search(self, query_term, **kwargs):
        """ 
        Returns a json blob with links of queries 
         
        Params
       
            limit        -- int
            offset       -- int
            query        -- string
            lang         -- string
            cities       -- list
            domain       -- string
            full_domain  -- string
            fields       -- list
      
        """ 

        api = 'https://api-ssl.bitly.com/v3/search?access_token={0}&query={1}'
        try:
            for each in kwargs.items():
                if isinstance(each[1], str):
                    api += '&' + each[0] + '=' + each[1].replace(' ', '+').lower()
                elif isinstance(each[1], int):
                    api += '&' + each[0] + '=' + str(each[1])
                elif isinstance(each[1], list):
                    api += '&' + each[0] + '=' + ','.join(each[1]).lower().replace(' ', '+')
            formatted = api.format(self._token, query_term)
            req = urllib2.Request(formatted)
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

    """
    Section 3:
        link metrics
    """

    def link_clicks(self, link, **kwargs):
        """ Returns the number of clicks on a bit.ly shortened link """
 
        api = 'https://api-ssl.bitly.com/v3/link/clicks?access_token={0}&link={1}'
        try:
            if kwargs.items() != []:
                api += '&'.join(map(lambda x: x[0] + '=' + str(x[1]), kwargs.items()))
            formatted = api.format(self._token, link)
            req = urllib2.Request(formatted)
            resp = urllib2.urlopen(req)
            if resp.code not in range(200, 300):
                raise BitDataException("Link Clicks Error")

        except urllib2.URLError:
            sys.exit(1)

        return json.loads(resp.read())


    def link_countries(self, link, **kwargs):
        """ Returns the countries visiting a bit.ly shortened link """
 
        api = 'https://api-ssl.bitly.com/v3/link/countries?access_token={0}&link={1}'
        try:
            if kwargs.items() != []:
                api += '&'.join(map(lambda x: x[0] + '=' + str(x[1]), kwargs.items()))
            formatted = api.format(self._token, link)
            req = urllib2.Request(formatted)
            resp = urllib2.urlopen(req)
            if resp.code not in range(200, 300):
                raise BitDataException("Link Clicks Error")

        except urllib2.URLError:
            sys.exit(1)

        return json.loads(resp.read())


    def link_encoders(self, link, **kwargs):
        """ Returns the users who have encoded a bit.ly shortened link """
 
        api = 'https://api-ssl.bitly.com/v3/link/encoders?access_token={0}&link={1}'
        try:
            if kwargs.items() != []:
                api += '&'.join(map(lambda x: x[0] + '=' + str(x[1]), kwargs.items()))
            formatted = api.format(self._token, link)
            req = urllib2.Request(formatted)
            resp = urllib2.urlopen(req)
            if resp.code not in range(200, 300):
                raise BitDataException("Link Encoders Error")

        except urllib2.URLError:
            sys.exit(1)

        return json.loads(resp.read())


    def link_encoders_by_count(self, link, **kwargs):
        """
            Returns the users who have encoded a bit.ly shortened link sorted by 
            the number of clicks the encoded link got
        """
 
        api = 'https://api-ssl.bitly.com/v3/link/encoders_by_count?access_token={0}&link={1}'
        try:
            if kwargs.items() != []:
                api += '&'.join(map(lambda x: x[0] + '=' + str(x[1]), kwargs.items()))
            formatted = api.format(self._token, link)
            req = urllib2.Request(formatted)
            resp = urllib2.urlopen(req)
            if resp.code not in range(200, 300):
                raise BitDataException("Link Encoders By Count Error")

        except urllib2.URLError:
            sys.exit(1)

        return json.loads(resp.read())


    def link_encoders_count(self, link):
        """ Returns the number of users who have encoded a bit.ly shortened link """
 
        api = 'https://api-ssl.bitly.com/v3/link/encoders_count?access_token={0}&link={1}'
        try:
            formatted = api.format(self._token, link)
            req = urllib2.Request(formatted)
            resp = urllib2.urlopen(req)
            if resp.code not in range(200, 300):
                raise BitDataException("Link Encoders Count Error")

        except urllib2.URLError:
            sys.exit(1)

        return json.loads(resp.read())

    def link_referrers(self, link, **kwargs):
        """
            Returns the users who have encoded a bit.ly shortened link sorted by 
            the number of clicks the encoded link got
        """
 
        api = 'https://api-ssl.bitly.com/v3/link/referrers?access_token={0}&link={1}'
        try:
            if kwargs.items() != []:
                api += '&'.join(map(lambda x: x[0] + '=' + str(x[1]), kwargs.items()))
            formatted = api.format(self._token, link)
            req = urllib2.Request(formatted)
            resp = urllib2.urlopen(req)
            if resp.code not in range(200, 300):
                raise BitDataException("Link Referrers Error")

        except urllib2.URLError:
            sys.exit(1)

        return json.loads(resp.read())


    

class BitDataException(Exception):
    pass    
