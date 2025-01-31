from fastapi import APIRouter
from api.backend.client.client import FibonacciRpcClient
from api.model.model import Data
import logging

router = APIRouter()


@router.get("/")
def test():
    return "API is running"


@router.post("/calculate")
def calculate_fibonacci(inputData: Data):
    fibonacci_rpc = FibonacciRpcClient()

    logging.info(" [x] Requesting fib(%s)" % inputData.fibNumber)
    response = fibonacci_rpc.call(inputData.fibNumber)
    logging.info(" [.] Got %r" % response)

    return {f"Fibbonacci number from {inputData.fibNumber}": response}
