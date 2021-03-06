#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import json
import random
import urllib
import urllib2
import webapp2
import jinja2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        if self.request.get('term'):

            base_url = "http://api.giphy.com/v1/gifs/search?"
            url_params = {'q': 'puppy', 'api_key': 'dc6zaTOxFJmzC', 'limit': 10}
            giphy_response = urllib2.urlopen(base_url + urllib.urlencode(url_params))
            giphy_json_content = giphy_response.read()
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            gif_url = parsed_giphy_dictionary['data'][0]['images']['original']['url']
    #        self.response.write(gif_url)
            main_template = env.get_template('output.html')
            self.response.out.write(main_template.render())

        else:
            self.response.write("What do you want to see?")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

#class SearchHandler(webapp2.RequestHandler):
#    def get()
