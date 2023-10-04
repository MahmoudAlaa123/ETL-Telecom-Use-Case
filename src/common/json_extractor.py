import json
from common.file_handler import FileHandler

class JsonExtractor:


    @staticmethod
    def get_json_parsed_from_file(file_path: str) -> dict:
        """Get json content from path contating json file 

        Args:
            file_path (str): the path of file containing json

        Returns:
            data (dict): Dictionary containing the json content
        """

            # Read the file and get its content as a string
        json_string = FileHandler.read_resource_file(file_path)
            # Attempt to parse the JSON string into a Python dictionary
        data = JsonExtractor.extract_json_from_str(json_string)

        return data
    
    @staticmethod
    def extract_json_from_str(json_string: str) -> dict:
        """Extract json dictionary from string 

        Args:
            json_string (str): json in the string format

        Returns:
            data: dictionary represents the json

        Raises:
            error in case of any failures to convert the json string to dict        
        """
        try:
            data = json.loads(json_string)
            return data
        except json.JSONDecodeError as e:
            raise ValueError(str(e))
