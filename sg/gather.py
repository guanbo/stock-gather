# Copyright 2021 guanbo
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

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


class Gather(object):
  URLBase = 'https://hk.finance.yahoo.com/quote/##code##/key-statistics?lang=en&p=##code##'
  def __init__(self):
    self._mongo = MongoClient()
    self.db = self._mongo['stock']
    self.col = self.db['statistics']
    pass

  def pasre(self, code):
    url = self.URLBase.replace('##code##', code)
    print(url)
    page = requests.get(url, headers={'User-Agent': 'custom'})
    if page.status_code != 200:
      print(url, 'is response:', page.status_code)
      return

    soup = BeautifulSoup(page.content, "html.parser")
    record = {
      'code': code
    }
    job_elements = soup.find_all('tr')
    for job_element in job_elements:
      # print(job_element)
      items = list(job_element.find_all('td'))
      record[items[0].text.strip()] = items[1].text.strip()

    rec = self.db.statistics.insert_one(record)
    pass