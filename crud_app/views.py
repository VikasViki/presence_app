
from rest_framework import viewsets
from django.http.response import JsonResponse
from mongo_helper import get_mongo_collection

def health_check(request):
    return JsonResponse({"msg": "I am healthy"})

class CrudView(viewsets.ViewSet):

    def __init__(self):
        self.crud_collection = get_mongo_collection("postman_app", "crud_app")
    
    def _remove_id_from_result(self, result):
        result.pop("_id")

    def add_record(self, request):
        response = {"status": False}

        try:
            request_data = request.data
            
            db_result = self.crud_collection.insert_one(request_data)
            print("DEBUG", str(db_result.inserted_id))
            response["db_result"] = str(db_result.inserted_id)
            
            response["status"] = True

        except Exception as e:
            response["error"] = str(e)

        return JsonResponse(response)

    def read_record(self, request):
        response = {"status": False}
        
        try:
            request_data = request.data
            test_id = request_data.get("test_id")
            if test_id == None:
                raise Exception("test_id is required field")

            db_result = self.crud_collection.find_one({"test_id": test_id})
            self._remove_id_from_result(db_result)
            response["db_result"] = db_result

            response["status"] = True

        except Exception as e:
            response["error"] = str(e)

        return JsonResponse(response)

    def update_record(self, request):
        response = {"status": False}
        
        try:

            response["status"] = True
        except Exception as e:
            response["error"] = str(e)

        return JsonResponse(response)

    def delete_record(self, request):
        response = {"status": False}
        
        try:

            response["status"] = True
        except Exception as e:
            response["error"] = str(e)

        return JsonResponse(response)