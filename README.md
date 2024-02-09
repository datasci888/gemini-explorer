# Gemini-Explorer - RadicalX
## gemini-explorer-412518
This repository implements a chatbot driven by a Vertex AI Generative Model, allowing users to interact with the model through a Streamlit interface.
Key Features:
- Utilizes a pre-trained Gemini generative model
- Enables users to input queries and receive responses
- Displays conversation history in a chat-like format
- Stores conversation history in session state for seamless experience
Requirements:
- Python 3.7+
- Vertex AI account with access to a generative model (e.g., "gemini-pro")
- Streamlit
- google-cloud-aiplatform package
Installation:
- Create a virtual environment (recommended): python3 -m venv venv
- Activate the virtual environment: source venv/bin/activate (Windows: venv\Scripts\activate)
- Install dependencies: pip install -r requirements.txt
Instructions:
- Replace "gemini-explorer-412518" with your actual project name in vertexai.init.
- Ensure authentication using gcloud auth application-default login.
- Set environment variables as needed (e.g., for Vertex AI project ID).
- Run the application: streamlit run app.py
Code Structure:
- app.py: Main script containing Streamlit layout and logic
- utils.py (optional): Helper functions for code organization (if needed)
Functionality:
- The script interacts with a Vertex AI Generative Model named "gemini-pro".
- It uses a chat session to send user queries and receive responses.
- The llm_function processes queries and displays outputs in Streamlit.
- User input and model responses are stored in session state for context.
- Session state is cleared or initialized if no previous messages exist.
Customization:
- Modify the initial_prompt to set a starting conversation.
- Enhance the user interface with more Streamlit features (e.g., buttons, sliders).
- Experiment with different generative models and configurations.
Future Enhancements:
- Implement error handling and feedback mechanisms.
- Explore user authentication and personalizations.
- Integrate with other Google Cloud services or APIs.
