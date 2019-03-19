Microtask 7:
====================
Based on the JSON documents produced by Graal and its source code, try to answer the following questions:
------------------------------------------
* **Which are the common methods of the Graal backends?**  
```
 1) fetch(self, category=CATEGORY, paths=None, from_date=DEFAULT_DATETIME, to_date=DEFAULT_LAST_DATETIME, branches=None, latest_items=False)  
 Fetch items from the particular analyzer, such as fench commits and and add code complexity information.  
 
 2) fetch_items(self, category, **kwargs)  
 Fetch the commits and adds analysis information.
```
* **List and explain at least 2 Git commands used by Graal (and not implemented in Perceval).** 
```
 1) $ graal cocom https://github.com/chaoss/grimoirelab-perceval --git-path /tmp/graal-cocom > /graal-cocom.test
 The CoCom backend requires the URL where the repository is located (https://github.com/chaoss/grimoirelab-perceval) and the local path where to mirror the repository (/tmp/graal-cocom). 
 Then, the JSON documents produced are redirected to the file graal-cocom.test.

 2) $ graal cocom –h
 get information about a specific backend.
```
