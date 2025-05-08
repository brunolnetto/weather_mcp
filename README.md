# 🌦️ Weather-MCP

**Weather-MCP** is a FastAPI server that integrates with [FastMCP](https://github.com/fastmcp/fastmcp) and [Pydantic AI](https://github.com/pydantic/pydantic-ai) to provide real-time weather alerts and forecasts. Users can interact with the server through natural language prompts, enabling seamless access to weather information.

---

## 📋 Table of Contents

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [API Endpoints](#api-endpoints)
* [Contributing](#contributing)
* [License](#license)

---

## 🚀 Features

* Fetch active weather alerts for U.S. states.
* Retrieve detailed weather forecasts based on geographic coordinates.
* Natural language interaction powered by Pydantic AI.
* Extensible toolset via FastMCP.

---

## 🛠️ Installation


### Prerequisites

* Python 3.8 or higher
* [Node.js](https://nodejs.org/) and [npm](https://www.npmjs.com/) (required for `npx`)
* An OpenAI API key (`OPENAI_API_KEY`): To obtain an OpenAI API key, please visit the [OpenAI API Keys page](https://platform.openai.com/account/api-keys) 

Ensure you have these prerequisites in place before proceeding with the setup.

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/weather-mcp.git
   cd weather-mcp
   ```

2. **Create and activate a virtual environment:**

   ```bash
   pip install uv
   uv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   uv sync
   ```

4. Set the OpenAI API Key

To securely use OpenAI services, set the `OPENAI_API_KEY` environment variable.([DEV Community][1])

#### On Unix/Linux/macOS:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

To make this change permanent, add the above line to your shell's configuration file (e.g., `~/.bashrc`, `~/.zshrc`) and reload the shell:([Hacker News][2])

```bash
source ~/.bashrc  # or source ~/.zshrc
```

#### On Windows (Command Prompt):

```cmd
setx OPENAI_API_KEY "your-api-key-here"
```

After setting the variable, restart your Command Prompt to apply the changes.

#### On Windows (PowerShell):

```powershell
$env:OPENAI_API_KEY = "your-api-key-here"
```

5. **Start the server:**

   ```bash
   python weather_server.py
   ```

The server will be accessible at `http://localhost:8000/sse`.

---

## 💡 Usage


### Interacting via Pydantic AI

You can interact with the server using natural language prompts through Pydantic AI.([YouTube][1])

**Example:**

```python
import asyncio
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerHTTP

# Define the MCP server connection
mcp_server = MCPServerHTTP(url="http://localhost:8000/sse")

# Create the Pydantic AI agent
agent = Agent(
    model="openai:gpt-4o-mini",
    mcp_servers=[mcp_server],
    system_prompt="You are a helpful assistant that provides weather information."
)

async def main():
    prompt = "Are there any weather alerts for California?"
    async with agent.run_mcp_servers():
        result = await agent.run(prompt)
        print(result.output)

if __name__ == "__main__":
    asyncio.run(main())
```

### Direct Tool Invocation

Alternatively, you can directly invoke the tools using FastMCP's client.

**Example:**

```python
import asyncio
from fastmcp import Client

async def main():
    async with Client("http://localhost:8000/sse") as client:
        tools = await client.list_tools()
        print("Available tools:")
        for tool in tools:
            print(f"- {tool.name}: {tool.description}")

        # Call the get_weather_alerts tool
        state_code = "CA"
        alerts_result = await client.call_tool("get_weather_alerts", {"state": state_code})
        print(f"\nWeather alerts for {state_code}:\n{alerts_result[0].text}")

        # Call the get_weather_forecast tool
        latitude = 34.05
        longitude = -118.25
        forecast_result = await client.call_tool("get_weather_forecast", {
            "latitude": latitude,
            "longitude": longitude
        })
        print(f"\nWeather forecast for ({latitude}, {longitude}):\n{forecast_result[0].text}")

if __name__ == "__main__":
    asyncio.run(main())
```



---

## 📡 API Endpoints

The server exposes the following tools via the MCP protocol:

* **`get_weather_alerts(state: str) -> str`**
  Fetches active weather alerts for the specified U.S. state.

* **`get_weather_forecast(latitude: float, longitude: float) -> str`**
  Retrieves the weather forecast for the given geographic coordinates.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.([GitHub][2])

For major changes, please open an issue first to discuss what you would like to change.([Make a README][3])

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

