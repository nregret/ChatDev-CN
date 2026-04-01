import json
import os

EN_PATH = "d:/Project/Code/ChatDev/frontend/src/locales/en.json"
ZH_PATH = "d:/Project/Code/ChatDev/frontend/src/locales/zh.json"

with open(EN_PATH, "r", encoding="utf-8") as f:
    en_data = json.load(f)

with open(ZH_PATH, "r", encoding="utf-8") as f:
    zh_data = json.load(f)

en_help = {
  "startNode": {
    "title": "Start Node",
    "description": "The entry point for your workflow. All nodes connected to the Start node will run in parallel when the workflow launches.",
    "examples": [
      "Connect multiple nodes to start them simultaneously",
      "The first nodes to execute receive your initial input"
    ]
  },
  "workflowNode": {
    "agent": {
      "title": "Agent Node",
      "description": "An AI agent that can reason, generate content, and use tools. Agents receive messages and produce responses based on their configuration.",
      "examples": [
        "Content generation (writing, coding, analysis)",
        "Decision making and routing",
        "Tool usage (search, file operations, API calls)"
      ]
    },
    "human": {
      "title": "Human Node",
      "description": "Pauses workflow execution and waits for human input. Use this to review content, make decisions, or provide feedback.",
      "examples": [
        "Review and approve generated content",
        "Provide additional instructions or corrections",
        "Choose between workflow paths"
      ]
    },
    "python": {
      "title": "Python Node",
      "description": "Executes Python code on your local environment. The code runs in the workspace directory and can access uploaded files.",
      "examples": [
        "Data processing and analysis",
        "Running generated code",
        "File manipulation"
      ]
    },
    "passthrough": {
      "title": "Passthrough Node",
      "description": "Passes messages to the next node without modification. Useful for workflow organization and filtering outputs in loops.",
      "examples": [
        "Preserve initial context in loops",
        "Filter redundant outputs",
        "Organize workflow structure"
      ]
    },
    "literal": {
      "title": "Literal Node",
      "description": "Outputs fixed text, ignoring all input. Use this to inject instructions or context at specific points in the workflow.",
      "examples": [
        "Add fixed instructions before a node",
        "Inject context or constraints",
        "Provide test data"
      ]
    },
    "loop_counter": {
      "title": "Loop Counter Node",
      "description": "Limits loop iterations. Only produces output when the maximum count is reached, helping control infinite loops.",
      "examples": [
        "Prevent runaway loops",
        "Set maximum revision cycles",
        "Control iterative processes"
      ]
    },
    "subgraph": {
      "title": "Subgraph Node",
      "description": "Embeds another workflow as a reusable module. Enables modular design and workflow composition.",
      "examples": [
        "Reuse common patterns across workflows",
        "Break complex workflows into manageable pieces",
        "Share workflows between teams"
      ]
    },
    "unknown": {
      "title": "Workflow Node",
      "description": "A node in your workflow. Click to view and edit its configuration."
    }
  },
  "edge": {
    "basic": {
      "title": "Connection",
      "description": "Connects two nodes to control information flow and execution order. The upstream node's output becomes the downstream node's input.",
      "examples": [
        "Data flows from source to target",
        "Target executes after source completes"
      ]
    },
    "trigger": {
      "enabled": {
        "description": "This connection triggers the downstream node to execute."
      },
      "disabled": {
        "description": "This connection passes data but does NOT trigger execution. The downstream node only runs if triggered by another edge."
      }
    },
    "condition": {
      "hasCondition": {
        "description": "This connection has a condition. It only activates when the condition evaluates to true."
      }
    }
  },
  "contextMenu": {
    "createNode": {
      "description": "Create a new node in your workflow. Choose from Agent, Human, Python, and other node types."
    },
    "copyNode": {
      "description": "Duplicate this node with all its settings. The copy will have a blank ID that you must fill in."
    },
    "deleteNode": {
      "description": "Remove this node and all its connections from the workflow."
    },
    "deleteEdge": {
      "description": "Remove this connection between nodes."
    },
    "createNodeButton": {
      "description": "Open the node creation form. You can also right-click the canvas to create a node at a specific position."
    },
    "configureGraph": {
      "description": "Configure workflow-level settings like name, description, and global variables."
    },
    "launch": {
      "description": "Run your workflow with a task prompt. The workflow will execute and show you the results."
    },
    "createEdge": {
      "description": "Create a connection between nodes. You can also drag from a node's handle to create connections visually."
    },
    "manageVariables": {
      "description": "Define global variables (like API keys) that all nodes can access using ${VARIABLE_NAME} syntax."
    },
    "manageMemories": {
      "description": "Configure memory modules for long-term information storage and retrieval across workflow runs."
    },
    "renameWorkflow": {
      "description": "Change the name of this workflow file."
    },
    "copyWorkflow": {
      "description": "Create a duplicate of this entire workflow with a new name."
    }
  }
}

