# business_module_template/config.py
## MODULE'S CONFIGS HERE

# MODULE SPECIFIC CONFIGURATIONS
MODULE_SETTING_1 = "default_value"
MODULE_SETTING_2 = True

## AI CREDENTIAL AND CONFIGURATIONS
AI_API_KEY = "" ##SECRETS WILL BE HANDLED THROUGH DATABASE, FOR DEBUGGING PURPOSE IT IS STORED HERE

# AI CORE PROMPT TEMPLATE
AI_CORE_PROMPT = ""

# AI TOOLS TEMPLATE - Define your module's available functions
AI_TOOLS = [
    {
        "type": "function",
        "name": "template_function",
        "description": "Template function with parameters",
        "parameters": {
            "type": "object",
            "properties": {
                "param1": {
                    "type": "string",
                    "description": "Description of parameter 1"
                },
                "param2": {
                    "type": "integer",
                    "description": "Description of parameter 2"
                }
            },
            "required": ["param1"]
        }
    }
]

AI_MODEL = ""
AI_TEMPERATURE = 1.0