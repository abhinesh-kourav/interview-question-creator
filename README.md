# Interview Question Creator

An AI-powered tool that generates coding interview questions based on user preferences, leveraging the Llama 3 model through Ollama.

## Description

This application helps interviewers and hiring managers create tailored coding questions for technical interviews. Simply upload a pdf document from which the questions are needed, and the tool will generate appropriate interview questions.

## Prerequisites

Before running this application, make sure you have the following installed:

1. **Ollama**
   - Visit [Ollama's official website](https://ollama.com/download) to download and install
   - After installation, download the Llama 3 model:
     ```
     ollama run llama3
     ```

2. **Python 3.10**
   - Create a  Python 3.10 virual environment from [python.org](https://www.python.org/downloads/)

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/abhinesh-kourav/interview-question-creator.git
   cd interview-question-creator
   ```

2. **Create a virtual environment**
   ```bash
   conda create -n interview python=3.10 -y
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```
     conda activate interview
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Ollama server**
   - Ensure the Ollama service is running on your machine

2. **Run the application**
   ```bash
   uvicorn app:app
   ```

3. **Access the web interface**
   - Open your browser and navigate to `http://localhost:8000`

## Usage

1. Upload the pdf related to which you want interview questions and answers.
2. Click "Generate Q&A" button to create interview questions and their answers.
3. The generated output in the csv format will include:
   - Generated 5-10 interview questions
   - Ideal answer to the corresponsing question

## Acknowledgments

- Thanks to the Ollama team for providing an easy way to run Llama 3 locally

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/abhinesh-kourav/interview-question-creator/issues) on GitHub.
