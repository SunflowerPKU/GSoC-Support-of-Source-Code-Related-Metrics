**Microtask 3**:
====================
Based on the JSON documents produced by Perceval and its source code, try to answer the following questions:
------------------------------------------
* **What is the meaning of the JSON attribute 'timestamp'?**  
The Unix timestamp that the data was retrieved.
* **What is the meaning of the JSON attribute 'updated_on'?**  
The last time (Unix timestamp) the data was modified.
* **What is the meaning of the JSON attribute 'origin'?**  
URI of the data source, e.g., Git repository, Bugzilla server URL.
* **What is the meaning of the JSON attribute 'category'?**  
It includes the types of data that was retrieved, such as 'issue' and 'pull_request' fetched by perceval.backends.core.github.
* **What is the meaning of the JSON attribute 'uuid'?**  
It is universally unique identifier (UUID), which is a 128-bit number used to identify this data.
* **Which are the common methods of the Perceval backends?**  
For example:  
  ```
  1) fetch(self, category, **kwargs) # Fetch items from the repository. 
  2) fetch_items(category, **kwargs) #Fetch the certain item from the category.  
  3) metadata_category(item) #Extracts the category from a item.
  ```
* **List and explain at least 3 Git commands used by the Perceval backend (you can rely on the Git documentation).**  
  ```
  1) $ perceval git 'https://github.com/chaoss/grimoirelab-perceval.git' --from-date '2016-01-01'  
  fetch commits from https://github.com/chaoss/grimoirelab-perceval.git newer than '2016-01-01'(inclusive).

  2) $ perceval bugzilla 'https://bugzilla.redhat.com/' --backend-user user --backend-password pass --from-date '2016-01-01'  
  fetch bugs from https://bugzilla.redhat.com/ newer than '2016-01-01'(inclusive).

  3) $ perceval github elastic logstash  
  fetch issues and pull-request data from elastic's project – logstash.
  ```

