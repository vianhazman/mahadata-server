# mahadata-server
Work in progress!

## To run:
- Create an `.env` file. An example can be found on `.env.example` file
- Run `docker-compose up -d` - it will spin up the Flask server and the Redis instance

## API Documentation

#### Get mobility data

**URL** : `/data/daily`

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

