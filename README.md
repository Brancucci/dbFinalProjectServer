# dbFinalProjectServer

Server API for touring application for web applications.

## Usages

### Log In

In order to login, make a `POST` request to the following endpoint 'http://django-env.92j4wqasxc.us-east-1.elasticbeanstalk.com/Touring360/login`. The body of the request needs to contain the user's `email` and `password`.

The response is in JSON Format like so

```
{
  "notFound": false,
  "wrongPassword": false,
  "success": true,
}
'''

The `notFound` flag is set to true when a no user is found using the login credentials.

The `wrongPassword` is set to true when no user is found that matches the email+password pair.

The `success` flag is only set to true when the user is successfully validated.