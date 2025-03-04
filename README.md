# Road-Ticket-Management (This README file is subject to continuous change as I learn and document my progress.)

This is a road ticket management project for motorists and officials to replace the current system in Nigeria, which causes confrontations between both parties due to the lack of means to make payments conveniently and the inability to monitor and track tickets, as the current system is paper-based. The aim of the project is to create a platform for seamless payment of road traffic tickets, monitor and track tickets, and completely remove unnecessary confrontations between motorists and officials, as the current system gives rise to all these problems.

The project is also my attempt at project-based learning and solving a problem in my home country, Nigeria. I aim to learn basic backend concepts as I implement them in this project. These concepts are:

- Database creation and population
- Basic CRUD operations
- Basic authentication and authorization
  
I am using Django as the backend framework and PostgreSQL as the database. The frontend was created using basic HTML and CSS.

This is the first implementation of the project (V1). I intended to implement a number of features, and after research, I concluded that they were necessary for the project to meet its functional requirements.

Features for (V1):

- Sign-in and log-in (Authentication)
- Profile creation (CRUD)
- Ticket creation for officials (CRUD)
- Frontend for ticket monitoring (CRUD)
- Means for disputing tickets for motorists (CRUD)
- Means to pay for tickets (CRUD)


During the process of working on authentication, I realized I needed a more customized model after using the default model, which caused migration problems. This issue helped me learn about database migrations and how to manage them. I made migration changes on a new branch, but upon merging, it seemed to cause irreversible problems. This led me to move to the second implementation of the project (Road-Ticket-Management1).
