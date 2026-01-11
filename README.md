<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Build a RAG API with FastAPI

**Project Link:** [View Project](http://learn.nextwork.org/projects/ai-devops-api)

**Author:** Victor Cipriano  
**Email:** vcipriano@fi.uba.ar

---

![Image](http://learn.nextwork.org/motivated_amber_fierce_fox/uploads/ai-devops-api_g3h4i5j6)

---

## Introducing Today's Project!

In this project, I will demonstrate how to build RAG API from scratch. I'm doing this project to learn about RAG (Retrieval-Augmented Generation) works and how to integrate its usage with a web API.

### Key services and concepts

Key concepts I learnt include web API, frameworks, RAG, embeddings and LLM.

### Challenges and wins

This project took me approximately 2 hours. The most challenging part was to understand how to integrate Chroma and Ollama to FastAPI It was most rewarding to check the LLM used the given context to generate a "more" accurante answer.

### Why I did this project

I did this project because I wanted to know how to integrate a LLM to a web API.

---

## Setting Up Python and Ollama

In this step, I'm setting up Python and Ollama. Python is the programming language we're about to use. Ollama is a tool to run AI models. I need these tools because it gives an easy path to develop a web API and to get the integration with an LLM to manage responses.

### Python and Ollama setup

![Image](http://learn.nextwork.org/motivated_amber_fierce_fox/uploads/ai-devops-api_i9j0k1l2)

### Verifying Python is working

### Ollama and tinyllama ready

Ollama is a tool to run AI models. I downloaded the tinyllama model because I needed a lightweight model who can also be good enough in expected performance. The model will help my RAG API by using the context to generate a response to the request made by the user.

---

## Setting Up a Python Workspace

In this step, I'm setting up a Python Virtual Environment. I need it because it's an easy way to setup a Python Environment (files/dependencies) without getting conflicts between system package versions previously installed. Also is easier to eliminate it when you don't need it anymore.

### Python workspace setup

### Virtual environment

A virtual environment is an isolated Python environment that keeps your project's dependencies separate from other Python projects on your computer. I created one for this project to make sure anything I install or run with Python only affects this project. Once I activate it using the command "source ./venv/bin/activate". To create a virtual environment, I run the command "python3 -m venv venv"

### Dependencies

The packages I installed are FastAPI, Chroma, Uvicorn and Ollama. FastAPI is used as a web framework that helps us build APIs quickly. Chroma is used as a vector database that stores document embeddings (numerical representations of text). Uvicorn is used for running our FastAPI app and make it accessible locally on your computer. Ollama library is used to let the code talk to Ollama, giving the API a way to send questions to tinyllama and get responses programmatically.

![Image](http://learn.nextwork.org/motivated_amber_fierce_fox/uploads/ai-devops-api_u1v2w3x4)

---

## Setting Up a Knowledge Base

In this step, I'm creating a knowledge base. A knowledge base is a set of documents used to give the LLM a context to generate an answer to the request made by the user. I need it because a RAG API needs to "Retrieve" some base data to build this context for the answer.

### Knowledge base setup

![Image](http://learn.nextwork.org/motivated_amber_fierce_fox/uploads/ai-devops-api_t1u2v3w4)

### Embeddings created

Embeddings are a numerical representation for text and documents that capture meaning. I created them to search embeddings semantically, and not just by matching keywords, but by finding text with similar meaning. The db/ folder contains your knowledge base's embeddings so Chroma can quickly search through them when your API is running. This is important for RAG because Chroma converts your question into an embedding, searches for the most similar embeddings in its database, and returns the matching text. 

---

## Building the RAG API

In this step, I'm building a RAG API. An API is a way for different software systems or applications to communicate and share data with each other. FastAPI is a web framework for building APIs. I'm creating this because we're building a web API that can answer questions using AI powered by your own knowledge base. And FastAPI is designed to be fast, easy to use, and automatically generates interactive documentation. 

### FastAPI setup

### How the RAG API works

My RAG API works by: given a received request in the question endpoint, the app searchs throught the knowledge base using Chroma to find text that matches the question's meaning, returns the most relevant information from your documents (context) and the question and the context are sent together to tinyllama to generate an answer to send back to the one who asked.

![Image](http://learn.nextwork.org/motivated_amber_fierce_fox/uploads/ai-devops-api_f3g4h5i6)

---

## Testing the RAG API

In this step, I'm testing my RAG API. I'll test it using the command line. I'll use it to try how the API works and to check if it behaves as expected.

### Testing the API

### API query breakdown

I queried my API by running the command "curl -X POST "http://127.0.0.1:8000/query" -G --data-urlencode "q=What is Kubernetes?"". The command uses the POST method, which is an HTTP method used to send data to a server. The API responded with an answer generated by tinyllama using the context from the knowledge base and the question made (especifically, it answered ""Response: Yes, I can clarify that \"Kubernezes\" is the name of Kubernetes, a container orchestration platform used to manage containers at scale."")

![Image](http://learn.nextwork.org/motivated_amber_fierce_fox/uploads/ai-devops-api_g3h4i5j6)

### Swagger UI exploration

Swagger UI is a documentation page for your FastAPI server. I used it to explore the API's endpoints, see what parameters they accept, and even try them out right from the browser. The best part about using Swagger UI was that it is automatically generated and interactive. 



---

## Adding Dynamic Content

In this project extension, I'm adding an endpoint to dynamically extend the program's knowledge base.

### Adding the /add endpoint

![Image](http://learn.nextwork.org/motivated_amber_fierce_fox/uploads/ai-devops-api_w9x0y1z2)

### Dynamic content endpoint working

The /add endpoint allows me to build a dynamic knowledge base. This is useful because it allows to accept new content through an API, store it automatically in Chroma and make it searchable immediately without manual file editing or server restarts.

---

---
