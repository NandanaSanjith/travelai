# travelai
travel project server
# pending work
## backend 
data injestion for all airports 
get all airports using rest api
email after booking
email with weather information
bus booking system
## frontend
more styling 
booking confirmation or booking error
chat api window
bus booking

### Backend Installation
## Run Rest Server
 - open terminal 
 - cd <proj-folder>\backend\rest_api
 - poetry install
 - poetry run fastapi dev src\rest_api\main.py

## Install Stripe
 - open terminal 
 - make sure stripe is installed from this location https://github.com/stripe/stripe-cli/releases/download/v1.31.1/stripe_1.31.1_windows_x86_64.zip
 - Unzip the file and move to "c:\stripe" folder

## Run Stripe
 - open terminal 
 - cd c:\stripe
 - stripe login 
 - stripe listen --forward-to localhost:8000/webhook
 - copy the "whsec_" key to .env STRIPE_WEBHOOK_SECRET


## Run Frontend
 - open terminal 
 - cd <proj-folder>\frontend\travel-ai
 - npm install
 - npm run dev