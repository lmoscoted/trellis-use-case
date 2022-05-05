# Django Docker NGINX app for Production Deployment

Django app for deployment an app for production.

#### Python Django application exposes two endpoints:
* GET /num_to_english?number=12345678
* POST /num_to_english
  
    ```
    {
    “number”: “12345678”
    }
    ```
This endpoints will convert any number given to it into the english words that describe that
number. For example the above request should return:

```
{
“status”: “ok”,
“num_in_english”: “twelve million three hundred forty five thousand six hundred seventy eight”
}
```
### How to run
1. Update the .env file. You have to copy the _.env.example_ update it accordingly (only for production) and rename it to _.env_
   - For deployment: Run `docker compose  -f docker-compose-deploy.yml up --build` and you can access the ALLOWED_HOSTS in the _.env_ file on the port _8080_
   - For local developmnet: Run `docker compose  -f docker-compose.yml up --build` and you can access http://localhost:8000