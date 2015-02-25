# Copyright Licencing:
# MIT Licence

# Project Title: AuroraCoin tip-bot
# Module Title: API Abstraction Module
# Author: Joseph Lee
# Email: joseph.lee.esl@gmail.com
# Date: 2015-01-26

# Description:
# This package abstracts the web API connection details.  Profiles for connecting to sources can be created here. 
# The profile name is passed into the object upon creation. 

# Import Basic Modules

class ApiConnection:
    def __init__(self, profile):
        # bland.is profile
        if profile == "bland":
            base_url = "https://api.bland.is/"
            key = "your_api_key"
            access_token= "your_access_token"
            # Bland.is requires three APIs for finding commands in user text
            self.categories_url = base_url + "messageboard/categories?api_key=" + key
            self.threads_url = base_url + "messageboard/?api_key=" + key + "&category_id="
            self.info_url = base_url + "me/info?access_token=" + access_token
            self.inbox_url = base_url + "me/message?access_token=" + access_token + "&limit="
            self.publish_url = base_url + "me/publishes?access_token=" + access_token
            self.new_post_url = base_url + "me/messageboard/?api_key=" + key + "&access_token=" + access_token
            self.parent_id_url = "&parent_id=" 
            self.message_url = "&message="
            self.aurora_node_balance = "http://104.236.66.174:3333/chain/Auroracoin/q/addressbalance/"
