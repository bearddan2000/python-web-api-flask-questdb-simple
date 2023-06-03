URL = 'http://py-srv:5000'

GET_BY_COLOR_URL = URL + '/dog/color/White'

GET_BY_BREED_URL = URL + '/dog/breed/Labrador'

GET_ALL_URL = URL + '/dog'

STATIC = {
  "results": {
    "count": 4,
    "data": [
      {
        "color": "White",
        "id": 1,
        "name": "Am Bulldog"
      },
      {
        "color": "Grey",
        "id": 2,
        "name": "Blue Tick"
      },
      {
        "color": "Black",
        "id": 3,
        "name": "Labrador"
      },
      {
        "color": "Brown",
        "id": 4,
        "name": "Gr Shepard"
      }
    ]
  }
}

INSERT_URL = URL + '/dog/breed/Poodle/color/Green'

SMOKE_URL = URL + '/'

SMOKE = {'results': {"hello": "world"}}
