"""
TestAgentb1 - Custom Lambda Agent
Description: test ai chat agent

IMPORTANT: Only edit the code in the main() function below.
The Lambda handler will be automatically appended during deployment.
DO NOT add lambda_handler code here - it will be added automatically.
"""

def main(event_body):
    """Main function for TestAgentb1"""
    return {
        "success": True,
        "message": "Hello from TestAgentb1!",
        "data": event_body
    }
