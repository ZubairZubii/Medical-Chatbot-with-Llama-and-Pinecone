Here is a well-structured **README** for your project:

---

# 🩺 **Medical Chatbot with Llama and Pinecone** 🤖

This project is a **medical chatbot** that leverages **Langchain**, **HuggingFace embeddings**, and **Pinecone** for vector storage. It uses a **Llama model** to handle medical-related questions and provide detailed answers. You can interact with this chatbot via a web interface, and the bot can retrieve information about medical conditions, treatments, and more.

---

## 🌟 **Key Features**

- 🧠 **AI-Powered**: Uses **Llama-2-7b** model for answering complex medical-related queries.
- 📚 **Semantic Search**: Powered by **Pinecone** for fast and accurate vector searches based on semantic similarity.
- 🌍 **HuggingFace Embeddings**: Implements **all-MiniLM-L6-v2** model for creating embeddings that improve the accuracy of search results.
- 🎨 **Web Interface**: Simple, easy-to-use web interface built with **Flask**.
- 🔄 **Real-time Responses**: Chatbot provides near-instant responses to both simple greetings and complex medical queries.

---

## 🎥 **Watch the Demo Video**

Check out the demo video of the Medical Chatbot in action:

[![Watch the Demo](https://img.youtube.com/vi/6f0fdf913b0/0.jpg)](https://www.loom.com/share/06f0fdf913b048f2859b459a35d0e411?sid=5afa2638-014b-455a-a1e0-aea94a342433)

---

## 🚀 **Live Demo**

👉 **[Try it Now!](#)** *(Replace with actual URL once deployed)*

---

## 🛠️ **Tech Stack**

- **Backend**: Flask
- **AI Model**: Llama-2-7b (CTransformers)
- **Vector Storage**: Pinecone (for efficient search)
- **Embeddings**: HuggingFace (all-MiniLM-L6-v2)
- **Frontend**: HTML/CSS (Flask templates)

---

## ⚙️ **Setup and Installation**

### 1. **Clone the Repository**

```bash
git clone https://github.com/Medical Chatbot with Llama and Pinecone/medical-chatbot.git
cd medical-chatbot
```

### 2. **Install Required Dependencies**

Make sure you have `pip` installed, then install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. **Set up Environment Variables**

Create a `.env` file in the root directory and add the following keys:

```bash
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_API_ENV=your_pinecone_environment
```

### 4. **Download the HuggingFace Embeddings Model**

You can download the HuggingFace embeddings by running the following Python command:

```bash
python -c "from src.helper import download_hugging_face_embeddings; download_hugging_face_embeddings()"
```

### 5. **Run the Application**

Start the Flask server locally:

```bash
python app.py
```

Visit `http://localhost:8080` in your browser to start chatting with the medical bot.

---

## 🧠 **How It Works**

1. **Embedding Search**: The input query is converted into embeddings using **HuggingFace**'s `all-MiniLM-L6-v2` model.
2. **Pinecone Search**: The embeddings are used to perform a vector search in **Pinecone** to retrieve the most relevant medical information.
3. **Llama-2-7b Model**: The retrieved information is processed by the **Llama-2-7b** model to generate an appropriate answer.
4. **Response**: The chatbot returns a coherent response based on the input query and retrieved information.

---

## 🔄 **Endpoints**

- **GET /**: Renders the chat interface.
- **POST /get**: Handles user input and returns the chatbot's response.

---

## 📂 **Project Structure**

```bash
medical-chatbot/
├── app.py              # Flask application logic
├── src/
│   ├── helper.py       # Helper functions for HuggingFace model downloads
│   ├── prompt.py       # Custom prompts for the chatbot
├── templates/
│   └── chat.html       # HTML template for chat interface
├── static/             # Static assets (CSS, images, etc.)
├── .env                # Environment variables
└── requirements.txt    # Python dependencies
```

---

## 🧪 **Example Queries**

Here are some examples of how to interact with the chatbot:

- **Greeting**: "Hi"
- **Medical Query**: "What are the symptoms of diabetes?"
- **Condition Information**: "Tell me about hypertension treatments."

---

## 🤝 **Contributions**

Contributions are welcome! Feel free to:

1. **Fork the Repository** 🍴.
2. **Create a Feature Branch**: `git checkout -b feature/new-feature`.
3. **Commit Your Changes**: `git commit -m 'Add new feature'`.
4. **Push to the Branch**: `git push origin feature/new-feature`.
5. **Open a Pull Request**: 🔄.

---

## 📫 **Contact**

- **GitHub**: [Zubair Ali](https://github.com/ZubairZubii)
- **Email**: zs970120@gmail.com

---

## 🌍 **License**

This project is licensed under the **MIT License**.

---

### 🚀 Powered by: Llama, HuggingFace, and Pinecone 🚀

---

