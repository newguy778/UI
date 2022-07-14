from collections import namedtuple
firstname = "v1/firstname"
lastname = "v1/firstname"

API_ENDPOINT = namedtuple("END_POINTS", ['firstname', 'lastname'])

API = API_ENDPOINT(firstname, lastname)
