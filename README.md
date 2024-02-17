1. Presence status update
- get user id from client
- update users presence flag in db.


## Database:

users_presence

{
    user_id: "",
    is_present: True/ False,
    last_visited_time: now()  - when toggle from True to False
}


2. Querying presence information

- get workspace id (omitted for now)
- query in db with is_present = True
- return list of user_id