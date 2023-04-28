from autogpt.config.ai_config import AIConfig

"""
Test cases for the AIConfig class, which handles loads the AI configuration
settings from a YAML file.
"""


def test_goals_are_always_lists_of_strings(tmp_path):
    """
    Test if the goals attribute is always a list of strings.
    """
    yaml_content = """ 
ai_goals:
- Goal 1: Make a sandwich
- Goal 2, Eat the sandwich
- Goal 3 - Go to sleep
ai_role: A hungry AI
ai_name: McFamished
"""

    config_file = tmp_path / "ai_settings.yaml"
    config_file.write_text(yaml_content)

    ai_config = AIConfig.load(config_file)

    assert len(ai_config.ai_goals) == 3
    assert ai_config.ai_goals[0] == "Goal 1: Make a sandwich"
    assert ai_config.ai_goals[1] == "Goal 2, Eat the sandwich"
    assert ai_config.ai_goals[2] == "Goal 3 - Go to sleep"
