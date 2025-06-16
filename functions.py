# business_module_template/functions.py
## IMPORTS HERE

## BUSINESS LOGIC FUNCTIONS HERE

async def template_function(session, param1, param2=None):
    try:
    #     # Your function logic here
    #     print(f"Processing template function with param1: {param1}")
        
    #     # Simulate some async work
    #     await asyncio.sleep(0.1)
        
    #     # Example session update
    #     session['template_data'] = {
    #         'param1': param1,
    #         'param2': param2,
    #         'processed_at': datetime.now().isoformat()
    #     }
        
        return "SUCCESS"
        
    except Exception as e:
        print(f"Error in template_function: {e}")
        return f"Failed to process request: {str(e)}"
    
async def cleanup_session_data(session):
    """
    Clean up heavy session data
    
    Args:
        session: Session to clean up
    """
    try:
        # Remove heavy data objects
        heavy_keys = ['large_data_1', 'large_data_2']
        for key in heavy_keys:
            session.pop(key, None)
            
        print("Session cleanup completed")
        
    except Exception as e:
        print(f"Error during session cleanup: {e}")