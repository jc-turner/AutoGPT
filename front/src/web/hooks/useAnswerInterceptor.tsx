import { useEffect, useState } from "react"
import IAnswer from "../types/data/IAnswer"
import IAgent from "../types/data/IAgent"
import { useDispatch } from "react-redux"
import { addAgent, removeAgent } from "@/redux/data/dataReducer"
import useAgents from "./data/useAgents"

const AGENT_CREATED = "COMMAND = start_agent  ARGUMENTS = "
const DELETE_AGENT = "COMMAND = delete_agent  ARGUMENTS = "
const useAnswerInterceptor = () => {
  const dispatch = useDispatch()
  const { agents, agentsArray } = useAgents()

  const interceptAnswer = (data: IAnswer[]) => {
    data.forEach((answer) => {
      if (!answer.content) return
      if (answer.content.includes(AGENT_CREATED)) {
        let agentSystemReturn = answer.content.split(AGENT_CREATED)[1]
        const jsonAgent = JSON.parse(
          agentSystemReturn.replace(/'/g, '"'),
        ) as IAgent

        if (agentsArray.find((agent) => agent.name === jsonAgent.name)) return
        dispatch(addAgent(jsonAgent))
      }
      if (answer.content.includes(DELETE_AGENT)) {
        let agentSystemReturn = answer.content.split(DELETE_AGENT)[1]
        const jsonAgent = JSON.parse(
          agentSystemReturn.replace(/'/g, '"'),
        ) as IAgent

        dispatch(removeAgent(jsonAgent.name))
      }
    })
  }

  return {
    interceptAnswer,
  }
}

export default useAnswerInterceptor
