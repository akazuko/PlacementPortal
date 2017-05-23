# PlacementPortal
A common placement portal that can be utilized by any university/institute

####Installation:

[Pre Requisites]
#####Mongod

- Have a mongod instance running at a server.


1. To install the required python packages

```commandline
# source the virtual env and cd into the cloned repo dir
pip install -r requirement.txt
```


2. Make a file at a secure location with the following the content:
```json
{
  "username": "<DB_USERNAME>", 
  "host": "<DB_HOSTNAME>", 
  "password": "<DB_PASSWORD>",
  "db": "<DB_NAME>"
}
```
3. Update the `MONGO_DB_INFO` in `portal/settings.py` with the absolute path to
 the file created in step above.
 
4. Run `python manage.py runserver <PORT>`