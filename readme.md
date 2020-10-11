# mahadata-server
Work in progress!

## To run:
- Create an `.env` file. An example can be found on `.env.example` file
- Run `docker-compose up -d` - it will spin up the Flask server and the Redis instance

## API Documentation

#### Get mobility data

Province level data


**URL** : `/data/daily/province`

District level data

*Mobility and ratio*

**URL** : `/data/daily/district`

**Method** : `GET`

**Response:**
```json
  [{
        "date": "[timestamp]",
        "data": { "region_name": {
            "change": "[float]",
            "ratio": "[float]",
            "color": "[array]",
          }}
    }]
```

*Daily cumulative case*

**URL** : `/data/case/province`

**Method** : `GET`

**Response:**
```json
  [{
        "date": "[timestamp]",
        "data": { "region_name": "[int]"}
    }]
```

*Get ranking data*

**URL** : `/data/rank/<district OR province>
`

**Method** : `GET`

**Response:**
```
{
	"ratio": {
		"top": [{
			"Sarmi": 28.0
		}, {
			"Mappi": 29.0
		}, {
			"Paniai": 31.0
		}],
		"bottom": [{
			"Salatiga": 11.0
		}, {
			"Sukoharjo": 11.0
		}, {
			"Karanganyar": 11.0
		}]
	},
	"change": {
		"top": [{
			"Bombana": 14.0
		}, {
			"Takalar": 19.0
		}, {
			"Mandailing Natal": 21.0
		}],
		"bottom": [{
			"Kota Yogyakarta": -12.0
		}, {
			"Jakarta Pusat": -11.0
		}, {
			"Manggarai Timur": -11.0
		}]
	}
}
```

