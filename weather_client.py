import asyncio
from fastmcp import Client

async def main():
    # Connect to the MCP server via SSE
    async with Client("http://localhost:8000/sse") as client:
        # List available tools
        tools = await client.list_tools()
        print("Available tools:")
        for tool in tools:
            print(f"- {tool.name}: {tool.description}")

        # Call the get_weather_alerts tool
        state_code = "CA"
        alerts_result = await client.call_tool("get_weather_alerts", {"state": state_code})
        print(f"\nWeather alerts for {state_code}:\n{alerts_result[0].text}")

        # Call the get_weather_forecast tool
        latitude = 34.05   # Replace with desired latitude
        longitude = -118.25  # Replace with desired longitude
        forecast_result = await client.call_tool("get_weather_forecast", {
            "latitude": latitude,
            "longitude": longitude
        })
        print(f"\nWeather forecast for ({latitude}, {longitude}):\n{forecast_result[0].text}")

if __name__ == "__main__":
    asyncio.run(main())
