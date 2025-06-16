# business_module_template/main.py
## IMPORTS HERE

## BUSINESS LOGIC CORE PROCESS HERE
import json
from datetime import datetime
from business_modules.base_module import BaseBusinessModule  ##REQUIRED

from .config import *
from .functions import (
    template_function,
    cleanup_session_data
)
from .utils import *

class ModuleNameModule(BaseBusinessModule):
    """Template business module implementation"""
    
    def __init__(self):
        super().__init__()
        self.module_name = "module_name"  # Change this to your module name
        self.version = "1.0.0"
    
    def get_ai_config(self):
        """Return AI configuration for this module"""
        return {
            "AI_MODEL": AI_MODEL, ##FROM CONFIG
            "AI_TEMPERATURE": AI_TEMPERATURE, ##FROM CONFIG
            "AI_TOOLS": AI_TOOLS, ##FROM CONFIG
        }
    
    def get_openai_api_key(self) -> str:
        """Return OpenAI API key based on environment"""
        return AI_API_KEY ##FROM CONFIG

    def get_next_state(self, current_state):
        """Define state transitions for your module"""
        state_transitions = {
            "get_greeting": "get_inquiry",
            "get_inquiry": "processing_request",
            "processing_request": "show_results",
            "show_results": "confirmation",
            "confirmation": "finalize",
            "finalize": "idle"
        }
        
        return state_transitions.get(current_state)

    def get_state_prompt(self, state):
        """Return state-specific prompts"""
        prompts = {
            "state_A": (
                "Specific prompt(s) for handling state A"
            ),
            
            "state_B": (
                "Specific prompt(s) for handling state B"
            ),
        
            "state_C": (
                "Specific prompt(s) for handling state C"
            )
        }
        
        return prompts.get(state, "Handle the user's request appropriately.")
    
    def get_failed_prompt(self, state):
        """Return prompts for failed states"""
        return (
            "There was an issue processing your request. "
            "Let me help you resolve this or try a different approach."
        )
    
    async def initialize_session(self, session):
        """Initialize session with module-specific data"""
        session['module_data'] = {
            'initialized_at': datetime.now().isoformat(),
            'requests_count': 0,
            'user_preferences': {}
        }
        
        # Add any module-specific initialization here
        print("Session initialized for module")

    async def get_greeting_setup(self, data):
        """Setup greeting configuration"""
        return "Hello, I am your Business AI Assistant"

    async def handle_function_call(self, session, function_call):
        """Handle function calls from AI"""
        status = None
        result = None
        buttons = None
        
        function = function_call.name
        args = json.loads(function_call.arguments)

        ## DEBUGGING PURPOSE
        print(f"Function: {function}")
        print(f"Args: {args}")
        
        # Update state to next state
        await session.set_current_state(self.get_next_state(function))
        
        if function == "function A":
            ## PROCESS FOR FUNCTION A CORRELATED CASE
            result = "function A processing result"
            status = "SUCCESS" ## SET STATUS "SUCCESS" IF PROCESSING SUCCEED, ELSE RETURN ERROR MESSAGE 
        
        elif function == "function B":
            ## PROCESS FOR FUNCTION A CORRELATED CASE
            result = "function B failed processing, error message: {error_message}"
            status = result ## RETURN "SUCCESS" IF PROCESSING SUCCEED, ELSE RETURN ERROR MESSAGE 
        
        elif function == "function C":
            ## PROCESS FOR FUNCTION A CORRELATED CASE
            result = "function C processing result, with buttons"
            buttons = [
                {
                    "text": "Button1 text",
                    "action": "Button1 action / callback data"
                },
                {
                    "text": "Button2 text",
                    "action": "Button2 action / callback data"
                }
            ]
            status =  "SUCCESS" ## RETURN "SUCCESS" IF PROCESSING SUCCEED, ELSE RETURN ERROR MESSAGE

        else:
            status = "FAILED"
            result = f"Unknown function: {function}"
        
        return status, result, buttons
    
    async def handle_document(self, session, document):
        """Handle document uploads (optional)"""
        if not document:
            return "No document provided."
        
        # Add document processing logic here
        return "Document processed successfully."
    
    async def cleanup_session(self, session):
        """Clean up session data when needed"""
        await cleanup_session_data(session) ##OPTIONAL, RECOMMENDED FOR SESSION CACHE MEMORY RESOURCE EFFICIENCY