zh_help = {
  "startNode": {
    "title": "起始节点",
    "description": "您的工作流的入口点。当工作流启动时，所有连接到起始节点的节点将同时并行运行。",
    "examples": [
      "连接多个节点以同时启动它们",
      "首先执行的节点会接收您的初始输入内容"
    ]
  },
  "workflowNode": {
    "agent": {
      "title": "Agent 节点 (智能体)",
      "description": "一个能够推理、生成内容以及使用工具的 AI 智能体。智能体接收消息并根据其配置产出相应的响应内容。",
      "examples": [
        "内容生成 (写作、编码、分析)",
        "逻辑决策与路由分发",
        "使用外部工具 (搜索、文件操作、API 调用)"
      ]
    },
    "human": {
      "title": "Human 节点 (人工节点)",
      "description": "暂停工作流执行并等待人工输入介入。使用此节点来审查内容、做决策或提供反馈修订。",
      "examples": [
        "审查并批准 AI 生成的内容",
        "提供额外的修正指令",
        "在不同的工作流分支中做选择"
      ]
    },
    "python": {
      "title": "Python 节点",
      "description": "在您的本地环境中执行 Python 代码。代码将在工作区目录下运行，并可以访问用户上传的文件。",
      "examples": [
        "数据处理和分析清洗",
        "运行由 AI 生成的代码测试",
        "直接在本地操作文件"
      ]
    },
    "passthrough": {
      "title": "Passthrough 节点 (透传节点)",
      "description": "将接收到的消息未经任何修改的地传递给下一个节点。常用于工作流结构的整理和在循环执行中过滤无用输出。",
      "examples": [
        "在循环体内保留初始的上游上下文",
        "过滤掉多余冗余的节点输出",
        "将工作流结构的连线梳理得更整洁"
      ]
    },
    "literal": {
      "title": "Literal 节点 (常量节点)",
      "description": "直接输出固定的文本内容，忽略一切上游输入。可以用来在工作流的特定位置硬性植入指令或上下文。",
      "examples": [
        "在目标节点前强制追加固定的系统设定",
        "注入硬编码的上下文或约束条件",
        "提供模拟的测试样例数据"
      ]
    },
    "loop_counter": {
      "title": "Loop Counter 节点 (循环计数器)",
      "description": "用来限制循环的迭代次数。仅仅在达到最大的计数值时才会产生输出，这在使用 AI 时能有效防止无限死循环。",
      "examples": [
        "防止工作流陷入失控的失控循环",
        "设定最大允许的工作流修改/审查次数",
        "控制复杂的迭代处理流程"
      ]
    },
    "subgraph": {
      "title": "Subgraph 节点 (子图节点)",
      "description": "将另外一个独立的工作流文件作为可重用模块嵌入进来。有了它即可实现模块化设计与大型工作流协同组合。",
      "examples": [
        "在不同的工作流间重用常用的功能模式",
        "将巨大复杂的工作流拆分成多个方便管理的小块",
        "在不同的团队间共享固定的工作流资产"
      ]
    },
    "unknown": {
      "title": "工作流节点",
      "description": "您工作流中的一个节点。点击即可查看并编辑其相关配置属性。"
    }
  },
  "edge": {
    "basic": {
      "title": "节点连线",
      "description": "用来连接两个节点以控制信息数据流向和逻辑执行顺序。上游节点输出的结果将直接作为下游节点的输入内容。",
      "examples": [
        "数据从源节点无缝传递到目标节点",
        "等待源节点完全处理结束后目标节点再开始执行"
      ]
    },
    "trigger": {
      "enabled": {
        "description": "当前连线会触发并唤醒处于下游的节点执行。"
      },
      "disabled": {
        "description": "目前连线仅会传递数据，但不触发下游执行。这说明下游节点只能在被其它节点触发时才会运行。"
      }
    },
    "condition": {
      "hasCondition": {
        "description": "这是一个附带条件的连线。只有当满足相关条件并计算为 true 时连线上的数据流才会激活穿行。"
      }
    }
  },
  "contextMenu": {
    "createNode": {
      "description": "在您的工作流中创建一个全新的节点。可以在智能体 (Agent)、人工 (Human)、代码 (Python) 等各个节点类型中选择。"
    },
    "copyNode": {
      "description": "带着原有的全部设置完美复刻这个节点。由于是克隆产生的，所以新生成的节点需要您手动给它重置一个空白的节点 ID。"
    },
    "deleteNode": {
      "description": "从当前工作流内彻底移除该节点及其所连接的所有上下游连线。"
    },
    "deleteEdge": {
      "description": "移除这两个节点之间的连线与关系。"
    },
    "createNodeButton": {
      "description": "打开节点创建表单。您也可以在画布空白处右键点击来将节点直接创建在该对应的坐标位置上。"
    },
    "configureGraph": {
      "description": "配置整个工作流级别的全局设定，例如工作流最终名称、文字描述以及那些关键的全局变量参数。"
    },
    "launch": {
      "description": "使用任务提示词直接运行您的这个工作流。工作流将会自动执行并且即刻为您展示中间的所有思考运行轨迹与最终产出结果。"
    },
    "createEdge": {
      "description": "在两个节点模型中创建连接桥梁。当然，您更可以直接通过在节点的手柄圆点上拖拽出一条线来直观地构建连线图谱。"
    },
    "manageVariables": {
      "description": "统一定义全局共享变量 (比如各种 API key 或默认参数)，这样整个工作流所有的节点都能通用 ${变量名} 这一语法来提取并访问利用它们。"
    },
    "manageMemories": {
      "description": "跨越多次工作流执行，配置长期的工作记忆模块专门用作存储信息并支持快速的知识检索反馈。"
    },
    "renameWorkflow": {
      "description": "重新修改并调整此工作流配置文件的名称。"
    },
    "copyWorkflow": {
      "description": "为此完整的工作流模型资产创建一个同结构副本，它将被赋予一个新的副本名称存储到同目录下。"
    }
  }
}

en_data["help"] = en_help
zh_data["help"] = zh_help

with open(EN_PATH, "w", encoding="utf-8") as f:
    json.dump(en_data, f, ensure_ascii=False, indent=2)

with open(ZH_PATH, "w", encoding="utf-8") as f:
    json.dump(zh_data, f, ensure_ascii=False, indent=2)

print("Translations injected.")
