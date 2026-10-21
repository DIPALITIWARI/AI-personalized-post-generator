# AI-Powered LinkedIn Post Generator 🤖

An AI-powered LinkedIn Post Generator that creates personalized LinkedIn posts based on the selected topic, language, and desired length. The project uses Large Language Models (LLMs) and few-shot prompting to generate relevant and engaging content.

✨ Features

- **AI-Powered Content Generation:** Generate LinkedIn posts using an LLM.
- **Few-Shot Prompting:** Uses relevant example posts to guide the generated content.
- **Customizable Length:** Generate short, medium, or long posts.
- **Language Support:** Generate posts in English and Hinglish.
- **Topic-Based Generation:** Create posts for different topics.
- **Metadata Extraction:** Extract post metadata such as line count, language, and relevant tags.
- **JSON Data Processing:** Load and process LinkedIn posts stored in JSON files.

 🛠️ Tech Stack

- Python
- LangChain
- Groq API
- Pandas
- JSON
- python-dotenv

📁 Project Structure

```text
Linkedin/
├── data/
│   ├── raw_data.json
│   └── processed_data.json
├── llm_helper.py
├── few_shot.py
├── post_generator.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

*Note: Update the filenames in this structure to match your actual project files.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd Linkedin
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**macOS/Linux**
```bash
source .venv/bin/activate
```

**Windows**
```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get an API key from [Groq Console](https://console.groq.com/).

**Important:** Never upload your actual `.env` file or API key to GitHub.

### 5. Prepare the dataset

Place your LinkedIn post dataset in the `data/` directory. Ensure that the JSON file paths used in your Python code match the actual filenames.

### 6. Run the project

Run the Python file containing your post-generation logic:

```bash
python post_generator.py
```

Replace `post_generator.py` with your actual entry-point filename if different.

## 💡 How It Works

1. LinkedIn post data is loaded from JSON files.
2. Post metadata is extracted using an LLM.
3. Processed posts are loaded into a Pandas DataFrame.
4. Relevant few-shot examples are selected based on the requested parameters.
5. A prompt is constructed using the topic, language, desired length, and example posts.
6. The LLM generates a new LinkedIn post.

## 🔮 Future Improvements

- Personalized writing styles based on user preferences.
- Semantic search using embeddings and vector databases.
- Multiple post variations and tone selection.
- Engagement analytics and performance prediction.
- A web interface using Streamlit or React.
- User feedback and saved-post functionality.
- Deployment as a web application.

 🔐 Security

- Store API keys in environment variables.
- Keep `.env` out of version control.
- Never publish private or sensitive user data in the dataset.

👩‍💻 Author

Dipali Tiwari

B.Tech Computer Science Engineering

---

If you find this project interesting, consider giving the repository a ⭐ on GitHub!