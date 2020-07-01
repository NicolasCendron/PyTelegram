# Configuration #
###################

Waits config.json 

{
"api_id":"UNIQUE_ID",
"api_hash": "UNIQUE_HASH",
"password":"PASSWORD",
"host":"IP_HOST",
"port":"PORT_HOST"
}


## SETUP ##
Run Setup.py to enter your number, confirm identity and create session file
## Send Message ##

HOST:PORT/sendTelegramMEssage [POST]
JSON
{
"password":"YOUR_PASSWORD",
"phone":"PHONE_INTERNATIONAL", 
"message":"MESSAGE"
}

## Docker Build Example ##
sudo docker build -t telegram .

## Docker Run Example ##
sudo docker run --rm -d --network host --name telegram telegram

## Curl Example ##

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"password":"PASSWORD","phone":"NUMBER","message":"Message"}' \
  http://127.0.0.1:5000/sendTelegramMEssage

