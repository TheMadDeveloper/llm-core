# LLM Core

## Project Summary
**LLM Core** is a modular, flexible LLM boilerplate chatbot framework built in Python. Initially, the project leverages a cloud-based LLM (e.g., OpenAI API) for quick prototyping and easy setup, with plans to transition to a local model (such as LLaMA or GPT-J) in the future. The focus is on simplicity, clean structure, and extensibility, making it a strong foundation for future LLM-based applications.

## Key Goals
- **Simple Terminal Chatbot Interface:**  
  Create a minimal, terminal-based chatbot to interact with the LLM.
- **Cloud-Hosted LLM Integration:**  
  Start with a cloud-hosted LLM API (like OpenAI) for rapid development.
- **Modular Architecture:**  
  Build the project in a way that supports swapping LLM backends, adding configuration, and extending functionality easily.
- **Future Local Model Support:**  
  Prepare for a smooth transition to a local model to optimize performance and reduce API dependency.

## Project Plan

### Phase 1 – Cloud-Based MVP
- **API Integration:**  
  Connect to a cloud-hosted LLM (e.g., OpenAI API).
- **Terminal Chat Loop:**  
  Build a basic terminal interface for user input and LLM responses.
- **Message History:**  
  Implement a simple history tracker to manage context between messages.

### Phase 2 – Config & Extensibility
- **Configuration Management:**  
  Add a configuration file to set parameters such as model, temperature, and token limits.
- **Multi-LLM Support:**  
  Enable the framework to support multiple LLM backends.
- **Logging & Debugging:**  
  Integrate logging and debugging options for easier development and troubleshooting.

### Phase 3 – Local Model Support
- **Model Swap:**  
  Replace the cloud-based LLM with a local model using the same interface.
- **Performance Optimization:**  
  Optimize the framework to run efficiently on development hardware (e.g., 2024 MacBook Pro with M3 Pro chip).

### Phase 4 (Optional) – Advanced Features
- **Extended Memory:**  
  Add persistent memory beyond the session for improved context.
- **API Exposure:**  
  Develop a lightweight API to allow external integrations.
- **Enhanced Interfaces:**  
  Explore fine-tuning options and a potential GUI front-end for broader usability.