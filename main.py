import os

import fitbit

client_id = os.environ.get("client_id")
client_secret = os.environ.get("client_secret")

auth_user = fitbit.Fitbit(client_id, client_secret)

