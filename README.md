 # Back-end-Application-Development-Capstone-Project
https://www.coursera.org/learn/backend-development-capstone-project

![image](https://github.com/user-attachments/assets/8bf02361-31a6-4099-af3f-4d7116ce364d)



## M1 - FLASK basics:

![image](https://github.com/user-attachments/assets/99eea4ce-9129-47ff-817f-56ac9352c3de)

![image](https://github.com/user-attachments/assets/f99e5f98-d6a7-4083-9f6b-cbf26c550013)

![image](https://github.com/user-attachments/assets/2ccc039d-f059-4569-ada2-a72aa18da466)

![image](https://github.com/user-attachments/assets/740b1d95-c18c-4cf1-acce-b2b2642fc972)

![image](https://github.com/user-attachments/assets/a84534d2-3cb7-4e7f-aef7-0912b5ba3f96)

![image](https://github.com/user-attachments/assets/ff354d68-67fb-4338-bc37-334d695be60e)

![image](https://github.com/user-attachments/assets/53f6f92e-cb57-4e51-9cf8-bcfd396b7aad)

![image](https://github.com/user-attachments/assets/af5017f9-00d7-4fec-bdfc-c4d841e66f1d)

![image](https://github.com/user-attachments/assets/43f968fc-4312-40d4-8043-7254cc6d4d33)

### basic application and routes

- first, import 'Flask' class from the module 'flask'
- next, Instantiate an object on the FLask class as your APP.
  ![image](https://github.com/user-attachments/assets/9487a8a7-6b39-4594-b90f-458cbc9c1b34)

- adding routes
  ![image](https://github.com/user-attachments/assets/a025a9de-6a6c-4d0e-afbc-8fbd575187bb)

- define flask app and development variables.
- run the applicaiton
  ![image](https://github.com/user-attachments/assets/78406dbe-9bda-40c5-b807-0600ffaa82b4)

- run falsk with Arguments
  ![image](https://github.com/user-attachments/assets/8f8dd633-7d26-4e53-9f4b-7e9018896c51)

- returning JSON
- 2nd way: using jsonify()
  ![image](https://github.com/user-attachments/assets/e2a8682f-a24d-4a9d-8a15-c1283c704bed)
  ![image](https://github.com/user-attachments/assets/38ae3e7c-1583-44ae-9e94-18940eba3208)

- application configuration
- loading configuration
  ![image](https://github.com/user-attachments/assets/90324da5-748c-4e2d-b703-fd52aad9450a)
  ![image](https://github.com/user-attachments/assets/d3ae1e6a-f9e7-4563-acb4-66eab14a8d6a)

- application structure
  ![image](https://github.com/user-attachments/assets/906e0647-0265-496f-a0ca-e3da45e2eaef)

### Request and Response Objects
- flask **Request** Object
  ![image](https://github.com/user-attachments/assets/a8af52db-91a6-4051-a259-e7c4030029db)
  ![image](https://github.com/user-attachments/assets/a359e0d2-9f90-43b5-8569-97f0d614a101)
  ![image](https://github.com/user-attachments/assets/e75e68ae-0e01-4dd8-8a09-1dac1c9a4f74)

- Flask Response Object (send back to the clients)
  ![image](https://github.com/user-attachments/assets/0de6c648-18dd-45ba-959d-2300a1068aa3)
  ![image](https://github.com/user-attachments/assets/f70bcecd-06cc-4657-b56d-9a86f9bcd143)

- custome routes examples
  ![image](https://github.com/user-attachments/assets/ef095101-0cac-4653-a95d-70571878db82)


### Dynamic Routes
- how to call an **external API**
  - use python requests library
  ![image](https://github.com/user-attachments/assets/0a92c4cc-16cd-4526-9c99-044f9121d3ab)

- how to pass **parameters to routes** in Flask
  - dynamic route parameters
    ![image](https://github.com/user-attachments/assets/03d6fc84-168c-47ff-82c1-d2484a33519c)
    ![image](https://github.com/user-attachments/assets/9d91c37a-2a15-4289-9c8a-5242138a7a08)

### Error Handing
- HTTP return status
  ![image](https://github.com/user-attachments/assets/41fd8cd7-32de-4755-af08-c82782e44d86)
  ![image](https://github.com/user-attachments/assets/5cbbdd3e-e6e9-46a2-b88e-2a8284368ff4)

- error handling in flask
 - return status: Explicit
    ![image](https://github.com/user-attachments/assets/aac48bad-e185-4d97-bc45-9573b7896769)
   
- how to return erros from API in flask
![image](https://github.com/user-attachments/assets/be76020c-b21b-4f8a-9518-534f0f657703)
 - call this end-point with curl command
   ![image](https://github.com/user-attachments/assets/2c49abe4-6f23-4baa-9c18-f567d9a63f13)
   ![image](https://github.com/user-attachments/assets/5354517b-944b-4dcc-927c-ca99e6d5eb16)
   ![image](https://github.com/user-attachments/assets/8274aba9-01d6-4447-9b49-153841c88bc2)


## M2 - MongoDB, NoSQL
- NoSQL (key-value, Document, Column, Graph)

### NoSQL
![image](https://github.com/user-attachments/assets/3e749c57-bcb7-4382-bccd-7122c0eacd18)

- benefits: Scalability, Performance, Availability, Cloud Architecture, Cost, Flexible Schema, Varied Data Structures, Specialized Capabilities 

### Document-based
![image](https://github.com/user-attachments/assets/27b8e893-18dc-4da4-bbfa-9a0609cfcf09)
![image](https://github.com/user-attachments/assets/f5fe8bb7-b36e-4eb1-bebf-ce13959a93dd)
![image](https://github.com/user-attachments/assets/f04b8aca-5e8f-457e-8ae0-9ce0b06307a1)

### MongoDB overview
![image](https://github.com/user-attachments/assets/1b928c2b-325a-49ab-bd68-5a8324d8d83e)

### CRUD
Create: insertOne(), inertMany()
![image](https://github.com/user-attachments/assets/2cf368aa-24ac-467c-9aa8-52443b0c6dd9)

Read: findOne(), find(), count(),
![image](https://github.com/user-attachments/assets/daa5eb74-0b5a-4d20-9485-d1d2a11c6047)
![image](https://github.com/user-attachments/assets/3c5076fd-d7a5-49da-83f9-ab8d75ec1dbc)


Update: replaceOne(), updateOne(), updateMany()
![image](https://github.com/user-attachments/assets/6a861796-be39-4333-b3db-953fce491c8b)
![image](https://github.com/user-attachments/assets/96c92888-73c8-405c-b643-68836eda5af6)

Delete: deleteOne(), deleteMany()
![image](https://github.com/user-attachments/assets/bc12c082-02b5-4f0d-a43e-81f6fe6be4bf)

### Access MongoDB from Python

- MongoClient (a class help to interact with MongoDB)
  ![image](https://github.com/user-attachments/assets/5621842a-4a4f-4aba-b74c-c142b6046415)

![image](https://github.com/user-attachments/assets/c369c839-48fd-4b95-a758-d621b418ae5b)


### Creating Songs with MongoDB and Flask (2nd lab)
- overview: create a service in Flask that gets songs from MongoDB database.
- todo:
 - start MongoDB database server
 - create a flask server
 - write RESTful APIs on song resource
 - test the APIs


## M3 - Main Django Application
- create a Django application and connect it to services
- create a data model and use Django migration tool to create the tables and relationships
- create controllers to implement business logic to send appropriate data to the provided templates

## M4 - Deploy your application and services

- intro to serverless with code engine
  ![image](https://github.com/user-attachments/assets/2fe14c21-d1ca-48a2-b345-997591f5fcbd)

![image](https://github.com/user-attachments/assets/e17453d5-e559-4044-9e62-80fca8415fb9)

![image](https://github.com/user-attachments/assets/c80030c8-7ec9-4841-ad15-5669f97d1482)



- deploy your application and services

