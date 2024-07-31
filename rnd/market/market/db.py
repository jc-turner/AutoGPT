import prisma.models
import prisma.types
from prisma.errors import PrismaError
from fuzzywuzzy import fuzz


class AgentQueryError(Exception):
    """Custom exception for agent query errors"""

    pass


async def get_agents(
    page: int = 1,
    page_size: int = 10,
    name: str | None = None,
    keyword: str | None = None,
    category: str | None = None,
    description: str | None = None,
    description_threshold: int = 60,
    sort_by: str = "createdAt",
    sort_order: str = "desc",
):
    """
    Retrieve a list of agents from the database based on the provided filters and pagination parameters.

    Args:
        page (int, optional): The page number to retrieve. Defaults to 1.
        page_size (int, optional): The number of agents per page. Defaults to 10.
        name (str, optional): Filter agents by name. Defaults to None.
        keyword (str, optional): Filter agents by keyword. Defaults to None.
        category (str, optional): Filter agents by category. Defaults to None.
        description (str, optional): Filter agents by description. Defaults to None.
        description_threshold (int, optional): The minimum fuzzy search threshold for the description. Defaults to 60.
        sort_by (str, optional): The field to sort the agents by. Defaults to "createdAt".
        sort_order (str, optional): The sort order ("asc" or "desc"). Defaults to "desc".

    Returns:
        dict: A dictionary containing the list of agents, total count, current page number, page size, and total number of pages.
    """
    try:
        # Define the base query
        query = {}

        # Add optional filters
        if name:
            query["name"] = {"contains": name, "mode": "insensitive"}
        if keyword:
            query["keywords"] = {"has": keyword}
        if category:
            query["categories"] = {"has": category}

        # Define sorting
        order = {sort_by: sort_order}

        # Calculate pagination
        skip = (page - 1) * page_size

        # Execute the query
        try:
            agents = await prisma.models.Agents.prisma().find_many(
                where=query,  # type: ignore
                order=order,  # type: ignore
                skip=skip,
                take=page_size,
            )
        except PrismaError as e:
            raise AgentQueryError(f"Database query failed: {str(e)}")

        # Apply fuzzy search on description if provided
        if description:
            try:
                filtered_agents = []
                for agent in agents:
                    if (
                        agent.description
                        and fuzz.partial_ratio(
                            description.lower(), agent.description.lower()
                        )
                        >= description_threshold
                    ):
                        filtered_agents.append(agent)
                agents = filtered_agents
            except AttributeError as e:
                raise AgentQueryError(f"Error during fuzzy search: {str(e)}")

        # Get total count for pagination info
        total_count = len(agents)

        return {
            "agents": agents,
            "total_count": total_count,
            "page": page,
            "page_size": page_size,
            "total_pages": (total_count + page_size - 1) // page_size,
        }

    except AgentQueryError as e:
        # Log the error or handle it as needed
        raise e
    except ValueError as e:
        raise AgentQueryError(f"Invalid input parameter: {str(e)}")
    except Exception as e:
        # Catch any other unexpected exceptions
        raise AgentQueryError(f"Unexpected error occurred: {str(e)}")


async def get_agent_details(agent_id: str, version: int | None = None):
    """
    Retrieve agent details from the database.

    Args:
        agent_id (str): The ID of the agent.
        version (int | None, optional): The version of the agent. Defaults to None.

    Returns:
        dict: The agent details.

    Raises:
        AgentQueryError: If the agent is not found or if there is an error querying the database.
    """
    try:
        query = {"id": agent_id}
        if version is not None:
            query["version"] = version  # type: ignore

        agent = await prisma.models.Agents.prisma().find_first(where=query)  # type: ignore

        if not agent:
            raise AgentQueryError("Agent not found")

        return agent

    except PrismaError as e:
        raise AgentQueryError(f"Database query failed: {str(e)}")
    except Exception as e:
        raise AgentQueryError(f"Unexpected error occurred: {str(e)}")