# Road-Ticket-Management (This README file is subject to continous change as i learn and document my progress)

This is a road ticket management project for motorists and officials to replace the current system in Nigeria which causes confrontations between both parties due to lack of means to make payments convienently and means to monitor and track tickets as the current system is paper based. 
The aim of the project is to create a platform for seamless payment of road traffic tickets, monitor and track tickets and completely remove unnecesary confrontations between motorists and officials as the current system gives rise to all these problems.

The project is also my attempt on project based learning. I aim to learn basic backend concepts as I implement them on this project. Which are;
- Database creation and population.
- Basic CRUD operations.
- Basic Authentication and authorization.

I am making use of the Django as the backend framework and PostgreSQL as the database. The frontend was created using basic HTML and CSS. 

This is the first implementation of the project(V1). I intended to implement a number features which after research came to the conclusion where necessary for the project to meet its functional requirements. 

Features for (V1):
- Sign In and Log In. (Authentication)
- Profile creation. (CRUD)
- Ticket creation for officials. (CRUD)
- Frontend for ticket monitoring. (CRUD)
- Means for disputing tickets for motorists. (CRUD)
- Means to pay for tickets. (CRUD)

In the process of working on the Authentication, I felt i needed a more customized model after using the default model which caused migration problems. This issue helped me learn about database migrations and how to manage them. I made migration changes on a new branch and on merging it seemed to cause irreversible problems. This made me move to the second implementatiom of the project (Road-Ticket-Management1)

