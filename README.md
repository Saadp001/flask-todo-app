# 📌 **Flask To-Do App – Full Stack + Docker + CI/CD + AWS EC2 Deployment**

A fully functional **Flask CRUD application** with:

* Task creation, editing, deleting
* Marking tasks as completed
* Clean UI (HTML + SCSS)
* REST API (GET/POST/PUT/PATCH/DELETE)
* Dockerized application
* CI/CD using GitHub Actions
* Deployment to AWS EC2 using Docker Hub

---

## 🚀 **Features**

### ✔ Task Management

* Add new tasks
* Edit existing tasks
* Delete tasks
* Mark tasks as completed
* Automatic timestamps

### ✔ REST API Endpoints

| Method | Endpoint                   | Description            |
| ------ | -------------------------- | ---------------------- |
| GET    | `/api/tasks`               | Get all tasks          |
| POST   | `/api/tasks`               | Create new task        |
| GET    | `/api/tasks/<id>`          | Get task by ID         |
| PUT    | `/api/tasks/<id>`          | Update task            |
| DELETE | `/api/tasks/<id>`          | Delete task            |
| PATCH  | `/api/tasks/<id>/complete` | Mark task as completed |

### ✔ DevOps & Deployment

* Dockerized application
* GitHub Actions CI/CD pipeline
* Auto-push Docker images to Docker Hub
* Auto-pull & reload container on AWS EC2
* Stable production deployment on port `5000`

---

## 🐳 **Docker Setup**

### Build Image

```bash
docker build -t flask-todo-app .
```

### Run Container

```bash
docker run -p 5000:5000 flask-todo-app
```

---

## 🔧 **GitHub Actions CI/CD Pipeline**

The workflow:

1. On every `git push` to `main`
2. GitHub builds Docker image
3. Pushes to Docker Hub
4. SSH into EC2
5. Pulls latest image
6. Restarts the container

Workflow file: `.github/workflows/deploy.yml`

---

## ☁️ **EC2 Setup**

* Ubuntu instance
* Installed Docker + Docker Compose
* Opened port `5000` in Security Group
* Added SSH key to GitHub Secrets

---

## 📁 **Project Structure**

```
├── app.py
├── Dockerfile
├── requirements.txt
├── static/
│   ├── css/
│   └── scss/
├── templates/
│   ├── index.html
│   └── edit.html
├── instance/
├── .dockerignore
└── README.md
```

---

## 👨‍💻 **Tech Stack**

* **Python / Flask**
* **SQLAlchemy (SQLite)**
* **HTML, CSS, SCSS**
* **REST APIs**
* **Docker**
* **GitHub Actions**
* **AWS EC2**
* **Linux & SSH**

---

## 📸 **Screenshots**


<img width="1000" height="500" alt="Screenshot (646)" src="https://github.com/user-attachments/assets/64762d3b-9d17-4076-8231-512ba27a00bf" />

<img width="1600" height="858" alt="Screenshot (645)" src="https://github.com/user-attachments/assets/db2fe169-9915-4de7-9a41-b98f432685d6" />

---

## ⭐ **Future Enhancements (Optional)**

* User authentication (Flask-Login / JWT)
* Per-user task lists
* Pagination
* Priority categories
* Docker Compose multi-container setup
* Nginx reverse proxy + HTTPS

---

# 🙌 **Author**

**Saad Patel**
DevOps & Cloud Enthusiast | Python & Backend Learner
(Insert your social links)

---


