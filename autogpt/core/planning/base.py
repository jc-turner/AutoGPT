import abc

from autogpt.core.configuration import SystemConfiguration
from autogpt.core.planning.schema import (
    LanguageModelClassification,
    LanguageModelPrompt,
)

# class Planner(abc.ABC):
#     """Manages the agents's planning and goal-setting by constructing language model prompts."""
#
#     @staticmethod
#     @abc.abstractmethod
#     async def decide_name_and_goals(
#         user_objective: str,
#     ) -> LanguageModelResponse:
#         """Decide the name and goals of an Agent from a user-defined objective.
#
#         Args:
#             user_objective: The user-defined objective for the agents.
#
#         Returns:
#             The agents name and goals as a response from the language model.
#
#         """
#         ...
#
#     @abc.abstractmethod
#     async def plan(self, context: PlanningContext) -> LanguageModelResponse:
#         """Plan the next ability for the Agent.
#
#         Args:
#             context: A context object containing information about the agents's
#                        progress, result, memories, and feedback.
#
#
#         Returns:
#             The next ability the agents should take along with thoughts and reasoning.
#
#         """
#         ...
#
#     @abc.abstractmethod
#     def reflect(
#         self,
#         context: ReflectionContext,
#     ) -> LanguageModelResponse:
#         """Reflect on a planned ability and provide self-criticism.
#
#
#         Args:
#             context: A context object containing information about the agents's
#                        reasoning, plan, thoughts, and criticism.
#
#         Returns:
#             Self-criticism about the agents's plan.
#
#         """
#         ...


class PromptStrategy(abc.ABC):
    default_configuration: SystemConfiguration

    @property
    @abc.abstractmethod
    def model_classification(self) -> LanguageModelClassification:
        ...

    @abc.abstractmethod
    def build_prompt(self, *_, **kwargs) -> LanguageModelPrompt:
        ...

    @abc.abstractmethod
    def parse_response_content(self, response_content: dict) -> dict:
        ...
