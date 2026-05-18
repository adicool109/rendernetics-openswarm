from pathlib import Path

from agency_swarm import Agent, ModelSettings
from agency_swarm.tools import IPythonInterpreter, LoadFileAttachment, WebSearchTool
from openai.types.shared.reasoning import Reasoning
from shared_tools import CopyFile, ExecuteTool, FindTools, ManageConnections, SearchTools

from config import get_default_model, is_openai_provider

_INSTRUCTIONS_PATH = Path(__file__).parent / "instructions.md"


def _build_instructions() -> str:
    return _INSTRUCTIONS_PATH.read_text(encoding="utf-8")


def create_marketing_agent() -> Agent:
    return Agent(
        name="Marketing Agent",
        description=(
            "Campaign strategist for end-to-end marketing plans, social media management, "
            "and content generation."
        ),
        instructions=_build_instructions(),
        files_folder="./files",
        tools_folder="./tools",
        tools=[
            WebSearchTool(),
            IPythonInterpreter,
            LoadFileAttachment,
            CopyFile,
            ExecuteTool,
            FindTools,
            ManageConnections,
            SearchTools,
        ],
        model=get_default_model(),
        model_settings=ModelSettings(
            reasoning=Reasoning(effort="medium", summary="auto") if is_openai_provider() else None,
            truncation="auto",
            response_include=["web_search_call.action.sources"] if is_openai_provider() else None,
        ),
        conversation_starters=[
            "Build a launch campaign for a new SaaS product.",
            "Create a one-month social media plan for our brand.",
            "Turn these product insights into a marketing strategy and content plan.",
            "Draft a data-driven campaign brief with channels, KPIs, and messaging.",
        ],
    )
