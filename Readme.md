
# Password Strength Analyzer

An advanced password strength analyzer that provides real-time feedback as users type their passwords. Built with FastAPI, WebSockets, and Python, this tool helps identify weak passwords and suggests improvements. Ideal for integration into web applications requiring secure password practices.

## Features
- **Real-Time Feedback**: Instantly assess the strength of a password as it's being typed.
- **Common Password Detection**: Checks against a large list of common passwords to ensure security.
- **Entropy Calculation**: Analyzes the entropy of the password to determine its strength.
- **Modern UI**: A responsive, modern interface with a progress bar and password visibility toggle.
- **Secure and Scalable**: Designed with security and scalability in mind, utilizing Docker for deployment.

## Setup and Installation

### Prerequisites
- Docker
- Python 3.11

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Muhammad-H-Arif/password-strength-analyzer.git
    cd password-strength-analyzer
    ```

2. Build and run the application using Docker:
    ```bash
    docker-compose up --build
    ```

3. Access the application in your browser at `http://localhost:8000`.

## Usage
- Open the application in a web browser.
- Type a password into the input field to receive real-time feedback on its strength.

## Development
### Running Locally without Docker
If you prefer to run the application locally without Docker:
1. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the FastAPI application:
    ```bash
    uvicorn app.main:app --reload
    ```

4. Access the application at `http://localhost:8000`.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

