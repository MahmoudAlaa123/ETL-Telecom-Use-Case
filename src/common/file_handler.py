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

        Raises:
            FileNotFoundError: If the resulting absolute path does not point to an existing file.
        """
        # Get the current working directory
        cwd = os.getcwd()

        # Combine the current working directory with the relative path
        absolute_path = os.path.join(cwd, relative_path)

        # Check if the file exists
        if not os.path.exists(absolute_path):
            raise FileNotFoundError(f"No file found at {absolute_path}")

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


    
