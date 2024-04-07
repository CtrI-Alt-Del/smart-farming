# Archtecture

## System Design

<img src="../images/system-design.png" alt="system design" />

## Folders structure
```bash
. # Root
├── documentation/ 
├── src/ # All our code
│   ├── app/ # Backend code
│   │   ├── core/ # Related to business rules code
│   │   │   ├── commons/ # Pieces of the business rules that repeat
│   │   │   ├── constants/ # global and imutable values  
│   │   │   ├── entities/ # classes to indentify a record of the business rules
│   │   │   └── use_cases/ # Features of the business rules
│   │   ├── infra/ # Related to external technologies, serivices and libs to sustain the backend
│   │   │   ├── database/ # Related to a database
│   │   │   ├── repositories/ # Classes to manipulate the database
│   │   │   ├── auth/ # Related to authentication of users
│   │   │   ├── forms/ # Classes to build forms of frontend 
│   │   │   ├── providers/ # Classes to manipulate external libs
│   │   │   ├── views/ # Functions to handle routes and return html
│   │   │   └── utils/ # Utilities classes to asbtract backend features like folder/files handling
│   │   └── main.py
│   └── ui/ # Frontend code
│       ├── static/ # assets files to use in Html
│       │   ├── styles/ # CSS files
│       │   ├── scripts/ # Javascript files
│       │   └── images/ # images (png, jpg, gif or svg)
│       └── templates/ # Html files
│           ├── layouts/ # Container of pages
│           ├── pages/ # Pages of website
│           └── components/ # Reusable UI components such as buttons cards, and modals
```

