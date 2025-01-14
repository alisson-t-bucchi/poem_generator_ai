# 🤖 AI Poem Generator

This project is an AI-based poem generator built with [Cohere API](https://cohere.ai/) and [Streamlit](https://streamlit.io/). 

It allows users to create personalized poems based on a theme and the desired number of lines.

## 📝 Features

- Generate custom poems based on a provided theme.
- Specify the number of lines in the poem.
- Interactive user interface built with Streamlit.

## 🚀 How to Run

### Prerequisites

Ensure you have the following dependencies installed:

- Python 3.8 or higher
- Python libraries:
  - `cohere`
  - `streamlit`

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/ai-poem-generator.git
   cd ai-poem-generator
   ```
   
2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a config.py file in the root directory and add Cohere API key: 

    ```python
   API_KEY = "your_cohere_api_key"
    ```

### Running the Application

1. Start the Streamlit app:

    ```bash
    streamlit run <filename>.py
    ```
   
2. Open the generated link in your terminal (usually http://localhost:8501) in a web browser.

### ⚙️ How to Use

1. Enter the desired number of lines for your poem.
2. Enter a theme for your poem (e.g., love, nature, dreams).
3. The generated poem will be displayed on the screen.

### 🛠 Technologies Used

- Cohere API: For AI text generation.
- Streamlit: For building the user interface.
- Python: The main programming language used in development.

### ⚠️ Error Handling
If the Cohere API returns an error, the program will display error messages in the console for debugging purposes.

### 📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.

💡 Developed with ❤️ and AI by Alisson Bucchi. 