# LangChain Models

A collection of examples demonstrating how to work with different Large Language Models (LLMs), Chat Models, and Embedding Models using LangChain.

## Project Structure

```text
Langchain_models/
│
├── ChatModels/          # Examples of LangChain Chat Models
├── EmbeddedModels/      # Examples of Embedding Models
├── LLMs/                # Examples of LLM integrations
├── test.py              # Testing script
├── requirements.txt     # Project dependencies
├── .gitignore
└── README.md
```

## Features

* Integration with multiple LLM providers
* Chat model examples
* Embedding model examples
* Environment variable management using `.env`
* Easy-to-understand sample code
* Beginner-friendly LangChain demonstrations

## Prerequisites

* Python 3.10+
* Git
* API Keys for the models you want to use

## Installation

Clone the repository:

```bash
git clone https://github.com/as578820/Langchain_models.git
cd Langchain_models
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root and add your API keys:

```env
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

> Never commit your `.env` file to GitHub.

## Usage

Run any example script:

```bash
python test.py
```

Or execute scripts from the individual folders:

```bash
python LLMs/example.py
python ChatModels/example.py
python EmbeddedModels/example.py
```

## Models Covered

### LLMs

* Groq
* Google Gemini
* Hugging Face
* Other LangChain-supported LLMs

### Chat Models

* ChatGroq
* ChatGoogleGenerativeAI
* ChatHuggingFace
* Additional chat integrations

### Embedding Models

* Hugging Face Embeddings
* Gemini Embeddings
* Other vector embedding models

## Learning Objectives

This repository helps developers learn:

* LangChain fundamentals
* LLM integration
* Chat model usage
* Embedding generation
* Environment variable management
* Building AI-powered applications

## Contributing

Contributions are welcome. Feel free to submit pull requests or open issues for improvements.

## License

This project is intended for learning and educational purposes.

```
```
