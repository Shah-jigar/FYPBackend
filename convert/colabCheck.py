import sys

def is_running_in_colab():
    return 'google.colab' in sys.modules

# Example usage
if is_running_in_colab():
    print("Running in Colab environment")
else:
    print("Not running in Colab environment")
