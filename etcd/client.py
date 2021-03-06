import grequests
import requests

class Client(object):

  def __init__(self, host="localhost", port=4001):
    self.host = host
    self.port = port

  def get(self, name, full_response=False):
    return self._execute_command('GET', "keys", name,
                                 full_response=full_response)

  def set(self, name, value, full_response=False, ttl=None):
    data = { 'value': value }
    if ttl:
      data['ttl'] = ttl

    return self._execute_command('PUT', "keys", name, data,
                                 full_response=full_response)

  def mkdir(self, name, ttl=None, full_response=False):
    data = { 'dir': True }

    if not ttl:
      data['ttl'] = ttl

    return self._execute_command('PUT', "keys", name, data, no_answer=True,
                                 full_response=True)

  def listdir(self, name, recursive=False):
    return self._execute_command('GET', "keys", "%s/?recursive=%s" % (name, recursive),
                                 full_response=True)


  def delete(self, name, full_response=False):
    return self._execute_command('DELETE', "keys", name, no_answer=True,
                                 full_response=full_response)

  def refresh_dir(self, name):
    pass

  def refresh(self, name, ttl, value=None):
    data = { 'prevExist': True }

    if value:
      data['value'] = value

    if ttl:
      data['ttl'] = ttl

    return self._execute_command('PUT', "keys", name, data,
                                 full_response=True)

  def watch(self, name, recursive=False):
    while True:
      try:
        response = self._execute_command('GET', "keys", "%s?wait=true&recursive=%s" % (name, recursive), full_response=True)
        yield response
      except requests.exceptions.Timeout:
        pass

  def _base_url(self):
    return "http://%s:%s/v2" % (self.host, self.port)

  def _parse_response(self, response, full_response=False, no_answer=False):
    if full_response == True:
      return response.json()
    else:
      if no_answer == True:
        return None

      return response.json()["node"]["value"]

  def _execute_command(self, verb, prefix, path, data=None, full_response=False,
                       no_answer=False, timeout=None):
    partial_requests = getattr(requests, verb.lower())
    url = "%s/%s/%s" % (self._base_url(), prefix, path)

    if data == None:
      data = {}

    if timeout == None:
      timeout = 60

    response = partial_requests(url, data=data, timeout=timeout)

    return self._parse_response(response, full_response=full_response,
                                no_answer=no_answer)
