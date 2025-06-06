from .agent_base import AgentBase

class SanitizeDataValidatorAgent(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name="SanitizeDataValidatorAgent", max_retries=max_retries, verbose=verbose)

    def execute(self, original_data, sanitized_data):
        system_message = "You are an AI assistant that validates the sanitization of data by checking for the removal of unnecesaary information or foul language."
        user_content = (
            "Given the original data and the sanitized data, verify that all unnecesaary information or foul language has been removed.\n"
            "List any remaining unnecesaary information or foul language in the sanitized data and rate the sanitization process on a scale of 1 to 5, where 5 indicates complete sanitization.\n\n"
            f"Original Data:\n{original_data}\n\n"
            f"Sanitized Data:\n{sanitized_data}\n\n"
            "Validation:"
        )
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_content}
        ]
        validation = self.call_llama(messages, max_tokens=512)
        return validation
