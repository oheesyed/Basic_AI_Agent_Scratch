# AI Agent Project

This project is an AI agent with access to a toolbox of various tools. The agent can determine which tool is best suited to answer a user query and generate a response.

Credit to @john-adeojo for the original codebase.
https://github.com/john-adeojo/use-tools


## Features

- Basic Calculator
- String Reverser
- Joke Generator

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/oheesyed/basic-ai-agent-scratch.git
   cd your-repo-name
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   export OPENAI_API_KEY='your_openai_api_key'
   ```

## Usage

From main directory, run the agent in your terminal: 
```bash
python -m agents.agent
``` 
