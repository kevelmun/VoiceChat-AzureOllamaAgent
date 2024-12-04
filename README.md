# VoiceChat-AzureOllamaAgent

## Description

**VoiceChat-AzureOllamaAgent** is a voice chat application that integrates Azure services with the Ollama 3.2 language model. It utilizes **Azure Speech to Text** to convert voice input into text, the **Ollama 3.2** model to process and generate intelligent responses, and **Azure Text to Speech** to convert the text responses back into voice. This combination provides a seamless and natural communication experience.

## Features

- **Voice Recognition** powered by Azure Speech to Text.
- **Language Model** Ollama 3.2 for generating contextual responses.
- **Voice Synthesis** using Azure Text to Speech.
- Easy installation with `pip`.
- Ongoing development to enhance the voice chat system by updating the LLM with agents using swarm technology.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.8+** installed (I used Python=3.10.10). You can download it from [Python's official website](https://www.python.org/downloads/).
- **Ollama** installed on your system. Follow the [official installation guide](https://ollama.com/).
- An **Azure account** with access to **Speech to Text** and **Text to Speech** services.
- **pip** for managing Python packages.

## Installation

### 1. Install Ollama

Follow the official instructions to install Ollama on your operating system:

- [Ollama Installation Guide](https://github.com/ollama/ollama/blob/main/README.md#quickstart)

### 2. Download the Ollama 3.2 Model

After installing Ollama, download the specific model required for this project:

```bash
ollama pull ollama3.2
```

### 3. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/kevelmun/VoiceChat-AzureOllamaAgent.git
cd VoiceChat-AzureOllamaAgent
```

### 4. Install Dependencies

Install the necessary dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 5. Configure Azure Credentials

Create a `.env` file in the root directory of the project and add your Azure credentials:

```env
AZURE_SPEECH_KEY=your_azure_speech_key
AZURE_SPEECH_REGION=your_azure_region
```

Make sure to replace `your_azure_speech_key` and `your_azure_region` with your actual Azure credentials.

## Usage

To start the voice chat, run the following command:

```bash
python main.py
```

Once executed, you can interact with the voice chat system. The workflow is as follows:

1. **Speak into the microphone**: Your voice is converted to text using Azure Speech to Text.
2. **Model Processing**: The text is sent to the Ollama 3.2 model to generate a response.
3. **Voice Response**: The generated text response is converted back to voice using Azure Text to Speech.

## Ongoing Improvements

We are currently working on enhancing the voice chat system by updating the language model (LLM) with agents using **swarm** technology. These improvements aim to increase the system's efficiency and responsiveness, providing an even more natural and fluid user experience.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. **Fork** the repository.
2. Create a new branch for your feature (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please contact [3lihan.m.c@gmail.com](mailto:3lihan.m.c@gmail.com).

---

Thank you for using **VoiceChat-AzureOllamaAgent**! We hope this tool proves to be highly useful for your needs.