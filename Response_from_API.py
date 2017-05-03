import json

class Response_from_API(object):

    @staticmethod
    def input_value_json(self, inputtext):
            value = {
                "inputtext": inputtext,
                "email": "manikandan.rajappan@wipro.com"}
            data = json.dumps(value)
            response = self.restClient.post(self.url, data)

            return response

    @staticmethod
    def input_value_json_nlu(inputText,botInstance):
        value = {
            "inputPath":"/home/rootuser/BotRunENV/NLU_BOT/data/OS.json",
            "botInstance": botInstance,
            "inputText":inputText
        }
        return value