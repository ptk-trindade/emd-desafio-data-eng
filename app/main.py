from dotenv import load_dotenv
import os

print("pwd", os.getcwd())

from pipelines.brt.flows import brt_flow

load_dotenv()

if __name__ == '__main__':
    brt_flow.run()


