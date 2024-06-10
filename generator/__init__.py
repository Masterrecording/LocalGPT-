import llama_cpp
import json

class Response:
    def __init__(self, llama2_response: str, prompt: str):
        self.llama2_response = llama2_response
        self.prompt = prompt
        self.model = self.llama2_response["model"]
        self.role = self.llama2_response["choices"][0]["message"]["role"]
        self.response = self.llama2_response["choices"][0]["message"]["content"]
        
class Model:
    def __init__(self, model_path: str):
        self.llm = llama_cpp.Llama(
            model_path=model_path,
            chat_format="llama-2",
            n_ctx=2048,
            seed=0000
        )
        
    def generate(self, prompt: str, max_tokens: int = 128, stop: list = ["Q:"], echo: bool = True):
        completion = self.llm.create_chat_completion(
            messages=[
                {"role": "system", "content": "Eres un asistente útil llamado LocalGPT. Tienes que responder todas las preguntas de los usuarios."},
                {"role": "user", "content": prompt}
            ]
        )
        return Response(completion, prompt)