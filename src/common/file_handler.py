import os

class FileHandler:

    @staticmethod
    def get_absolute_path(relative_path: str) -> str:
        """
        Get the absolute path given a relative path.

        Args:
            relative_path (str): The relative path.

        Returns:
            str: The absolute path.


        """
        # Get the current working directory
        cwd = os.getcwd()

        for root, _, files in os.walk(cwd):
                for file in files:
                    if file.lower() == relative_path:
                        absolute_path = os.path.join(root, file)



        return absolute_path
    

        

    @staticmethod
    def read_resource_file(filepath : str) -> str:
        """
        Get the content of the file as a string

        Args:
            filepath (str): The path of the file.

        Returns:
            str: The content of the file.
        """
        jsonfile = FileHandler.get_absolute_path(filepath)

        with open(jsonfile, 'r') as f:
             output = f.read()

        return output


    
