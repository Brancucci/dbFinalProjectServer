# dbFinalProjectServer

Server API for touring application for web applications.

## Usages

### Log In

In order to login, make a `POST` request to the following endpoint `http://django-env.92j4wqasxc.us-east-1.elasticbeanstalk.com/Touring360/login`. The body of the request needs to contain the user's `email` and `password`.

The response is in JSON Format like so

```
{
  "notFound": false,
  "wrongPassword": false,
  "success": true,
}
```

The `notFound` flag is set to true when a no user is found using the login credentials.

The `wrongPassword` is set to true when no user is found that matches the email+password pair.

The `success` flag is only set to true when the user is successfully validated.

### Register New User

To register a user, execute a `POST` request to the following endpoint `http://django-env.92j4wqasxc.us-east-1.elasticbeanstalk.com/Touring360/register`. The body of the request needs to contain the following parameters

* email
* password
* phone
* city
* country
* address
* firstName
* lastName

The response is in JSON format like so

```
{
  "error": false,
  "taken": false,
  "success": true
}
```

The `error` flag is set to true if there was an error while executing the request.

The `taken` flag is set to true if an user with the same email already exists.

The `success` flag is set to true if the registration was a success.

### search

This API allows users to search hosts by city only, country only, and city and country, Start date and end date are optional but if used, both are required together. 

In order to perform a search, perform a `GET` request to the following endpoints

Searching by city: `http://django-env.92j4wqasxc.us-east-1.elasticbeanstalk.com/Touring360/search/city`

Searching by country: `http://django-env.92j4wqasxc.us-east-1.elasticbeanstalk.com/Touring360/search/country`

Searching by city and country: `http://django-env.92j4wqasxc.us-east-1.elasticbeanstalk.com/Touring360/search/city&country`

This request takes a query string. For example
Searching by city:
`http://django-env.92j4wqasxc.us-east-1.elasticbeanstalk.com/Touring360/search/city?city=Tampa`

Searching by country:
`http://django-env.92j4wqasxc.us-east-1.elasticbeanstalk.com/Touring360/search/country?country=USA`

Searching by city and country:
`http://django-env.92j4wqasxc.us-east-1.elasticbeanstalk.com/Touring360/search/city&country?city=Tampa&country=USA&start_available_date
=2017-05-01&end_avilable_date=2017-05-20`

The response is in JSON format like so

```
{
  "error": false, 
  "found": true, 
  "results": [
  {
    "email": "awesome@mail.com", 
    "city": "Tampa", 
    "country": "United States", 
    "start_date": "2017-03-31", 
    "account_num": "111111111", 
    "routing_num": "1111111", 
    "bio": "A cool Host", 
    "revenue": null, 
    "start_available_date": "2017-01-01", 
    "end_available_date": "2017-12-12", 
    "rating": 0
    }
  ]
}
```

The `error` flag is set to true when an error occurs.

The `found` flag is set to true when hosts are found in a given search.
