# python-web-api-flask-questdb-simple

## Description
Creates an api of `dog` table.
Has the ability to query by parameters.

Remotely tested with *testify*.

## Tech stack
- python
  - flask
  - testify
  - requests

## Docker stack
- python:latest
- questdb/questdb

## To run
`sudo ./install.sh -u`
- Get all dogs: http://localhost/dog
  - Schema breed and color
- Query with params: 
  - http://localhost/dog/breed/<breed>
  - http://localhost/dog/color/<color>

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credits
- [Questdb with python](https://tutswiki.com/setup-access-questdb-python-notebook/)