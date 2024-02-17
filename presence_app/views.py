from django.shortcuts import render

from mongo_helper import get_mongo_collection
from rest_framework import viewsets
from django.http.response import JsonResponse
import time

class PresenceView(viewsets.ViewSet):

    def __init__(self):
        self.users_presence_collection = get_mongo_collection("postman_app", "users_presence")
    
    def update_users_presence_state(self, request):

        response = {"status": False}

        try:
            request_data = request.data
            user_id = request_data.get("user_id")
            presence_state = request_data.get("is_present")

            # Check if user is alreay present
            db_result = self.users_presence_collection.find_one({"user_id": user_id})
            # print("Line 23 DEBUG : ", db_result)

            # Update presence state in Db
            if db_result:
                if db_result["is_present"] != presence_state:
                    if presence_state == True:
                        self.users_presence_collection.find_one_and_update(
                            {"user_id": user_id},
                            {"$set": {"is_present": presence_state}}
                        )
                    else:
                        self.users_presence_collection.find_one_and_update(
                            {"user_id": user_id},
                            {"$set": {
                                "is_present": presence_state,
                                "last_visited_time": time.time()
                                }
                            }
                        )
                    
                    response["message"] = f"presence state changed to {presence_state} for {user_id}"
            
            else:
                if presence_state is True:
                    self.users_presence_collection.insert_one(
                        {
                            "user_id": user_id,
                            "is_present": presence_state
                        }
                    )
                    response["message"] = f"presence state updated for {user_id}"

                else:
                    response["message"] = "First presence state should be True"
            
            response["status"] = True
        except Exception as e:
            response["exception"] = str(e)
        
        return JsonResponse(response)
    

    def get_all_present_users(self, request):
        response = {"status": False}

        try:
            request_data = request.data

            # Query all active users from DB
            present_user_ids = []
            present_users_cursor = self.users_presence_collection.find({"is_present": True})
            
            for user in present_users_cursor:
                print("77 DEBUG", user)
                present_user_ids += [user.get("user_id")]
            
            response["active_users"] = present_user_ids
            
            response["status"] = True
        except Exception as e:
            response["exception"] = e
        
        return JsonResponse(response)