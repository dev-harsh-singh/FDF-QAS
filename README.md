# FDF-QAS
# AI-Powered Document Intelligence System

An intelligent PDF document retrieval system built using Python and MySQL. The application allows users to upload PDF documents, extract textual content, store it in a database, and retrieve relevant information through an interactive search interface.

This project serves as the foundation for a future AI-powered document question-answering system using NLP, Vector Databases, Retrieval-Augmented Generation (RAG), and Large Language Models (LLMs).

---

## Features

* Upload and process PDF documents
* Extract text using PyPDF2
* Store extracted content in MySQL
* Interactive menu-driven interface
* Search information across uploaded documents
* Continuous query mode for multiple searches
* Modular and scalable project structure
* Database-driven document management

---

## Project Structure

```text
PDF_Qus_Ans_Sys/
│
├── main.py
├── database.py
├── pdf_reader.py
├── upload.py
├── search.py
├── requirements.txt
└── README.md
```

---

## System Workflow

```text
User
 │
 ▼
Main Menu
 │
 ├── Upload Document
 │       │
 │       ▼
 │   Extract Text
 │       │
 │       ▼
 │   Store in MySQL
 │
 └── Search Document
         │
         ▼
     Query Database
         │
         ▼
      Show Results
```

---

## Technologies Used

* Python
* MySQL
* SQL
* PyPDF2
* Object-Oriented Programming (OOP)
* File Handling
* Database Design

---

## Database Schema

```sql
CREATE TABLE documents(
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_name VARCHAR(255),
    paragraph TEXT
);
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd PDF_Qus_Ans_Sys
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure MySQL

Create a database:

```sql
CREATE DATABASE pdf_search;
```

Create the documents table:

```sql
CREATE TABLE documents(
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_name VARCHAR(255),
    paragraph TEXT
);
```

Update database credentials inside:

```python
database.py
```

```python
host="localhost"
user="root"
password="your_password"
database="pdf_search"
```

---

## Run the Application

```bash
python main.py
```

---

## Example Usage

```text
===== PDF SEARCH SYSTEM =====

1. Upload Document
2. Search Document
3. Exit
```

Upload a PDF document:

```text
Enter PDF Path:
C:\Users\User\Downloads\sample.pdf
```

Search stored content:

```text
Ask Question:
leave policy
```

Output:

```text
File: HR_Policy.pdf

Employees are entitled to 12 casual leaves annually.
```

---

## Current Capabilities

* Keyword-based document search
* PDF text extraction
* MySQL-based storage
* Multi-document support
* Interactive search sessions

---

## Future Enhancements

### Phase 2 - NLP Search

* TF-IDF Vectorization
* Cosine Similarity
* Document Ranking
* Semantic Search

### Phase 3 - Web Application

* Flask/FastAPI Integration
* User Authentication
* File Upload Dashboard
* Search Analytics

### Phase 4 - Generative AI

* Embedding Generation
* Vector Databases (FAISS/ChromaDB)
* Retrieval-Augmented Generation (RAG)
* Large Language Models (LLMs)
* Context-Aware Question Answering

### Phase 5 - Deployment

* Docker Containerization
* Cloud Deployment
* REST APIs
* Production Monitoring

---

## Learning Objectives

This project demonstrates:

* Python Programming
* SQL and Database Management
* File Processing
* Information Retrieval
* Modular Software Design
* Backend Development Fundamentals

It also serves as a stepping stone toward advanced AI Engineering concepts such as NLP, Vector Search, RAG, and LLM-powered applications.

---

## Author

Harsh Kumar

Aspiring AI Engineer | Python Developer | AI & Machine Learning Enthusiast
