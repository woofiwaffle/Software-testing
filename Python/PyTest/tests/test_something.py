import requests

from Python.PyTest.configuration import SERVICE_URL

from Python.PyTest.src.baseclasses.response import Response
from Python.PyTest.src.schemas.post import POST_SCHEMA
from Python.PyTest.src.pydantic_schemas.post import Post

def test_getting_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    response.assert_status_code(200).validate(Post)