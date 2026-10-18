from dataclasses import dataclass, asdict
import json
import time

# 1. DATACLASSES: The modern alternative to standard classes for state management
@dataclass
class AgentProfile:
    agent_name: str
    model_engine: str
    temperature: float
    # We can assign default values easily
    max_retries: int = 3
    is_active: bool = True

print("--- INITIALIZING AGENT ---")
# Instantiate our agent profile
primary_agent = AgentProfile(
    agent_name="DataBot_v1",
    model_engine="gpt-4-turbo",
    temperature=0.2
)

print(f"Agent '{primary_agent.agent_name}' initialized on {primary_agent.model_engine}.")

# 2. CONTEXT MANAGERS & JSON EXPORT
config_filename = "agent_config.json"

print("\n--- SAVING CONFIGURATION ---")
# The 'with' statement acts as a Context Manager, automatically closing the file when done.

with open(config_filename, "w") as file:
    # We convert the Dataclass back to a dictionary (asdict), then to a JSON string (json.dump)
    json.dump(asdict(primary_agent), file, indent=4)

print(f"Configuration securely saved to {config_filename}.")
