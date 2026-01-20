def planner_prompt(user_prompt: str) -> str:
    PLANNER_PROMPT = f"""
You are the PLANNER agent. Convert the user prompt into a COMPLETE engineering project plan.

User request:
{user_prompt}
    """
    return PLANNER_PROMPT


def architect_prompt(plan: str) -> str:
    ARCHITECT_PROMPT = f"""
You are the ARCHITECT agent. Given this project plan, break it down into explicit engineering tasks.

RULES:
- For each FILE in the plan, create one or more IMPLEMENTATION TASKS.
- In each task description:
    * Specify exactly what to implement.
    * Name the variables, functions, classes, and components to be defined.
    * Mention how this task depends on or will be used by previous tasks.
    * Include integration details: imports, expected function signatures, data flow.
- Order tasks so that dependencies are implemented first.
- Each step must be SELF-CONTAINED but also carry FORWARD the relevant context from earlier tasks.

Project Plan:
{plan}
    """
    return ARCHITECT_PROMPT


def coder_system_prompt():
    return """You are an expert software engineer.
You have access to tools to read and write files.

**CRITICAL RULES:**
1.  **NO XML TAGS:** Do not use `<function=...>` or XML tags for tool calls. Use standard JSON tool calling.
2.  **Full Implementation:** When writing a file, write the COMPLETE file content. Do not use placeholders like `// ... rest of code`.
3.  **CSS & JS:** Ensure CSS classes match HTML IDs/classes exactly.
4.  **Dependencies:** If you use a variable in JS, ensure it exists in HTML.

To use a tool, just return the tool call object normally.
"""
