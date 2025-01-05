# ReX - AI Chat Assistant

ReX is an interactive chat interface built with Streamlit that integrates Google's advanced language model, Gemini. This project provides an accessible and intuitive platform for exploring the capabilities of state-of-the-art AI language models.

![Gemini](https://github.com/mayankpujara/Gemini_Explorer/assets/76840933/039bc69c-dc50-478b-9e38-a4ace0252555)

## Key Features

- 💬 Interactive chat interface built with Streamlit
- 🤖 Powered by Google's Gemini Pro language model
- 🎯 Context-aware and accurate responses
- ⚡ Real-time conversation processing
- 🔧 Customizable and extensible architecture

## Installation Requirements

- Python 3.11 or higher
- Google Cloud Account
- Required packages:
  - streamlit
  - vertexai

## Setup Instructions

### 1. Enable Google Cloud

1. Visit [Google Cloud Platform](https://cloud.google.com/)
2. Create a new project
3. Enable Vertex AI APIs
4. Set up billing information

### 2. Initialize Google Cloud

```bash
# Install Google Cloud SDK
gcloud init

# Install required packages
pip install vertexai
pip install streamlit
```

### 3. Configure the Project

```python
import vertexai
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel

# Initialize Vertex AI
project = "your-project-ID"
vertexai.init(project=project)

# Configure model
config = generative_models.GenerationConfig()
model = GenerativeModel("gemini-pro", generation_config=config)
```

### 4. Launch the Application

```bash
streamlit run rex_chat.py
```

## Common Issues & Solutions

1. **Permission Denied (403)**
   - Ensure you're using project ID instead of project name
   - Verify service account activation

2. **DNS Resolution Error**
   ```python
   import os
   os.environ['GRPC_DNS_RESOLVER'] = 'native'
   ```

## Project Structure

```
ReX/
├── rex_chat.py        # Main application file
├── requirements.txt   # Dependencies
├── README.md         # Documentation
└── .gitignore       # Git ignore file
```

## Acknowledgements

- Built with Google's Gemini Pro LLM
- Interface powered by Streamlit
- Special thanks to the open-source community

## About

ReX is designed to showcase the practical applications of large language models in a user-friendly environment. Whether you're a developer looking to integrate AI into your applications or an enthusiast wanting to explore AI capabilities, ReX provides a robust platform for AI interactions.

## Contact

For questions, suggestions, or issues, please open a GitHub issue.
